from turbine_models.parser import Turbines
from turbine_models.tools.extract_power_curve import extract_power_curve
from turbine_models.tools.library_tools import check_turbine_library_for_turbine

turbine = "GE_1.5MW"
t_lib = Turbines()

turb_group = t_lib.find_group_for_turbine(turbine)
turbine_specs = t_lib.specs(turbine,group = turb_group)

is_valid = check_turbine_library_for_turbine(turbine)
power_curve = extract_power_curve(turbine_specs)
