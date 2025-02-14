# -*- coding: utf-8 -*-
"""Functions for listing and accessing turbine-model data.

Created on Wed Apr 21 14:12:17 2021

@author: twillia2
"""
import os
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import turbine_models
import yaml

class Turbines:
    """Access power curves from NREL's turbine-models repository."""

    def __repr__(self):
        """Return representation string for Turbines object."""
        nt = self.nturbines
        msg = f"<Turbines object: groups={self.groups}, nturbines={nt}>"
        return msg

    def curve(self, index, group="onshore", field="power_kw",
              interval=0.25):
        """Get an interpolated power curve for a specific turbine.
        
        Parameters
        ----------
        index : int
            Index position of turbine in table for given group.
        group : str
            Group name in which target turbine is contained.
        field : str
            Target field in turbine table (power_kw, cp, etc.).
        interval : int | float
            Windspeed interval in which to return target field values.

        Returns
        -------
        np.ndarray : 2D array containing wind speed intervals in m/s in the
                     first y-axis position and target field values in the
                     second.
        """
        df = self.table(index, group)[["wind_speed_ms", field]]
        curve = df.iloc[:, :2].values
        curve = self._interpolate(curve, interval)
        return curve

    def plot(self, index, group="onshore", field="power_kw",
             interval=0.25):
        """Plot an interpolated power curve for a specific turbine.
        
        Parameters
        ----------
        index : int
            Index position of turbine in table for given group.
        group : str
            Group name in which target turbine is contained.
        field : str
            Target field in turbine table (power_kw, cp, etc.).
        interval : int | float
            Windspeed interval in which to return target field values.
        """
        name = self.turbines(group)[index]
        curve = self.curve(index, group, field, interval)
        fig, ax = plt.subplots(1, 1)
        ax.plot(curve[:, 0], curve[:, 1])
        fig.suptitle(name)
        ax.set_ylabel(field)
        ax.set_xlabel("windspeed_ms")

    @property
    def groups(self):
        """Return list of turbine groups."""
        return list(self.paths.keys())

    @property
    def nturbines(self):
        """Return count of all available turbines."""
        n = 0
        for group in self.groups:
            n += len(self.turbines(group))
        return n

    @property
    def paths(self):
        """Return posix path object for package data."""
        contents = importlib_resources.files(turbine_models.__name__)
        data = [file for file in contents.iterdir() if file.name == "data"][0]
        paths = {folder.name.lower(): folder for folder in data.iterdir() if os.path.isdir(str(folder))}
        return paths

    @property
    def spec_paths(self):
        """Return posix path object for package specs."""
        contents = importlib_resources.files(turbine_models.__name__)
        data = [file for file in contents.iterdir() if file.name == "specs"][0]
        paths = {folder.name.lower(): folder for folder in data.iterdir() if os.path.isdir(str(folder))}
        return paths

    def table(self, index, group="onshore"):
        """Get a specific turbine power table.

        Parameters
        ----------
        index : int or str
            int: The integer associated with a a turbine model in the given group.
            str: The turbine model name in the given group.
        group : str
            The turbine group associated with the desired turbine model.

        Returns
        -------
        pd.DataFrame : Data frame containing all available turbines
                                  within a group.
        """
        if isinstance(index,int):
            fpath = self._turbines(group)[index]["path"]
        elif isinstance(index,str):
            indx_turb_dict = self.turbines(group=group)
            turb_idx_dict = {v:k for k,v in indx_turb_dict.items()}
            indx = turb_idx_dict[index]
            fpath = self._turbines(group)[indx]["path"]
        df = pd.read_csv(fpath)
        df = self._rename_cols(df)
        return df

    def specs(self, index, group="onshore"):
        if isinstance(index,int):
            fpath = self._turbines(group)[index]["spec_path"]
        elif isinstance(index,str):
            group = self.find_group_for_turbine(index)
            indx_turb_dict = self.turbines(group=group)
            turb_idx_dict = {v:k for k,v in indx_turb_dict.items()}
            if index in turb_idx_dict.keys():
                index = turb_idx_dict[index]
            else:
                index = None
        if index is not None:
            if "spec_path" in self._turbines(group)[index]:
                fpath = self._turbines(group)[index]["spec_path"]
                with open(fpath) as fid:
                    spec_data = yaml.load(fid, yaml.SafeLoader)
                power_table = self.table(index,group=group)
                spec_data.update({"power_curve":power_table})
            else:
                spec_data = self.table(index,group=group)
        else:
            spec_data = None
        return spec_data

    def find_close_matching_names(self,name,name_options):
        n_matches = {}
        name_parts = name.split("_")
        for part in name_parts:
            option_has_part = [k for k in name_options if part.lower() in k.lower()]
            new_matches = {opt:1 for opt in option_has_part if opt not in list(n_matches.keys())}
            more_matches = {k:v+1 for k,v in n_matches.items() if k in option_has_part}
            n_matches.update(new_matches)
            n_matches.update(more_matches)
        return n_matches
    
    def filter_matches(self,group_close_matches):
        top_matches = {}
        for possible_group in group_close_matches.keys():
            n_part_match_per_turb = [int(v) for v in group_close_matches[possible_group].values()]
            if max(n_part_match_per_turb)>1:
                vals,cnts = np.unique(n_part_match_per_turb,return_counts = True)
                max_similarity_turbs = [turb for turb,n in group_close_matches[possible_group].items() if n==int(vals[-1])]
                top_matches.update({possible_group:max_similarity_turbs})
        return top_matches

            


    def find_group_for_turbine(self,turbine_name,verbose = True):
        
        group_of_turb = None
        for group in self.groups:
            turbines_in_group = self.turbines(group)
            if any(k.lower()==turbine_name.lower() for k in list(turbines_in_group.values())):
                group_of_turb = group
                break

        if group_of_turb is None:
            group_close_matches = {}
            for group in self.groups:
                turbines_in_group = self.turbines(group)
                matches = self.find_close_matching_names(turbine_name,list(turbines_in_group.values()))
                
                if len(matches)>0:
                    group_close_matches.update({group:matches})
            if len(group_close_matches)>0:
                # print("Could not find exact turbine name, returning dictionary of possible matches")
                top_matches = self.filter_matches(group_close_matches)
                if len(top_matches)>0:
                    if verbose:
                        # warn = f"Could not find exact match for `{turbine_name}`. Did you mean: \n"
                        
                        print(f"Could not find exact match for `{turbine_name}`. Did you mean: \n")
                        for top_group in top_matches.keys():
                            print(f"\t {top_group} turbines:")
                            turbs = top_matches[top_group]
                            print_turbs = "\t \t - "
                            print_turbs += "\n \t \t - ".join(turbs)
                            print(print_turbs)
                            # warn += f"\t {top_group} turbines:"
                            # warn += print_turbs
                        
                    return top_matches
                else:
                    return group_close_matches
            else:
                raise ValueError(
                    f"Cannot find turbine in library that closely matches {turbine_name} \n"
                    "to see a list of turbines in a group, for example try: `Turbines.turbines(group='onshore')`"
                )
        else:
            return group_of_turb


    def turbines(self, group="onshore"):
        """Return dictionary of available turbines.
        
        Parameters
        ----------
        group : str
            Name of turbine group to list. Available groups found in
            Turbine.groups propery.

        Returns
        -------
        dict: Dictionary containing index positions as keys and turbine model
              names as values.
        """
        full_turbines = self._turbines(group)
        turbines = {key: value["name"] for key, value in full_turbines.items()}
        return turbines

    def _interpolate(self, curve, interval):
        # Interpolate curves to have equal intervals.
        ws = np.arange(
            0,
            interval * round(max(curve[:, 0]) / interval),
            interval
        )
        p = np.interp(ws, curve[:, 0], curve[:, 1])
        p[p < 0] = 0

        # Add in 0 to min windspeed
        if ws[0] != 0:
            zws = np.arange(0, min(ws), interval)
            zp = np.zeros(zws.shape[0])
            ws = np.concatenate((zws, ws))
            p = np.concatenate((zp, p))

        # Combine into 2d array
        ws = ws.reshape((-1, 1))
        p = p.reshape((-1, 1))
        curve = np.hstack([ws, p])

        return curve

    def _rename_cols(self, df):
        # Rename columns for easier typing
        columns = []
        keepers = []
        for column in df.columns:
            column = column.lower().replace("-", " ")
            for symbol in ["[", "]", "/"]:
                column = column.lower().replace(symbol, "")
            column = column.strip()
            column = column.lower().replace(" ", "_")
            columns.append(column)
            if "unnamed" not in column:
                keepers.append(column)
        df.columns = columns
        df = df[keepers]
        return df

    def _turbines(self, group="onshore",file_ext=".csv"):
        # Return dictionary containing turbine name and posix paths
        turbines = {}
        spec_paths = [file for file in self.spec_paths[group].iterdir()]
        spec_names = [file.name for file in self.spec_paths[group].iterdir()]
        for i, path in enumerate(self.paths[group].iterdir()):
            if file_ext in path.name:
                name = os.path.splitext(path.name)[0]
                turbines[i] = {}
                turbines[i]["name"] = name
                turbines[i]["path"] = path
                if any(name in k for k in spec_names):
                    turbines[i]["spec_path"] = [k for k in spec_paths if name in k.name][0]
        return turbines
