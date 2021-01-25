EntegrityEW50_50kW_15
=====================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Distributed/EntegrityEW50_50kW_15.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | Entegrity EW50          | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 50                      | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11.3                    | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 4                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 14.9                    | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 31.1                    | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Variable Speed          | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Stall Regulated         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+

The performance data comes from a power performance test conducted by NREL  [#smith2011]_.

Note turbine does not hit the reported 50 kW rated power at the rated wind speed in the performance test. See note in reference about blades being pitched to accommmodate air density at test site.

===========
Power curve
===========

.. image:: \\images\\EntegrityEW50_50kW_15_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\EntegrityEW50_50kW_15_Cp.png
  :width: 800

==========
References
==========

.. [#smith2011]  Smith, J., A. Huskey, D. Jager, and J. Hur. 2011.
    *Wind Turbine Generator System Power Performance Test Report for the Entegrity EW50 Wind Turbine*. Golden, CO: National Renewable Energy Laboratory. 
    NREL/TP-5000-51392. https://www.nrel.gov/docs/fy11osti/51392.pdf.
