import numpy as np
from turbine_models.parser import Turbines
from turbine_models.tools.extract_power_curve import extract_power_curve
from turbine_models.supported_turbines import missing_information_turbines

def get_pysam_turbine_specs(turbine_name):
    """Load turbine data from turbine-models library to use with PySAM wind simulation.

    Args:
        turbine_name (str): name of turbine in turbine-models library

    Raises:
        ValueError: if turbine is missing data.

    Returns:
        dict: turbine model dictionary formatted for PySAM.
    """
    if turbine_name in missing_information_turbines:
        raise ValueError(f"{turbine_name} turbine does not have enough information to model in PySAM.")
    
    t_lib = Turbines()
    turbine_specs = t_lib.specs(turbine_name)

    if not isinstance(turbine_specs,dict):
        msg = (
            f"Turbine {turbine_name} is missing some data, "
            "please try another turbine."
        )
        raise ValueError(msg)

    if isinstance(turbine_specs["hub_height"],(list,np.ndarray)):
        hub_height = np.median(turbine_specs["hub_height"])
    else:
        hub_height = turbine_specs["hub_height"]

    power_curve = extract_power_curve(turbine_specs)

    turbine_dict = {
        "wind_turbine_max_cp": max(power_curve.get("cp_curve")),
        "wind_turbine_ct_curve": power_curve.get("ct_curve"),
        "wind_turbine_powercurve_windspeeds": power_curve.get("wind_speed"),
        "wind_turbine_powercurve_powerout": power_curve.get("power_curve_kw"),
        "wind_turbine_rotor_diameter": turbine_specs["rotor_diameter"],
        "wind_turbine_hub_ht": hub_height,
    }
    return turbine_dict


def get_floris_turbine_specs(turbine_name):
    """Load turbine data from turbine-models library to use with FLORIS wind simulation. 
    
    Sets turbine's rated tip speed ratio (TSR) to 8.0 if not included in turbine data.
    Sets default values in the power thrust table as:
    
    - ``ref_air_density``: 1.225
    - ``ref_tilt``: 5.0
    - ``cosine_loss_exponent_yaw``: 1.88
    - ``cosine_loss_exponent_tilt``: 1.88

    Args:
        turbine_name (str): name of turbine in turbine-models library

    Raises:
        ValueError: if turbine is missing data.

    Returns:
        dict: turbine model dictionary formatted for FLORIS.
    """

    if turbine_name in missing_information_turbines:
        raise ValueError(f"{turbine_name} turbine does not have enough information to model in PySAM.")

    t_lib = Turbines()
    turb_group = t_lib.find_group_for_turbine(turbine_name)
    turbine_specs = t_lib.specs(turbine_name,group = turb_group)

    if not isinstance(turbine_specs,dict):
        msg = (
            f"Turbine {turbine_name} is missing some data, "
            "please try another turbine."
        )
        raise ValueError(msg)


    if isinstance(turbine_specs["hub_height"],(list,np.ndarray)):
        hub_height = np.median(turbine_specs["hub_height"])
    else:
        hub_height = turbine_specs["hub_height"]
    
    power_curve = extract_power_curve(turbine_specs)

    power_thrust_table = {
        "wind_speed": power_curve.get("wind_speed"),
        "power": power_curve.get("power_curve_kw"),
        "thrust_coefficient": power_curve.get("ct_curve"),
        "ref_air_density": 1.225,
        "ref_tilt": turbine_specs.get("rotor_tilt_angle", 5.0),
        "cosine_loss_exponent_yaw": 1.88,
        "cosine_loss_exponent_tilt": 1.88,
    }

    turbine_dict = {
        "turbine_type":turbine_name,
        "hub_height":hub_height,
        "TSR": turbine_specs.get("rated_tsr", 8.0),
        "rotor_diameter":turbine_specs.get("rotor_diameter"),
        "power_thrust_table": power_thrust_table,
    }
    return turbine_dict

    
