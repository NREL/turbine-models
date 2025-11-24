import numpy as np
from turbine_models.parser import Turbines
from turbine_models.tools.extract_power_curve import extract_power_curve
from turbine_models.tools.power_curve_tools import pad_power_curve
import matplotlib.pyplot as plt

turbine = "NREL_6MW_170"
t_lib = Turbines()

turb_group = t_lib.find_group_for_turbine(turbine)
turbine_specs = t_lib.specs(turbine,group = turb_group)

# get the original thrust coefficient data from the power curve
original_power_curve = turbine_specs["power_curve"].dropna()
wind_speed_from_data = np.nan_to_num(original_power_curve["wind_speed_ms"].to_numpy())
ct_curve_from_data = np.nan_to_num(original_power_curve["ct"].to_numpy())
padded_wind_speed, padded_ct_from_data = pad_power_curve(wind_speed_from_data, ct_curve_from_data, ws_min = 0.0, ws_max = 50.0)

# remove Ct from the turbine specs power curve
turbine_specs["power_curve"] = turbine_specs["power_curve"].drop(columns=["ct"])

assert "ct" not in turbine_specs["power_curve"].columns.to_list()

# estimate Ct curve
power_curve = extract_power_curve(turbine_specs)

# plot the difference
fig, ax = plt.subplots(1,1)
ax.plot(power_curve["wind_speed"], power_curve["ct_curve"], c="tab:orange", label="Data")
ax.plot(padded_wind_speed, padded_ct_from_data, c="tab:blue", ls='--', label="Estimated")
ax.set_xlim([0,30])

ax.legend()
ax.set_xlabel("Wind Speed [m/s]")
ax.set_ylabel("Ct [-]")
fig.show()



