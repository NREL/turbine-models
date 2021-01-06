WTK_Validation_IEC-3_normalized
===============================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Onshore/WTK_Validation_IEC-3_normalized.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | WTK Validation IEC III  | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            |                         | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 12                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 22                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         |                         | m              |
+------------------------+-------------------------+----------------+
| Hub Height             |                         | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             |                         | N/A            |
+------------------------+-------------------------+----------------+
| Control                |                         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | III                     | N/A            |
+------------------------+-------------------------+----------------+

Note: The reference presents normalized power curves, but assumes 2MW turbine ratings and 100m hub heights for modeling in the report.

===========
Power curve
===========

.. image:: C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\docs\\source\\images\\WTK_Validation_IEC-3_normalized_Power.png
  :width: 800

=======
Sources
=======

Normalized IEC Class 3 power curve from NREL report: "Validation of Power Output for the WIND Toolkit." Note Cp values are not available since rotor diameters are not included.
https://www.nrel.gov/docs/fy14osti/61714.pdf