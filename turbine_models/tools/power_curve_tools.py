import numpy as np
import matplotlib.pyplot as plt

def plot_power_curve(wind_speed, cp_curve, ct_curve):
    """Plot Cp and Ct curve per wind speed.

    Args:
        wind_speed (list | np.ndarray): list of wind speeds in m/s
        cp_curve (list | np.ndarray): power curve coefficients (Cp) at each wind speed in ``wind_speed``
        ct_curve (list | np.ndarray): thrust curve coefficients (Ct) at each wind speed in ``wind_speed``
    """
    betz_limit = 16/27
    fig,ax = plt.subplots(1,1)
    ax.plot(wind_speed, betz_limit*np.ones_like(wind_speed), ls='--', alpha=0.8, c="tab:red", label="Betz Limite")
    ax.plot(wind_speed, ct_curve, c='tab:blue', label="Coeff of Thrust")
    ax.plot(wind_speed, cp_curve, c='tab:orange', label="Coeff of Power")
    
    ax.legend()
    ax.set_xlabel("Wind Speed [m/s]")
    fig.show()


def pad_power_curve(wind_speed, curve, ws_min = 0.0, ws_max = 50.0):
    """Pad curve data with zeroes from wind speeds of ``ws_min`` to ``ws_max``. This method helps 
    avoid automated extrapolation to non-physical negative power values and avoid missing data 
    errors with common wind farm simulation tools such as FLORIS or PySAM.Windpower.

    Args:
        wind_speed (list | np.ndarray): list of wind speeds in m/s
        curve (list | np.ndarray): curve data at each wind speed in ``wind_speed``. Can be 
            either Cp, power, or Ct.
        ws_min (float, Optional): wind speed to start curve data at. Defaults to 0.0.
        ws_max (float, Optional): wind speed to end curve data at. Defaults to 50.0.

    Returns:
       2-element tuple containing:

       - **padded_wind_speed** (list): padded wind speed in m/s starting at ``ws_min`` and ending at ``ws_max``
       - **padded_curve** (list): padded curve data for wind speeds starting at ``ws_min`` and ending at ``ws_max``
    """
    
    if isinstance(wind_speed,list):
        wind_speed = np.array(wind_speed)
    if isinstance(curve,list):
        curve = np.array(curve)

    if min(wind_speed) > ws_min:
        wind_speed_pad = np.arange(ws_min,min(wind_speed),1)
        wind_speed = np.concatenate((wind_speed_pad,wind_speed))
        curve = np.concatenate((np.zeros_like(wind_speed_pad),curve))

    if max(wind_speed) < ws_max:
        wind_speed_pad = np.arange(max(wind_speed)+1,ws_max,1)
        wind_speed = np.concatenate((wind_speed,wind_speed_pad))
        curve = np.concatenate((curve,np.zeros_like(wind_speed_pad)))
    return wind_speed, curve

def calculate_cp_from_power(wind_speed, power_curve_kw, rotor_diameter, air_density = 1.225):
    """Calculate power coefficient curve (Cp) from power curve.

    Args:
        wind_speed (list | np.ndarray): list of wind speeds in m/s
        power_curve_kw (list | np.ndarray): turbine power (in kW) at each wind speed in ``wind_speed``
        rotor_diameter (float): rotor diameter of the turbine in meters.
        air_density (float, Optional): Air density assumed for power-curve calculations in kg/m3. 
            Defaults to 1.225.

    Raises:
        ValueError: if ``wind_speed`` and ``power_curve_kw`` are different lengths.

    Returns:
        np.ndarray: power curve coefficients (Cp) at each wind speed in ``wind_speed``
    """

    if len(wind_speed) != len(power_curve_kw):
        raise ValueError("The length of the wind speed and power vectors must be the same")
    
    if isinstance(wind_speed, list):
        wind_speed = np.array(wind_speed)
    if isinstance(power_curve_kw, list):
        power_curve_kw = np.array(power_curve_kw)
    
    # power available in the wind (kW)
    rotor_area = np.pi*((rotor_diameter/2)**2)
    p_wind = 0.5*air_density*rotor_area*(wind_speed**3)/1e3
    cp = power_curve_kw/p_wind
    cp = np.where(cp < 0, 0, cp)
    return cp

