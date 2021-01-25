VestasV82_1.65kW_82
===================

====================
Link to Tabular Data
====================

A .csv file is available on `GitHub <https://github.com/NREL/turbine-models/blob/master/Onshore/VestasV82_1.65MW_82.csv>`_.

==============
Key Parameters
==============

+------------------------+-------------------------+----------------+
| Item                   | Value                   | Units          |
+========================+=========================+================+
| Name                   | Vestas V82              | N/A            |
+------------------------+-------------------------+----------------+
| Rated Power            | 1650                    | kW             |
+------------------------+-------------------------+----------------+
| Rated Wind Speed       | 13                      | m/s            |
+------------------------+-------------------------+----------------+
| Cut-in Wind Speed      | 3.5                     | m/s            |
+------------------------+-------------------------+----------------+
| Cut-out Wind Speed     | 20                      | m/s            |
+------------------------+-------------------------+----------------+
| Rotor Diameter         | 82                      | m              |
+------------------------+-------------------------+----------------+
| Hub Height             | Varies approx 59-80m    | m              |
+------------------------+-------------------------+----------------+
| Drivetrain             | Geared                  | N/A            |
+------------------------+-------------------------+----------------+
| Control                | Active Stall            | N/A            |
+------------------------+-------------------------+----------------+
| IEC Class              | IIb                     | N/A            |
+------------------------+-------------------------+----------------+

The power curves come from the calculated power curves in a general specifications document [#vestas]_ . Further information comes from the product brochure [#bro]_.

===========
Power curve
===========

.. image:: \\images\\VestasV82_1.65MW_82_Power.png
  :width: 800

========
Cp curve
========

.. image:: \\images\\VestasV82_1.65MW_82_Cp.png
  :width: 800

==========
References
==========

.. [#Vestas]  Vestas Wind Systems A/S. No Date.
    *General Specification - V82-1.65 MW MK II*. 
    http://www.calco.state.mn.us/commerce/energyfacilities/documents/18884/General%20Specifications%20V82-1.65%20MW%20MK%20II.pdf.
    Accessed from calco.state.mn.us January 24, 2021.

.. [#bro] Vestas Wind Systems A/S. No Date.
    *V82-1.65 MW - Creating more from less*. 
    https://www.edprnorthamerica.com/wp-content/uploads/2014/04/V82.pdf.
    Accessed from edprnorthamerica.com January 24, 2021.
