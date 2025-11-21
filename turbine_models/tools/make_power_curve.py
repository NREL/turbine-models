import numpy as np
import turbine_models.tools.power_curve_tools as curve_tools

def extract_power_curve(turbine_specs: dict) -> dict[str, list[float]]:
    """Creates power-curve dictionary containing Ct, Cp, wind speeds, and power (in kW) 
    for a turbine based on available data.

    Args:
        turbine_specs (dict): turbine specs loaded from turbine-models library.

    Raises:
        ValueError: if turbine data doesn't have the minimum required power-curve information.

    Returns:
        dict[str,list[float]]: power-curve dictionary with keys of:
            - 'wind_speed': wind speeds [m/s].
            - 'ct_curve': Thrust coefficient (Ct) curve for each wind speed [-].
            - 'cp_curve': Power coefficient (Cp) curve for each wind speed [-].
            - 'power_curve_kw': power curve for each wind speed [kW]
    """

    turbine_specs["power_curve"] = turbine_specs["power_curve"].dropna()
    wind_speeds = np.nan_to_num(turbine_specs["power_curve"]["wind_speed_ms"].to_numpy())
    turbine_curve_cols = turbine_specs["power_curve"].columns.to_list()
    
    has_cp_curve = "cp" in turbine_curve_cols
    has_power_curve = "power_kw" in turbine_curve_cols
    has_ct_curve = "ct" in turbine_curve_cols
    
    if not has_cp_curve and not has_power_curve:
        turbine_name = turbine_specs["name"]
        msg = (
            f"Turbine {turbine_name} does not have the minimum required power curve data. "
            "Either power_kw or cp are required."
            )
        raise ValueError(msg)
    
    if has_cp_curve:
        cp_curve = np.nan_to_num(turbine_specs["power_curve"]["cp"].to_numpy())
        cp_curve = np.where(cp_curve<0,0,cp_curve).tolist()

    if has_power_curve:
        power_curve_kw = np.nan_to_num(turbine_specs["power_curve"]["power_kw"].to_numpy())
        power_curve_kw = np.where(power_curve_kw<0,0,power_curve_kw)
        power_curve_kw = np.where(power_curve_kw>turbine_specs["rated_power"],turbine_specs["rated_power"],power_curve_kw).tolist()

    if has_cp_curve and not has_power_curve:
        power_curve_kw = curve_tools.calculate_power_from_cp(wind_speeds,cp_curve,turbine_specs["rotor_diameter"],turbine_specs["rated_power"])
    
    if has_power_curve and not has_cp_curve:
        cp_curve = curve_tools.calculate_cp_from_power(wind_speeds,power_curve_kw)
        
    if has_ct_curve:
        ct = turbine_specs["power_curve"]["ct"].to_numpy()
    else:
        ct = curve_tools.estimate_thrust_coefficient(wind_speeds,cp_curve)
    
    _, cp_curve = curve_tools.pad_power_curve(wind_speeds,cp_curve)
    _, ct = curve_tools.pad_power_curve(wind_speeds,ct)
    wind_speeds, power_curve_kw = curve_tools.pad_power_curve(wind_speeds,power_curve_kw)
    
    power_thrust_table = {
        "ct_curve":ct,
        "cp_curve":cp_curve,
        "wind_speed":wind_speeds,
        "power_curve_kw":power_curve_kw,
        }
    return power_thrust_table