def calculate_power_from_cp(wind_speed, cp_curve, rotor_diameter, rated_power_kW, air_density = 1.225):
    """Calculate power curve from power coefficient curve (Cp).

    Args:
        wind_speed (list | np.ndarray): list of wind speeds in m/s
        cp_curve (list | np.ndarray): power curve coefficients (Cp) at each wind speed in ``wind_speed``
        rotor_diameter (float): rotor diameter of the turbine in meters.
        air_density (float, Optional): Air density assumed for power-curve calculations in kg/m3.
             Defaults to 1.225.
    
    Raises:
        ValueError: if ``wind_speed`` and ``cp_curve`` are different lengths.

    Returns:
        np.ndarray: turbine power (in kW) at each wind speed in ``wind_speed``
    """

    if len(wind_speed) != len(cp_curve):
        raise ValueError("The length of the wind speed and coefficient of power vectors must be the same")

    
    if isinstance(wind_speed, list):
        wind_speed = np.array(wind_speed)
    if isinstance(cp_curve, list):
        cp_curve = np.array(cp_curve)
    
    # power available in the wind (kW)
    rotor_area = np.pi*((rotor_diameter/2)**2)
    p_wind = 0.5*air_density*rotor_area*(wind_speed**3)/1e3
    power_kW = cp_curve*p_wind
    power_kW = np.where(power_kW > rated_power_kW, rated_power_kW, power_kW)
    power_kW = np.where(power_kW < 0, 0, power_kW)

    return power_kW

def estimate_thrust_coefficient(wind_speed, cp_curve, plot=False, print_output=False):
    """Calculate thrust coefficient curve (Ct) from power coefficient curve (Cp).

    Args:
        wind_speed (list | np.ndarray): list of wind speeds in m/s
        cp_curve (list | np.ndarray): power curve coefficients (Cp) at each wind speed in ``wind_speed``
        plot (bool, Optional): whether to plot Cp and Ct curve. Defaults to False.
        print_output (bool, Optional): Whether to print Cp and Ct curves. Defaults to False.
    
    Raises:
        ValueError: if ``wind_speed`` and ``cp_curve`` are different lengths.

    Returns:
        np.ndarray: thrust curve coefficients (Ct) at each wind speed in ``wind_speed``
    """
    
    # Check that the wind speed and the coefficient of power are the same length
    if len(wind_speed) != len(cp_curve):
        raise ValueError("The length of the wind speed and coefficient of power vectors must be the same")
    N_wind = len(wind_speed)
    ct_curve = np.zeros(N_wind)
    
    for i in range(N_wind):
        # calculate induction factor a
        # solve C_P = 4 * a * (1-a)**a  -> 4 * a**3 - 8 * a**2 + 4 * a - C_P = 0
        roots = np.roots([4, -8, 4, -cp_curve[i]])

        # Take root that is in range of a -> [0, 0.5]
        a = roots[np.where(np.logical_and(roots>= 0, roots<= 0.5))]

        # Calculate C_T = 4 * a * (1-a)
        ct = np.round(4 * a * (1-a), 4)
        
        ct_curve[i] = ct if isinstance(ct,(float,int)) else ct[0]
    
    ct_flat = ct_curve.flatten()

    if plot:
        plot_power_curve(wind_speed,cp_curve,ct_flat)

    if print_output:
        print("Wind  Speed (m/s) | Coefficient of Thrust (Ct) | Coefficient of Power (Cp)")
        for ws, ct, cp in zip(wind_speed, ct_flat, cp_curve):
            print(f"{ws:16.4f} | {ct:26.4f} | {cp:25.4f}")

    return ct_flat