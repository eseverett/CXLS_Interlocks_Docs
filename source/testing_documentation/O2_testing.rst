.. role:: yellow
.. role:: orange
.. role:: blue

O2 Sensor Testing Protocol
==========================

The purpose of this document is to test the functionality of the O2 sensors in Vault-1, Hutch-1, and RF-1. 


Staring Conditions
------------------

#. O2 main and remote units only show LED for POWER.

    - Vault-1 main unit
    - Vault-1 Control remote unit
    - RF-1 main unit
    - Accelerator Lab remote unit
    - Hutch-1 main unit
    - Hutch-1 Control remote unit (top)
    - Astrella enclosure main unit
    - Hutch-1 Control remote unit (bottom)

#. Vault-1 Control IONIZING RADIATION INTERLOCK protocase AREA MONITOR OXYGEN lamp is :green:`green`.

#. Relay contact #9 in Vault-1 Control west aggregator panel has LEDs on.

#. Yellow 4 contact blocks in Vault-1 Control west aggregator panel all have continuity with each other. 

.. warning::
    NEED IMAGES


Testing Connectivity Between Main and Remote Units
--------------------------------------------------

#. On the face of the main unit and remote unit, press mode until DIAG flashes on the display. Press enter, in return:

    - All LEDs on the units will light.
    - The units will alarm.

        - Vault-1 / Vault-1 Control
        - RF-1 / Accelerator Lab
        - Hutch-1 / Hutch-1 Control (top)
        - Astrella enclosure / Hutch-1 Control (bottom)

    
Testing Alarming
----------------

#. Using compressed gas, spray the gas into the main controller sensor until the unit sees an :math:`O_2` concentration of less than 19%.

    - The main and remote units will audibly alarm.
    - The ELDs for AL1 to flash. More AL# LEDs may flash depending on if you break the 17% and or 15% thresholds. 
      However, the AL1 relay is what is critical.
    - The Vault-1 Control IONIZING RADIATION INTERLOCK protocase AREA MONITOR OXYGEN lamp will turn :red:`red`.
    - Relay contract #9 in the Vault-1 Control west aggregator panel LEDs will turn off.
    - The correct :yellow:`yellow 4`` contact blocks will lose continuity with each other.
    - Corresponding :orange:`orange` beacon to the unit being tested will flash.
    - These units have latching alarms.
      Press the bottom left recessed button to rest the alarm. 

        - Vault-1 / Vault-1 Control
        - RF-1 / Accelerator Lab
        - Hutch-1 / Hutch-1 Control (top)
        - Astrella enclosure / Hutch-1 Control (bottom)


Emergency Tungsten Shutter Crash
--------------------------------

#. Secure Hutch-1.

#. Open a tungsten shutter and make sure it is physically open. 

#. Spray compressed gas into a O2 unit. In response:

    - The yellow and blue contact block for the tungsten shutters in Hutch-1 panel do nat have 24VDC across them.
    - Hutch-1 Control IONIZING RADIATION INTERLOCK protcase lamps for BEAM STATUS turn :red:`red`.


.. warning::
    NEED IMAGES