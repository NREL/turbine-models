IEA_10MW_198_RWT
================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Offshore/IEA_10MW_198_RWT.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | IEA 10 MW RWT           | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 10000                   | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 4                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 198                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 119                     | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Direct Drive            | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Pitch Regulation        | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | IA                      | N/A            |
+------------------------+-------------------------+----------------+

This turbine model originates from IEA Task 37. A Technical Report is available [#bortolotti2019]_ , and other data may be found in a GitHub repository for the project [#ieagh]_. 

Note the IEA 10 MW Reference represents an update to DTU 10 MW Reference Wind Turbine.

===========
Power curve
===========

.. image:: \\images\\IEA_10MW_198_RWT_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\IEA_10MW_198_RWT_Cp.png
  :width: 800

==========
References
==========

.. [#bortolotti2019] Bortolotti, Pietro, Helene Canet Tarres, Katherine Dykes, Karl Merz, Latha Sethuraman, David Verelst, and Frederik Zahle. 2019. 
    *IEA Wind Task 37 on Systems Engineering in Wind Energy -- WP2.1 Reference Wind Turbines*. International Energy Agency. NREL/TP-73492. https://www.nrel.gov/docs/fy19osti/73492.pdf.

.. [#ieagh] IEA Wind Task 37. 2020.
    "GitHub - IEA Wind Task 37/IEA-10.0-198-RWT." International Energy Agency.
    https://github.com/IEAWindTask37/IEA-10.0-198-RWT.
    Accessed January 23, 2021.
