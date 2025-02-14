from turbine_models.make_turbine_data_summary import create_turbine_data_summary
import os

output_dir = os.path.dirname(__file__,"outputs")
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

create_turbine_data_summary(output_dir)