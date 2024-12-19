# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="turbine_models",
    version="0.0.1",
    packages=["turbine_models"],
    description=("Retrieves power curves and key data for commonly used "
                 "turbine models in industry the R&D community."),
    author="Patrick Duffy & Travis Williams",
    author_email="patrick.duffy@nrel.gov",
    install_requires=["numpy", "pandas","matplotlib"],
    include_package_data=True,
    pacakage_data={
        "data": [
            "Offshore/*csv",
            "Onshore/*csv",
            "Distributed/*csv"
        ]
    }
)
