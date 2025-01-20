# import parser
from turbine_models.parser import Turbines

# initialize parser
turbs = Turbines()

# get list of onshore turbines and print
turbine_type = "onshore"
onshore_turbs = turbs.turbines(group=turbine_type)
print(onshore_turbs)

#choose turbine from that list
turbine_name = '2020ATB_NREL_Reference_5.5MW_175'

#get dictionary of turbine specs
specs = turbs.specs(turbine_name)
keys_vals_str = [f"{k}: {v}" for k,v in specs.items() if k!= "power_curve"]
specs_strings = "\n -"
specs_strings += "\n -".join(keys_vals_str)
print(f"specs for {turbine_name} in group {turbine_type}:")
print(specs_strings)

#get turbine power curve table
power_curve = turbs.table(turbine_name)
print(f"power curve for {turbine_name} in group {turbine_type}:")
print(power_curve)
