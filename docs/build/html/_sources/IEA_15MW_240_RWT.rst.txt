IEA_15MW_240_RWT
================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Offshore/IEA_15MW_240_RWT.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | IEA 15 MW RWT           | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 15000                   | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 10.6                    | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 240                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 150                     | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Direct Drive            | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Pitch Regulation        | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | 1B                      | N/A            |
+------------------------+-------------------------+----------------+

This turbine model originates from IEA Task 37. A Technical Report is available [#gaertner2020]_ , and other data may be found in a GitHub repository for the project [#ieagh]_. 

Note: The power curve data included is taken from the project's GitHub page, which is more recent than the curve in the original report.

===========
Power curve
===========

.. image:: \\images\\IEA_15MW_240_RWT_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\IEA_15MW_240_RWT_Cp.png
  :width: 800

==========
References
==========

.. [#gaertner2020]  Gaertner, Evan, Jennifer Rinker, Latha Sethuraman, Frederik Zahle, Benjamin Anderson, Garrett Barter, Nikhar Abbas, Fanzhong Meng, Pietro Bortolotti, Witold Skrzypinski, George Scott, Roland Feil,  Henrik Bredmose, Katherine Dykes, Matt Shields, Christopher Allen, and Anthony Viselli. 2020. *Definition of the IEA 15-Megawatt Offshore Reference Wind Turbine*. International Energy Agency. NREL/TP-5000-75698. https://www.nrel.gov/docs/fy20osti/75698.pdf

.. [#ieagh] IEA Wind Task 37. 2020.
    "GitHub - IEA Wind Task 37/IEA-15-240-RWT." International Energy Agency.
    https://github.com/IEAWindTask37/IEA-15-240-RWT.
    Accessed January 23, 2021.
