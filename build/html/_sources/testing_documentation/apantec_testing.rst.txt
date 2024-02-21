.. roles are for allowing custom css classes to work.
.. role:: yellow
.. role:: orange
.. role:: white-cell

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

.. note::
    Check calibration sheet in Accelerator Lab.

.. warning:: 
    Make calibration sheet and find a place to post it. 

#. The Ionizing Radiation Interlock protocase AREA MONITOR RADIATION lamps are :green:`green`.

    - Vault-1 Control
    - Hutch-1 Control

#. The :yellow:`yellow` and white contact blocks in the Vault-1 Control west aggregator panel for the radiation chain should have 24VDC across them.

#. Hutch-1 is in a non-secure state.

#. Relays in the Vault-1 Control west aggregator panel shows all diagnostic LEDs on.

    - R4
    - R6
    - R7
    - 8

#. Relays in the Vault-1 Control west aggregator panel show no power. 

    - R3
    - R5


.. figure:: /images/testing_documentation/apantec/Apantec_normal.jpg
    :align: center
    :scale: 20 %

    **Figure 1:** This is an example of the RMW1 rate meter control in a normal operating state. 

.. figure:: /images/testing_documentation/apantec/yellow_white_contacts.jpg
    :align: center
    :scale: 20 %

    **Figure 2:** These are the yellow and white contact blocks in the Vault-1 Control west panel.


Testing Alert alarm
-------------------

#. Using either the radiation monitoring program of using the Apantec physical interface, change the alarm set points to 0.
   In response:

    - The rate meter that controls the probe has the :orange:`ALERT` LED on.
    - The Ionizing Radiation Interlock protocase AREA MONITOR RADIATION lamp turns :red:`red`.
    - The yellow and white contact blocks lose 24VDC across them.   
    - Manually change the alert set point back to 50. 

.. list-table::
    :align: center 
    :header-rows: 1

    * - **Gamma:**
      - **Neutron:**
    * - Hutch-1 Front
      - Hutch-1 Front
    * - Hutch-1 Black
      - Hutch-1 Black
    * - Vault-1 Control
      - Vault-1 Control
    * - Laser-1
      - N/A
    * - RF-1
      - N/A

.. figure:: /images/testing_documentation/apantec/Apantec_alert.jpg
    :align: center
    :scale: 20 %

    **Figure 3:** This is an example of the RMW1 rate meter control in an alert state.

.. figure:: /images/testing_documentation/apantec/Hutch-1_Control_protocase_radiation_fail.jpg
    :align: center
    :scale: 20 %

    **Figure 4:** This is an example of the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase AREA MONITOR RADIATION lamp in a fail state.
    This should occur on the Vault-1 Control IONIZING RADIATION INTERLOCK protocase AREA MONITOR RADIATION lamp as well.


Testing High Alarm
------------------

#. Secure Hutch-1. 
   In Vault-1 Control west panel, relays R3 and R5 should have power, and relay R4 should have no power.

#. Change the alert alarm settings on any of the Hutch1 probes to zero.
   Nothing should happen, change the value back. 

#. Using the same methods as with the alert alarm setting, change the high alarm setting to zero on each probe one at a time. 
   In response:

    - The rate meter that controls the probe has the :red:`HIGH ALARM` LED on.
    - The rate meter that control the probe has an audible alarm.
    - The IONIZING RADIATION INTERLOCK protocase AREA MONITOR RADIATION lamps turn :red:`red`.
    - The yellow and white contact blocks lose 24VDC across them.
    - Manually change the set point back to 500.
    - Relay 16 in Hutch-1 panel loses power. 


.. list-table::
    :align: center
    :header-rows: 1

    * - **Gamma:**
      - **Neutron:**
    * - Hutch-1 Front
      - Hutch-1 Front
    * - Hutch-1 Black
      - Hutch-1 Black


.. figure:: /images/testing_documentation/apantec/Apantec_alarm.jpg
    :align: center
    :scale: 20 %

    **Figure 5:** This is an example of the RMW1 rate meter control in an alarm state.


.. TESTING FAIL ALARM 
.. ------------------

.. #. Power off the rate meter you are testing and unplug the gamma probe from their rate meters. 
..    Turn the unit back on, in response:

..     - The FAIL LED will turn on.
..     - The display will show FAIL: No Cnt GGRt1
..     - The yellow and white contact blocks lose 24 VDC.
..         - Hutch-1 Front
..         - Hutch-1 Back
..         - Laser-1
..         - RF-1
..         - Vault-1 Control

.. #. Turn off the rate meters and reconnect the probes. 
..    Once powered back on:

..     - The NORMAL LED is on.
..     - The display does not show an error.
..     - The yellow and white contact blocks have 24 VDC.

.. #. Repeat with the neutron probes. 
..    In response:

..     - The FAIL LED will turn on.
..     - The display will show FAIL: No Cnt NHRt1
..     - The yellow and white contact blocks lose 24 VDC.

.. #. Turn off the rate meters and reconnect the probes. 
..    Once powered back on:

..     - The NORMAL LED is on.
..     - The display does not show an error.
..     - The yellow and white contact blocks have 24 VDC.

.. .. warning
..     NEEDS IMAGES


Emergency Tungsten Shutter Crash
--------------------------------

#. Secure Hutch-1. 
   
#. Set the BEAM SELECT to COLLIMATED.

#. Change the Apantec gamma probe high alarm set point to 0 in Hutch-1. 
   In response:

    - Hutch-1 Control Ionizing Radiation Interlock protocase lamps for Beam Status turn :red:`red`. 
    - The COLLIMATED shutter (furthest, right side up shutter) closed. 