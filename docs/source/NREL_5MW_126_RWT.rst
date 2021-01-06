NREL_5MW_126_RWT
================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Offshore/NREL_5MW_126_RWT.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | NREL 5 MW RWT           | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 5000                    | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11.4                    | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 126                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 90                      | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Geared                  | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Pitch Regulated         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+

Note: (from Forum) RotThrust is axial force including some contribution from the rotor weight (not purely the aerodynamic thrust). Also, the included curves are the generator power and generator Cp. Aerodynamic power and Cp are available at the source.

===========
Power curve
===========

.. image:: C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\docs\\source\\images\\NREL_5MW_126_RWT_Power.png
  :width: 800

========
Cp curve
========

.. image:: C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\docs\\source\\images\\NREL_5MW_126_RWT_Cp.png
  :width: 800

=======
Sources
=======

NREL 5 MW Reference Report:
https://www.nrel.gov/docs/fy09osti/38060.pdf

Forum:
https://wind.nrel.gov/forum/wind/viewtopic.php?t=363#p1117