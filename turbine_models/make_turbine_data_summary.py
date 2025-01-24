from turbine_models.parser import Turbines
import pandas as pd
import turbine_models
import os
import yaml

def write_yaml(filename,data):
    if not '.yaml' in filename:
        filename = filename +'.yaml'

    with open(filename, 'w+') as file:
        yaml.dump(data, file,sort_keys=False,encoding = None,default_flow_style=False)
    return filename

def write_turbine_list_to_file(output_dir,group="all"):
    t = Turbines()
    version = turbine_models.__version__
    output_filepath = os.path.join(output_dir,f"{group}_turbines_list_v{version}.yaml")

    if group=="all":
        turb_group_list = {}
        for group in t.groups:
            turbs = t.turbines(group=group)
            turb_name_idx = {v:{"index":k} for k,v in turbs.items()}
            turb_group_list.update({group:turb_name_idx})
        write_yaml(output_filepath,turb_group_list)
    else:
        turbs = t.turbines(group=group)
        turb_name_idx = {v:{"index":k} for k,v in turbs.items()}
        write_yaml(output_filepath,turb_name_idx)

    print(f"wrote list of {group} turbines to {output_filepath}")

def create_turbine_data_summary(output_dir):
    data_summary = {}
    keys = ["turbine_rating_kW","turbine_idx","rotor_diameter","hub_height","cp_curve","power_curve","ct_curve"]
    t = Turbines()
    for group in t.groups:
        turbs = t.turbines(group=group)
        n_turbs = len(turbs.keys())
        data_summary.update({group:{}})
        for turb_indx,turb in turbs.items():
            t_specs = t.specs(turb,group=group)
            if isinstance(t_specs,dict):
                has_rd = t_specs["rotor_diameter"] is not None
                has_cp_curve = "cp" in t_specs["power_curve"].columns.to_list()
                has_ct_curve = "ct" in t_specs["power_curve"].columns.to_list()
                has_power_curve = "power_kw" in t_specs["power_curve"].columns.to_list()
                if t_specs["hub_height"] is not None:
                    if isinstance(t_specs["hub_height"],list):
                        hh_type = "multiple options"
                    elif isinstance(t_specs["hub_height"],(int,float)):
                        hh_type = "single value"
                else:
                    hh_type = False
                v = [t_specs["rated_power"],turb_indx,has_rd,hh_type,has_cp_curve,has_power_curve,has_ct_curve]
                data_summary[group].update({turb:dict(zip(keys,v))})
            elif isinstance(t_specs,pd.DataFrame):
                has_cp_curve = "cp" in t_specs.columns.to_list()
                has_ct_curve = "ct" in t_specs.columns.to_list()
                has_power_curve = "power_kw" in t_specs.columns.to_list()
                v = [None,turb_indx,False,None,has_cp_curve,has_power_curve,has_ct_curve]
                data_summary[group].update({turb:dict(zip(keys,v))})
    version = turbine_models.__version__
    output_filepath = os.path.join(output_dir,f"turbine_models_turbine_data_list_v{version}.yaml")
    write_yaml(output_filepath,data_summary)
    print(f"wrote turbine model summary to {output_filepath}")
    return data_summary

