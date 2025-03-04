import re

def check_string_for_floats(my_str):
    if isinstance(my_str, list):
        is_float = []
        for str_part in my_str:
            if any(k.isnumeric() for k in str_part.split(".")):
                is_float.append(True)
            else:
                is_float.append(False)
        return is_float
    if isinstance(my_str, str):
        is_float =  any(k.isnumeric() for k in my_str.split("."))
        return is_float
    return None

def check_name_for_power(name):
    power_options = []
    power_units = ''
    if "kW" in name:
        power_units = "kW"
        power_str = name.split("kW")[0].split("_")[-1]
    if "MW" in name:
        power_units = "MW"
        power_str = name.split("MW")[0].split("_")[-1]
    if power_units == '':
        return []
    if all(k.isnumeric() for k in power_str.split(".")):
        if "." in power_str:
            power = float(power_str)
        else:
            power = int(power_str)
    power_options.append(f"{power}{power_units}")
    if power_units == "MW":
        #check float version and kW
        if isinstance(power,float) and power_str.split(".")[-1].replace("0","")=='':
            power_options.append("{}MW".format(int(power)))
        elif isinstance(power,int):
            power_options.append("{}MW".format(float(power)))
        
        power_kw = power*1e3
        power_options.append("{}kW".format(float(power_kw)))
        power_options.append("{}kW".format(int(power_kw)))
        
    if power_units == "kW":
        # check float version and MW
        if isinstance(power,float) and power_str.split(".")[-1].replace("0","")=='':
            power_options.append("{}kW".format(int(power)))
        elif isinstance(power,int):
            power_options.append("{}kW".format(float(power)))
        power_mw = power/1e3
        if str(power_mw).split(".")[0]!="0":
            # greater than 1 MW
            power_options.append("{}MW".format(float(power_kw)))
            if str(power_mw).split(".")[-1]=="0":
                power_options.append("{}MW".format(int(power_kw)))
    return power_options
    
def split_name_for_description_parts(name):
    name_parts = []
    # idx_upper = [i for i,k in enumerate(name) if k.isupper()]
    # number followed by name: "2020ATB"
    numal_parts = re.findall("([0-9]+[a-zA-Z]+)",name)
    #name followed by number: "BergeyExcel15_v1"
    alnum_parts = re.findall("([a-zA-Z]+[0-9]+)",name)
    #name followed by number and letter: "NPS100C"
    alnumal_parts = re.findall("([a-zA-Z]+[0-9]+[a-zA-Z]+)",name)
    #find all clumps of alphabetic character greater than 1
    alpha_parts = [k for k in re.findall("([a-zA-Z]+)", name) if len(k)>1]
    alpha_parts = [k for k in alpha_parts if k!= "kW"]
    alpha_parts = [k for k in alpha_parts if k!= "MW"]
    
    parts = numal_parts + alnum_parts + alnumal_parts + alpha_parts
    #name followed by number and letter: "NPS100C"
    # re.findall("([a-zA-Z]+[0-9]+[a-zA-Z]+)","NPS100C")
    for a_part in parts:
        []
        if len(re.findall("([a-zA-Z]+[0-9]+[a-zA-Z]+)",a_part))>=1:
            name_parts.extend(re.findall("([a-zA-Z]+[0-9]+[a-zA-Z]+)",a_part))
        elif len(re.findall("([a-zA-Z]+[0-9]+)",a_part))>=1:
            name_parts.extend(re.findall("([a-zA-Z]+[0-9]+)",a_part))
        # split parts of capital followed by lowercase
        # ex: BergeyExcel returns Bergey Excel
        elif len(re.findall("([A-Z]+[a-z]+)", a_part))>1:
            name_parts.extend(re.findall("([A-Z]+[a-z]+)", a_part))
        # find consecutive capitalized
        elif len(re.findall("([A-Z]+)",a_part))>1:
            name_parts.extend(re.findall("([A-Z]+)",a_part))
        elif len(re.findall("([a-z]+)",a_part))>1:
            name_parts.extend(re.findall("([a-z]+)",a_part))
        else:
            name_parts.append(a_part)
    return name_parts



def check_input_name_params(name):
    # 1) check power
    power_options = check_name_for_power(name)
    # 2) check rotor diameter
    name_parts = name.split("_")
    numeric_parts = check_string_for_floats(name_parts)
    rotor_diam_parts = []
    if numeric_parts.count(True) >= 1:
        for ii,is_num in enumerate(numeric_parts):
            if is_num:
                if "kW" not in name_parts[ii] and "MW" not in name_parts[ii]:
                    rotor_diam = name_parts[ii]
                    rotor_diam_parts.append(f"{rotor_diam}")
        
    # 3) check nane parts
    desc_options = split_name_for_description_parts(name)
    desc_options += power_options
    desc_options += rotor_diam_parts
    return desc_options

