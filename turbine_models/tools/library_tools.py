from turbine_models.parser import Turbines
from turbine_models.supported_turbines import supported_turbines, missing_information_turbines

def check_turbine_library_for_turbine(turbine_name:str, turbine_group = "none"):
    """Check turbine-models library for turbine named ``turbine_name``.

    Args:
        turbine_name (str): name or nickname of turbine in turbine-models library
        turbine_group (str, Optional): group of turbine in turbine-models library.
            Options include "offshore", "onfshore", or "distributed".

    Returns:
        bool: whether the input turbine name matches a turbine available in the turbine-models library.
    """

    if turbine_name in supported_turbines:
        return True

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

def print_turbines_in_group(group_name, all_turbines, print_nicknames):
    """Print the turbine names for each group of turbines in turbine-models library.

    Args:
        group_name (str): group of turbine names to print, must be either "offshore", 
            "onshore", or "distributed".
        all_turbines (bool): If True, include the turbines that have missing information. 
            If False, only include the turbines with sufficient data.
        print_nicknames (bool): If True, print the nicknames of turbines. 
            If False, print the full name of turbines.

    """

    valid_groups = ["offshore","onshore","distributed"]
    if group_name.lower() not in valid_groups:
        raise ValueError(f"{group_name} is not a valid turbine group. Valid groups are: {valid_groups}")
    
    t_lib = Turbines()
    turbine_names = list(t_lib.turbines(group=group_name.lower()).values())

    fullname_to_nickname = {v:k for k,v in supported_turbines.items() if v in turbine_names}

    if not all_turbines and print_nicknames:
        # print nicknames and only include valid turbines
        turbines_to_print = [nickname for fullname,nickname in fullname_to_nickname.items() if nickname not in missing_information_turbines]
    if not all_turbines and not print_nicknames:
        # print fullnames and only include valid turbines
        turbines_to_print = [fullname for fullname,nickname in fullname_to_nickname.items() if nickname not in missing_information_turbines]
    if all_turbines and print_nicknames:
        # print nicknames and include all turbines
        turbines_to_print = list(fullname_to_nickname.values())
    if all_turbines and not print_nicknames:
        # print fullnames and include all turbines
        turbines_to_print = list(fullname_to_nickname.keys())

    msg = "\n " + "\n ".join(t for t in turbines_to_print)
    print(msg)
    return


def print_turbine_name_list(all_turbines=False, print_nicknames=False):
    """Print the turbine names for each group of turbines in turbine-models library.

    Args:
        all_turbines (bool, optional): If True, include the turbines that have missing information. 
            If False, only include the turbines with sufficient data. Defaults to False.
        print_nicknames (bool, optional): If True, print the nicknames of turbines. 
            If False, print the full name of turbines. Defaults to False.

    """
    
    print("-".join("" for i in range(25)))
    print("Offshore Turbine Names:")
    print("-".join("" for i in range(25)))
    print_turbines_in_group("offshore",all_turbines,print_nicknames)

    
    print("-".join("" for i in range(25)))
    print("Onshore Turbine Names:")
    print("-".join("" for i in range(25)))
    print_turbines_in_group("onshore",all_turbines,print_nicknames)

    print("-".join("" for i in range(25)))
    print("Distributed Turbine Names:")
    print("-".join("" for i in range(25)))
    print_turbines_in_group("distributed",all_turbines,print_nicknames)
    