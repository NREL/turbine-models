from pathlib import Path

from turbine_models.make_turbine_data_summary import create_turbine_data_summary

output_dir = Path(__file__).parent / "outputs"
if not output_dir.is_dir():
    output_dir.mkdir(parents=True)

create_turbine_data_summary(output_dir)