# -*- coding: utf-8 -*-
"""Functions for listing and accessing turbine-model data.

Created on Wed Apr 21 14:12:17 2021

@author: twillia2
"""
import pkg_resources
import os
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

import numpy as np
import pandas as pd
import turbine_models


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
        paths = {folder.name.lower(): folder for folder in data.iterdir()}
        return paths

    def table(self, index, group="onshore"):
        """Get a specific turbine power  table.

        Parameters
        ----------
        index : int
            The integer associated with a a turbine model in the given group.
        group : str
            The turbine group associated with the desired turbine model.

        Returns
        -------
        pd.frame.core.DataFrame : Data frame containing all available turbines
                                  within a group.
        """
        fpath = self._turbines(group)[index]["path"]
        df = pd.read_csv(fpath)
        df = self._rename_cols(df)
        return df

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
            round(min(curve[:,0]), 2),
            round(max(curve[:,0]), 2),
            interval
        )
        p = np.interp(ws, curve[:, 0], curve[:, 1])

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

    def _turbines(self, group="Onshore"):
        # Return dictionary containing turbine name and posix paths
        turbines = {}
        for i, path in enumerate(self.paths[group].iterdir()):
            name = os.path.splitext(path.name)[0]
            turbines[i] = {}
            turbines[i]["name"] = name
            turbines[i]["path"] = path
        return turbines
