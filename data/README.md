

This dataset contains measurements of snow properties and observations of microwave brightness temperature from Antarctica and Canada. It also contains snow microstructure properties derived from micro-CT imagery  from laboratory experiments and the Alps. This dataset was established to run and evaluate microwave scattering simulations. The results are presented in G. Picard, H. Löwe, F. Domine, L. Arnaud, F. Larue, V. Favier, E. Le Meur, E. Lefebvre, J. Savarino, A. Royer, The snow microstructural control on microwave scattering, to be published in AGU Advances.


# CanadaData/SP.xlsx

Excel file with snow properties profiles at 83 sites in Canada.

Each sheet corresponds to one snowpit and provides:
- Hneige: height of the measurement
- TEMPERATURE: temperature (°C)
- Density: snow density (kg/m3)
- SSA: Snow Specific surface area (m2/kg)
- Hneige_cm: thickness of the layer (cm)
- Temp_Kel: temperature (K)
- Ropt: optical radius deduced from the SSA
- Hneige (m): thickness of the layer (m)
- TempSol: Soil temperature

# CanadaData/TB.csv

csv file with ground-based brigthness temperature measurements.

The columns give the following information:
- zone:  ecozone
- CorresS: name of the snowpit
- site: name of the area
- Date: date of the snowpit measurements
- 10H 10V 19H 19V 37H 37V 89H 89V: measurements at each frequency and polarization

# AntarcticData/TB.csv

csv file with microwave observations and metadata for 18 sites in Antarctica.

The columns give the following information:
- site: name of the snowpit
- shortname: short name of the snowpit
- campaign: name of the measurement campaign
- lat,lon: geographical coordinates
- temperature: mean annual temperature from ERA5 (K)
- 10V,10H,19V,19H,37V,37H,89V,89H: annual mean AMSR2 brightness temperature (K) at each frequency and polarization
- 10V_summer,10H_summer,19V_summer,19H_summer,37V_summer,37H_summer,89V_summer,89H_summer: summer mean satellite brightness temperature (K) at each frequency and polarization
- skt,skt_summer: annual mean and summer mean skin temperatures (K) from ERA5
- 
# AntarcticData/profiles/

csv files with snow properties profiles at 18 sites in Antarctica.

- z: depth (m)
- density: snow density (kg/m3)
- ssa: specific surface area (m2/kg)

# MicroCTData/metadata-samples.dat

csv file with metadata for all the samples.

The columns give the following information:
- sampleid: number of the sample
- group: name of the experiment
- main_type: main snow type
- sub_type: sub snow type
- filename: name of the sample file
- time_in_h: duration of the experiment (h)
- T_in_K: temperature of the experiment (K)
- nablaT_in_K_per_m: temperature gradient of the experiment (K/m)

# MicroCTData/ice_vol_frac.dat

csv file with fractional volume for all the samples.

The columns give the following information:
- sample id
- fractional volume (no unit)

# MicroCTData/\*\_chords.dat

csv files with the chord length distribution for each snow sample.

Each row corresponds to a length (in pixel) and gives the number of ice and pore(=air) chords found in the tomography in the x, y, z directions.
The resolution of the pixel is given in the header part, in line "#el_size".


# Main references:

Canadian data: C. Vargel, A. Royer, O. St-Jean-Rondeau, G. Picard, A. Roy, V. Sasseville, A. Langlois, Arctic and Subarctic snow microstructure analysis for microwave brightness temperature simulations, Remote Sensing of Environment, 241, 111754, doi: 10.1016/j.rse.2020.111754, 2020

micro-CT data: Löwe, H., Riche, F., & Schneebeli, M. (2013). A general treatment of snow microstructure exemplified by an improved relation for thermal conductivity. The Cryosphere, 7(5), 1473–1480. doi:10.5194/tc-7-1473-2013

Krol, Q. and Löwe, H.: Relating optical and microwave grain metrics of snow: the relevance of grain shape, The Cryosphere, 10, 2847–2863, doi:10.5194/tc-10-2847-2016, 2016

Antarctic data: Larue, F., Picard, G., Aublanc, J., Arnaud, L., Robledano-Perez, A., Meur, E. L., Favier, V., Jourdain, B., Savarino, J., & Thibaut, P. (2021). Radar altimeter waveform simulations in Antarctica with the Snow Microwave Radiative Transfer Model (SMRT). Remote Sensing of Environment, 263, 112534. doi:10.1016/j.rse.2021.112534

