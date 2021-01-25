BAR_BAU-LBNL-IEA_3.3MW_156
==========================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Onshore/BAR_BAU-LBNL-IEA_3.3MW_156.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | BAR LBNL-IEA 3.3 MW     | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 3300                    | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 9                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 4                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 156                     | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 111                     | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             |                         | N/A            |
+------------------------+-------------------------+----------------+
| Control                |                         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              |                         | N/A            |
+------------------------+-------------------------+----------------+


This turbine model originates from NREL's Big Adaptive Rotor project [#johnson2019]_ and was also 
used as the 'business as usual (BAU)' turbine in a NREL Technical Report investigating the impact of tall towers [#lantz2019].

===========
Power curve
===========

.. image:: \\images\\BAR_BAU-LBNL-IEA_3.3MW_156_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\BAR_BAU-LBNL-IEA_3.3MW_156_Cp.png
  :width: 800

==========
References
==========

.. [#johnson2019]  Johnson, Nick, Pietro Bortolotti, Katherine Dykes, Garrett Barter, Patrick Moriarty, Scott Carron, Fabian Wendt, Paul Veers, Josh Paquette, Chris 
    Kelly, and Brandon Ennis. 2019. *Investigation of Innovative Rotor Concepts for the Big Adaptive Rotor Project*. Golden, CO: National Renewable Energy Laboratory. NREL/TP-5000-73605. https://www.nrel.gov/docs/fy19osti/73605.pdf.


.. [#lantz2019]  Lantz, Eric, Owen Roberts, Jake Nunemaker, Edgar DeMeo, Katherine Dykes, and George Scott. 
    2019. *Increasing Wind Turbine Tower Heights: Opportunities and Challenges*. Golden, CO: National Renewable Energy Laboratory. 
    NREL/TP-5000-73629. https://www.nrel.gov/docs/fy19osti/73629.pdf.
