.. wt-archive-test documentation master file, created by
   sphinx-quickstart on Tue Sep  8 09:58:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NREL Turbine Archive
===========================================
Welcome to the documentation for NREL's wind turbine archive!

The purpose of this archive is to compile public wind turbine data in one place for easy access.
There is a focus on providing tabular power (and when available thrust) curve data in an accessible (.csv)
format along with documentation. 

**Disclaimer**: *This archive is in no means an endorsement of specific turbine
models or individual companies.*

The documentation is broken into three categories:

* Distributed Wind Turbines
* Offshore Wind Turbines
* Onshore Wind Turbines

=====
Notes
=====

The naming convention for each turbine is source or manufacturer + model + _rated power + _rotor diameter.

RWT is an abbreviation of Reference Wind Turbine.

Air density is assumed to be 1.225 kg/ m^3, unless otherwise specified in power performance testing documentation.

The tabular data is available on GitHub: https://github.com/NREL/turbine-models

Not all turbine models or power curves are developed with the same level of rigor. 

For onshore and offshore modeling work the following models have the most detailed (and accessible) documentation:

* IEA_3.4MW_130_RWT
* IEA_10MW_198_RWT
* IEA_15MW_240_RWT
* NREL_5MW_126_RWT

In practice power curves may deviate from idealized reference model curves for a number of reasons. The Normalized Industry Composite machines have power curves that reflect modern control strategies around the cut-out wind speed. Several of the curves documented in this repository are based on measurements via power performance testing. 

If you have feedback or want to contribute please contact Patrick Duffy:
patrick.duffy@nrel.gov

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Distributed
   Offshore
   Onshore
