WTK_Validation_IEC-1_normalized
===============================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Onshore/WTK_Validation_IEC-1_normalized.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | WTK Validation IEC I    | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            |                         | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 17                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         |                         | m              |
+------------------------+-------------------------+----------------+
| Hub Height             |                         | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             |                         | N/A            |
+------------------------+-------------------------+----------------+
| Control                |                         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | I                       | N/A            |
+------------------------+-------------------------+----------------+

Normalized IEC Class 1 power curve comes from a report validating power output for the WIND Toolkit [#king2014]_. The report presents normalized power curves, but assumes 2MW turbine ratings and 100m hub heights for modeling in the report. Cp values are not available since rotor diameters are not included.

===========
Power curve
===========

.. image:: \\images\\WTK_Validation_IEC-1_normalized_Power.png
  :width: 800

==========
References
==========

.. [#king2014]  King, J., A. Clifton, and B.-M. Hodge. 2014.
     *Validation of Power Output for the WIND Toolkit*. Golden, CO: National Renewable Energy Laboratory.
     NREL/TP-5D00-61714. https://www.nrel.gov/docs/fy14osti/61714.pdf.