def check_well_defined_parts(name):
    full_desc_parts = check_input_name_params(name)
    name_desc_parts = split_name_for_description_parts(name)
    if len(full_desc_parts)>len(name_desc_parts):
        return True
    return False    

def check_turbine_group_for_possible_matches(parser, group, input_name_keywords, well_defined):

    possible_matches = []
    options = list(parser.turbines(group=group).values())
    
    for turb in options:
        turb_opt_parts = check_input_name_params(turb)
        # check parts across turb
        match_parts = [k for k in input_name_keywords if k in turb_opt_parts]
        # check parts in full string
        match_str = [k for k in input_name_keywords if k in turb]
        if len(match_parts) == len(input_name_keywords):
            if well_defined:
                return turb
            possible_matches.append(turb)
        if len(match_parts)>0 or len(match_str)>0:
            if turb not in possible_matches:
                possible_matches.append(turb)
        
    return possible_matches

def get_best_match_turbine_in_group(parser, group,turbine_input_name):
    well_defined_desc = check_well_defined_parts(turbine_input_name)
    turbine_desc_parts = check_input_name_params(turbine_input_name)
    possible_matches = check_turbine_group_for_possible_matches(parser,group,turbine_desc_parts,well_defined_desc)
    best_matches = []
    max_match = 1
    if isinstance(possible_matches,list):
        for turb in possible_matches:
            turb_opt_parts = check_input_name_params(turb)
            match_parts = [k for k in turbine_desc_parts if k in turb_opt_parts]
            match_str = [k for k in turbine_desc_parts if k in turb]
            match_overlap = [k for k in match_parts if k not in match_str]
            match_overlap += [k for k in match_str if k not in match_overlap]
            if len(match_overlap)>=max_match:
                if len(match_overlap)>max_match:
                    best_matches = turb
                    max_match = len(match_overlap)
                else:
                    if isinstance(best_matches,str):
                        best_matches = [best_matches]
                    best_matches.append(turb)
        has_name = [k for k in best_matches if turbine_input_name in k]
        if len(has_name)>0:
            return has_name
        else:
            return best_matches
        
    else:
        if well_defined_desc:
            return possible_matches
        return [possible_matches]

def get_best_match_turbine_from_options(turbine_input_name, possible_matches, max_match = 1):
    turbine_desc_parts = check_input_name_params(turbine_input_name)
    best_matches = []
    if isinstance(possible_matches,list):
        for turb in possible_matches:
            turb_opt_parts = check_input_name_params(turb)
            match_parts = [k for k in turbine_desc_parts if k in turb_opt_parts]
            match_str = [k for k in turbine_desc_parts if k in turb]
            match_overlap = [k for k in match_parts if k not in match_str]
            match_overlap += [k for k in match_str if k not in match_overlap]
            if len(match_overlap)>=max_match:
                if len(match_overlap)>max_match:
                    best_matches = turb
                    max_match = len(match_overlap)
                else:
                    if isinstance(best_matches,str):
                        best_matches = [best_matches]
                    best_matches.append(turb)
            
        return best_matches
    else:
        return [possible_matches]

def get_best_match_turbine_in_library(turbine_name, parser):
    possible_matches_all = []

    for group in parser.groups:
        best_matches_group = get_best_match_turbine_in_group(parser, group, turbine_name)
        if isinstance(best_matches_group,str):
            return best_matches_group
        if best_matches_group is not None:
            possible_matches_all += best_matches_group
    
    if len(possible_matches_all)==1:
        return possible_matches_all[0]
    if len(possible_matches_all)==0:
        error_msg = (
            f"Cannot find turbine with description matching {turbine_name}. "
            "No turbine names with a similar description were found."
            "To see a list of turbines in a group, for example try: `Turbines.turbines(group=group_name)`. "
            f"Valid group names include: {parser.groups}." 
        )
        raise ValueError(error_msg)
    else:
        best_options_remaining = get_best_match_turbine_from_options(turbine_name, possible_matches_all, max_match = 1)
        ii = 2
        while len(best_options_remaining)>0:
            best_options = [k for k in best_options_remaining]
            best_options_remaining = get_best_match_turbine_from_options(turbine_name, possible_matches_all, max_match = ii)
            ii +=1
            if len(best_options_remaining)==1:
                return best_options_remaining[0]
        error_msg = (
            f"Found multiple turbines with description matching {turbine_name}. "
            f"Turbine names that fit your description include: {best_options}"
        )
        raise ValueError(error_msg)
    

