.. roles are for allowing custom css classes to work.
.. role:: yellow

Apantec Ionizing Radiation Sensors Testing Protocol
===================================================

The objective of this testing procedure is to test the functionality of the Apantec ionizing radiation detection equipment and interlocks. 

Starting Conditions
-------------------

#. All rate meters are in normal operating condition. 

    - Only the :green:`NORMAL` condition LED is on. :red:`ALARM`, :yellow:`ALERT`, and FAIL LEDs are off.
    - There is no audible alarm from the rate meter.
    - The displays on the rate meters do not display any error messages.
    - All probes are calibrated. 

        - Hutch-1 Front 
        - Hutch-1 Black
        - Laser-1
        - RF-1
        - Vault-1 Control

#. The Ionizing Radiation Interlock protcase Area Monitor Radiation lamps are :green:`green`.

    - Vault-1 Control
    - Hutch-1 Control

#. The yellow and white contact blocks in the Vault-1 Control west aggregator panel for the radiation chain should have 24VDC across them.

#. Hutch-1 is in a non-secure state.

#. Relays in the Vault-1 Control west aggregator panel shows all diagnostic LEDs on.

    - R4
    - R6
    - R7
    - 8

#. Relays in the Vault-1 Control west aggregator panel show no power. 

    - R3
    - R5