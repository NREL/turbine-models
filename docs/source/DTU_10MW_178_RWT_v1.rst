DTU_10MW_178_RWT_v1
===================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Offshore/DTU_10MW_178_RWT_v1.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | DTU 10 MW RWT (v1)      | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 10000 (see note)        | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 11.4                    | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 4                       | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 25                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 178.3                   | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | 119                     | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Geared                  | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Pitch Regulated         | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | IA                      | N/A            |
+------------------------+-------------------------+----------------+

The model included here is the first version (v1) of the 10 MW Reference Wind Turbine developed by the Technical University of Denmark (DTU). Details are available in a DTU Technical Report and conference slides: [#bak2013]_ and [#bak13conf]_ . HAWC2 model files are also available from DTU Wind Energy [#hawc]_.

Note: despite the fact that the rated power is 10 MW, the turbine produces 10.6 MW according to the power curve from the source. Since this turbine model was released, IEA Wind Task 37 has produced an updated 10 MW reference turbine model: https://github.com/IEAWindTask37/IEA-10.0-198-RWT

===========
Power curve
===========

.. image:: \\images\\DTU_10MW_178_RWT_v1_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\DTU_10MW_178_RWT_v1_Cp.png
  :width: 800

==========
References
==========

.. [#bak2013]  Bak, Christian, Frederik Zahle, Robert Bitsche, Taeseong Kim Anders Yde, Lars Christian Henriksen, Anand Natarajan, and Morten Hartvig Hansen. 2013.
    *Description of the DTU 10 MW Reference Wind Turbine*. Roskilde, DK: DTU Wind Energy. DTU Wind Energy Report-I-0092.

.. [#bak13conf]  Bak, Christian, Frederik Zahle, Robert Bitsche, Taeseong Kim Anders Yde, Lars Christian Henriksen, Morten Hartvig Hansen, José Pedro Albergaria Amaral
    Blasques, Mac Gaunaa, and Anand Natarajan. 2013 (May 27 - May 28). *The DTU 10-MW Reference Wind Turbine* (Conference Presentation). Danish Wind Power Research 2013, Fredericia, Denmark. https://orbit.dtu.dk/en/publications/the-dtu-10-mw-reference-wind-turbine.

.. [#hawc]  DTU Wind Energy. 2017. 
    "HAWC2 Model for the DTU 10-MW Reference Wind Turbine." Roskilde, DK: DTU Wind Energy. https://www.hawc2.dk/Download/HAWC2-Model/DTU-10-MW-Reference-Wind-Turbine. Accessed January 23, 2021.
