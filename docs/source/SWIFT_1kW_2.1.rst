SWIFT_1kW_2.1
=============

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Distributed/SWIFT_1kW_2.1.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | SWIFT                   | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 1                       | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3.4                     | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     |                         | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 2.1                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 14.2                    | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             |                         | N/A            |
+------------------------+-------------------------+----------------+
| Regulation             | Stall Regulated         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+

The performance data comes from a power performance test conducted by NREL [#mendoza2015]_.

===========
Power curve
===========
.. image:: \\images\\SWIFT_1kW_2.1_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\SWIFT_1kW_2.1_Cp.png
  :width: 800


==========
References
==========

.. [#mendoza2015]  Ismael Mendoza and Jerry Hur. 2015.
    *Power Performance Test Report for the SWIFT Wind Turbine*. Golden, CO: National Renewable Energy Laboratory. 
    NREL/TP-5000-56499. https://www.nrel.gov/docs/fy13osti/56499.pdf.
