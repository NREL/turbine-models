from turbine_models.tools.interface_tools import get_pysam_turbine_specs, get_floris_turbine_specs
from turbine_models.tools.library_tools import check_turbine_library_for_turbine

turbine = "GE_1.5MW"
# check if turbine name is valid
is_valid = check_turbine_library_for_turbine(turbine)

if is_valid:
    # get dictionary of turbine specs formatted for PySAM
    pysam_turbine_dict = get_pysam_turbine_specs(turbine)
    # get dictionary of turbine specs formatted for FLORIS
    floris_turbine_dict = get_floris_turbine_specs(turbine)

