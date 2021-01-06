CF11(PhaseA)_11kW_11.15
=======================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Distributed/CF11(PhaseA)_11kW_11.15.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | CF11 (Phase A)          | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 11                      | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 9                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3.5                     | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 11.15                   | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 15.65                   | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Variable Speed          | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Pitch Regulated         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+

Note that this machine is the same as the CF12, but has an inverter which caps maximum power at 11 kW. This likely explains why the rated wind speed 9 m/s instead of 11 m/s (wind speed at which AWEA defines the rated power for small wind turbines).

===========
Power curve
===========

.. image:: C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\docs\\source\\images\\CF11(PhaseA)_11kW_11.15_Power.png
  :width: 800

========
Cp curve
========

.. image:: C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\docs\\source\\images\\CF11(PhaseA)_11kW_11.15_Cp.png
  :width: 800

=======
Sources
=======

Intertek power performance test:
https://www.intertek.com/uploadedFiles/Intertek/Divisions/Commercial_and_Electrical/Media/PDF/Energy/Wind/101510200LHD-001a_BWEA%20Summary%20Report_CF11%20(phase%20A).pdf

See also: 
https://www.intertek.com/wind/directory/CF11/ 
https://www.intertek.com/wind/directory/
https://www.intertek.com/wind/small/RTC/