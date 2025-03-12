# NREL Wind Turbine Power Curve Archive
## Welcome to the repository for the wind turbine power curve archive.

The intention of this repositiory is to provide power curves and key data for commonly used turbine models in industry the R&D community. 

    
## Structure
Tabular power (and thrust when available) curve data is stored in the following folders:
- Distributed Wind Turbines
- Offshore Wind Turbines
- Onshore Wind Turbines

Here you can find .csv files with the following turbine data:
1. Power curve
2. Thrust curve (when available)
3. Cp curve (when available)
4. Ct curve (when available)

## Documentation
Each turbine included in the repository is documented in detail:
https://nrel.github.io/turbine-models/

The name of the turbine on the .csv file with tabular data should match up with a corresponding documentation page.

## Installing from Source
1. Using Git, navigate to a local target directory and clone repository:

    ```bash
    git clone https://github.com/NREL/turbine-models.git
    ```

2. Navigate to `turbine-models`

    ```bash
    cd turbine-models
    ```

3. Create a new virtual environment and change to it. Using Conda and naming it `turb_lib`:

    ```bash
    conda create --name turb_lib python=3.11 -y
    conda activate turb_lib
    ```

4. Install turbine-models and its dependencies:
    - for general use:

        ```bash
        pip install .
        ```

    - for general use and running examples:

        ```bash
        pip install ".[examples]"
        ```
    
    - for development dependencies and running tests. Note the `-e` flag which installs turbine-models in-place so you can edit the turbine-models package files: 
        
        ```bash
        pip install -e ".[develop]"
        ```


## Getting started
The [Examples](./examples/) contain Python scripts for common usage scenarios.
