

import os
import glob
import pandas as pd
import numpy as np

import intake

from smrt import make_snowpack
#, sensor_list, make_model
from smrt.core.interface import make_interface


class AntarcticSnowpacks(object):

    def __init__(self, remove_meagadunes=True):
        self.cat = intake.open_catalog(os.path.join(os.path.dirname(__file__), "../data/AntarcticData/catalog.yml"))
        self.database = self.cat.sites_with_tbs.read().set_index('site').sort_values('lat')

        if remove_meagadunes:
            self.database = self.database.iloc[5:]  # remove the site in the megadune

        self.sites = self.database.index

        self.profiles = self.cat.profiles.read().set_index('site')
        print("profiles", self.profiles)

    def prepare_snowpacks(self,
                          site,
                          add_rough_interface=False,
                          microstructure=['TS'],
                          summer_simulation=False,
                          params={}):
        """prepare the snowpack for a given site"""

        info = self.database.loc[site]
        profile = self.profiles.loc[site].copy()

        profile = compute_thickness(profile)
        profile = expand_profile(profile)
        profile['thickness'].iloc[-1] = 1000

        density_ice = 917.
        corr_length = 4 * (1 - profile.density / density_ice) / (density_ice * profile.ssa)
        porod_length = corr_length
        radius = 3 / (density_ice * profile.ssa)

        microstructure_dict = {
            "TS": dict(microstructure_model="teubner_strey", corr_length=corr_length,
                       repeat_distance=2 * np.pi * params.get('coef_TS', 0.92) * corr_length),
            "GF": dict(microstructure_model="gaussian_random_field", corr_length=corr_length,
                       repeat_distance=2 * np.pi * params.get('coef_GF', 0.92) * corr_length),
            "EXP": dict(microstructure_model="exponential", corr_length=params.get('coef_EXP', 0.625) * corr_length),
            "SHS": dict(microstructure_model="sticky_hard_spheres", radius=radius, stickiness=params.get('stickiness', 0.14)),
            "SHSPI20": dict(microstructure_model="sticky_hard_spheres_picard2020", corr_length=corr_length, 
                            polydispersity=params.get('coef_SHSPI20', 0.625)),
            
            "USEXP": dict(microstructure_model="unified_scaled_exponential", porod_length=porod_length, polydispersity=params.get('polydispersity', 0.625)),
            "UTS": dict(microstructure_model="unified_teubner_strey", porod_length=porod_length, polydispersity=params.get('polydispersity', 0.6)),
            "USHS": dict(microstructure_model="unified_sticky_hard_spheres", porod_length=porod_length, polydispersity=params.get('polydispersity', 0.64)),
        }

        if add_rough_interface:
            interface = make_interface("geometrical_optics_backscatter", mean_square_slope=info['mss'])
        else:
            interface = None

        sp = {m: make_snowpack(profile.thickness,
                               density=profile.density,
                               temperature=(info.skt_summer + 273.15) if summer_simulation else (info.temperature + 273.15),
                               interface=interface,
                               **microstructure_dict[m]) for m in microstructure_dict if m in microstructure}
        return sp


def expand_profile(profile):

    maxdepth = profile.z.max()
    n = int(max(0, 15 - maxdepth))  # repeat over 15 meters

    profile_last_meter = profile[profile.z < profile.z.min() + 1]
    profile = pd.concat([profile] + [profile_last_meter] * n)
    profile['z'] = -profile['thickness'].cumsum()

    return profile


def compute_thickness(profile):

    profile = profile.copy()
    profile['thickness'] = np.abs(np.diff(np.insert(profile.z.values, 0, 0)))
    return profile
