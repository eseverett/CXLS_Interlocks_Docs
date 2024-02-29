.. these roles are defined to use custom css classes

VIEWMARQ Marquee Display Interlock Error Troubleshooting Guide
==============================================================

The VIEWMARQ Marquee displays show the status of the room the display oversees.
It knows the status of the room by receiving an 8-bit signal from the possible hazards, where each hazard corresponds to one of the 8 channels. 


.. list-table:: Vault-1 Control VIEWMARQ Display Bit Channels
    :align: center 
    :header-rows: 1

    * - Bit Channel
      - Status
    * - 1
      - Ionizing Radiation E-stop Active
    * - 2
      - RF Armed 
    * - 3
      - Pharos Admin Override 
    * - 4
      - Dira Admin Override  
    * - 5
      - Laser Safety
    * - 6
      - Pharos Armed 
    * - 7
      - Dira Armed 
    * - 8
      - Unused Bit Channel

.. list-table:: Hutch-1 Control VIEWMARQ Display Bit Channels
    :align: center
    :header-rows: 1

    * - Bit Channel
      - Status
    * - 1
      - Unused Bit Channel
    * - 2   
      - Unused Bit Channel
    * - 3
      - Unused Bit Channel
    * - 4
      - Astrella Admin Override 
    * - 5
      - Unused Bit Channel
    * - 6
      - Laser Safety
    * - 7
      - Unused Bit Channel
    * - 8
      - Astrella Armed

    
.. list-table:: Accelerator Lab VIEWMARQ Display Bit Channels
    :align: center
    :header-rows: 1

    * - Bit Channel
      - Status
    * - 1
      - Ionizing Radiation E-stop Active
    * - 2
      - RF Armed
    * - 3
      - Unused Bit Channel
    * - 4
      - Unused Bit Channel
    * - 5
      - Unused Bit Channel
    * - 6
      - Unused Bit Channel
    * - 7
      - Unused Bit Channel
    * - 8
      - Unused Bit Channel



Resolved Issues
---------------

#. The a VIEWMARQ displays shows :red:`Interlock System Error: xxxxxxxx`, where the xxxxxxxx is an 8-bit binary number, if there is a state that should not exist. 
   The error was that the specific 8-bit combination was not programmed into the VIEWMARQ display.
   All 255 possible combinations of the 8-bit signal must be programmed individually, therefore is a combination was not considered or overlooked, a false error will occur. 

#. The VIEWMARQ display either shows the wrong status or an error status.
   This error was caused by incorrect wiring in the interlock system aggregator panel between the relays. 
   This could also be caused by a faulty relay, bad power supply, or other downstream issues.