2020ATB_NREL_Reference_12MW_214
===============================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Offshore/2020ATB_NREL_Reference_12MW_214.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | 2020 ATB Reference 12   | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 12000                   | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 4                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 214                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 136                     | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             |                         | N/A            |
+------------------------+-------------------------+----------------+
| Control                |                         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+

This turbine model was used for analysis in the 2020 NREL ATB [#atb2020]_ . It was scaled with a constant specific power 
assumption from an earlier version of the `IEA_15MW_240_RWT <https://nrel.github.io/turbine-models/IEA_15MW_240_RWT.html>`_.

===========
Power curve
===========

.. image:: \\images\\2020ATB_NREL_Reference_12MW_214_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\2020ATB_NREL_Reference_12MW_214_Cp.png
  :width: 800

==========
References
==========

.. [#atb2020]  NREL (National Renewable Energy Laboratory). 2020. 
    "2020 Annual Technology Baseline: Offshore Wind." Golden, CO: National Renewable Energy Laboratory. https://atb.nrel.gov/electricity/2020/index.php?t=ow. Accessed January 23, 2021.
