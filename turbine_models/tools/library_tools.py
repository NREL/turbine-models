from turbine_models.parser import Turbines

def check_turbine_library_for_turbine(turbine_name:str, turbine_group = "none"):
    """Check turbine-models library for turbine named ``turbine_name``.

    Args:
        turbine_name (str): name of turbine in turbine-models library
        turbine_group (str, Optional): group of turbine in turbine-models library.
            Options include "offshore", "onfshore", or "distributed".

    Returns:
        bool: whether the input turbine name matches a turbine available in the turbine-models library.
    """

    t_lib = Turbines()
    valid_name = False
    if turbine_group not in t_lib.groups:
        for turb_group in t_lib.groups:
            turbines_in_group = t_lib.turbines(group = turb_group)
            if any(turb.lower()==turbine_name.lower() for turb in turbines_in_group.values()):
                valid_name = True
    else:
        turbines_in_group = t_lib.turbines(group = turbine_group)
        if any(turb.lower()==turbine_name.lower() for turb in turbines_in_group.values()):
            valid_name = True
    return valid_name

def print_turbine_name_list():
    """Print the turbine names for each group of turbines in turbine-models library.
    """
    
    t_lib = Turbines()
    osw_turbines = list(t_lib.turbines(group="offshore").values())
    
    print("-".join("" for i in range(25)))
    print("Offshore Turbine Names:")
    print("-".join("" for i in range(25)))
    osw_msg = "\n " + "\n ".join(t for t in osw_turbines)
    print(osw_msg)

    lbw_turbines = list(t_lib.turbines(group="onshore").values())
    print("-".join("" for i in range(25)))
    print("Onshore Turbine Names:")
    print("-".join("" for i in range(25)))
    lbw_msg = "\n " + "\n ".join(t for t in lbw_turbines)
    print(lbw_msg)

    distributed_turbines = list(t_lib.turbines(group="distributed").values())
    print("-".join("" for i in range(25)))
    print("Distributed Turbine Names:")
    print("-".join("" for i in range(25)))
    dw_msg = "\n " + "\n ".join(t for t in distributed_turbines)
    print(dw_msg)