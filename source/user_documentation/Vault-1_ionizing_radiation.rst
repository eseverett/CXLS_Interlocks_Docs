Vault-1 Ionzing Radiation Interlock System User Manual
======================================================

Vault-1 Ionizing Radiation Hazard Indicators
--------------------------------------------

This secetion will cover the ionizing radiation hazard indicators in Vault-1 Control and Accelerator Lab. 
These indicators will correspond to hazards present in Vault-1 and RF-1.

Vault-1 Control Protocase
^^^^^^^^^^^^^^^^^^^^^^^^^

The Vault-1 Control IONIZING RADIATION INTERLOCK protocase is an interface to view if Vault-1 is secure, arm the accelerator and transmitters, and view the status of the area monitors. 
This panel is located on the east wall in Vault-1 Control next to the Vault-1 door. 
See Figure 1 for Refernce.

The SERCURE PERIMETER section of the protocase shows the status of search buttons being engaged and if the sheild door is open. 
If all the lamps are :green:`green`, then Vault-1 is in a secure state. When Vault-1 is secure the vault cannot be entered until the accelerator is put into an unarmed state.
If the shield door is opened with the accelerator and/or transmitters armed, then the interlock system will trip and put them into a safe state. 

The AREA MONITORS section of the protocase shows the status of RADIATION, OXYGEN, and MICROWAVE area monitors. 
These lamps will turn red if any of the ionizing radiation, O :sub:`2`, or microwave monitors in the CXLS suite alarms. 
If any of these monitors alarm the corresponding lamp will turn red,  and then the interlock system will trip, and the accelerator will be put into an unarmed state. 

The ACCELERATOR section of the protocase is to be able to view and chaning the arming status of the accelerator and both transmitters.
The accerlerator cannot be armed until Vault-1 is secured, and the transmitters cannot be armed until the accerlerator is armed.


.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase.jpg
    :scale: 20 %
    :align: center

    **Figure 1:** This is the Vault-1 Control Ionzing Radiation Interlock Protocase. In this state Vault-1 is not secured, the accelerator is not armed, and the transmitters are not armed. 
    As well, there are no area monitors alarming or failing.


VIEWMARQ displays
^^^^^^^^^^^^^^^^^

There are two VIEWMARQ displays that share information on Vault-1 ionizing radiation hazard status. There is one in the Accelerator Lab and one in Vault-1 Control. 
See Figure 2 and 3 for the Vault-1 Control and Accelerator Lab VIEWMARQ displays respectively.

+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| VIEWMAEQ Display Notes                                                                                                | VIEWMARQ Display Text                    |
+=======================================================================================================================+==========================================+
| The VIEWMARQ display in Vault-1 Control shows :green:`LASER SAFE`                                                     | :green:`Laser Safe` / :green:`RF Safe`   |
|                                                                                                                       |                                          |
| because this display also displays laser hazards present in Vault-1.                                                  |                                          |
|                                                                                                                       |                                          |
| The display in Accelerator Lab displays RF SAFE when neither.                                                         |                                          |
|                                                                                                                       |                                          |
| transmitter is armed.                                                                                                 |                                          |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| Both VIEWMARQ displays show :red:`VAULT SECURE - RF ARMED` once                                                       | :red:`Vault-1 Secure - RF Armed`         |
|                                                                                                                       |                                          |
| Vault-1 is searched, secured, the accelerator is armed, and either one                                                |                                          |
|                                                                                                                       |                                          |
| or both transmitters are armed. Additional laser hazards will appear                                                  |                                          |
|                                                                                                                       |                                          |
| here as well. See Vault-1 laser system manual for hazards.                                                            |                                          |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| Both VIEWMARQ displays :red:`IONIZING RADIATION E-STOP ACTIVED`                                                       | :red:`Ionizing Radiation`                |
|                                                                                                                       |                                          |
| when any ionizing radiation e-stop in the CXLS suite is pressed.                                                      | :red:`E-Stop Activated`                  |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------+


 .. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_Control_VIEWMARQ.jpg
    :scale: 20 %
    :align: center

    **Figure 2:** This is the Vault-1 Control VIEWMARQ display. In this state there are no ionizing radiation or laser hazards.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Accelerator_lab_VIEWMARQ.jpg
    :scale: 20 %
    :align: center

    **Figure 3:** This is the Accelerator Lab VIEWMARQ display. In this state there are no ionizing radiation hazards.


Beacons
^^^^^^^

There are blue, red, and orange beacons in Vault-1 Control and Accelerator Lab to the left of the VIEWMARQ displays.


.. This role was added beacuse the file was not recognizing the custom.css orange-cell class without it.
.. role:: orange-cell

.. list-table::
    :header-rows: 1

    * - Status
      - Beacon Color
    * - The blue beacon indicates that RF has been enabled into the Vault-1 structures.
      - :blue-cell:`Beacon Color`
    * - The red beacon indicated that an ionizing radiation emergency stop button had been

        pressed. This beacon is also on the Vault-1 Control protocase.
      - :red-cell:`Beacon Color`
    * - The orange beacon indicates that one of the O2 meters isreading below 19% O :sub:`2`

        levels.
      - :orange-cell:`Beacon Color`

Refernce figures 1, 2, and 3 for the location of the beacons. 
The green, orange, white, blue beacon stack in Vault-1 Control is part of the laser interlock system and is not covered here.

O2 Main and Remote Units
^^^^^^^^^^^^^^^^^^^^^^^^

Ther eare two O :sub:`2` sensors in the Vault-1 ionizing radiation interlock system. 
One is located in Vault-1 and the other is located in RF-1. 
These units will have an audible alarm and flash one of the AL# LEDs depending on the alarm setpoint it passed. 
Any O :sub:`2` reading below 19% will cause the sensors to alarm. 
Each O :sub:`2` sensor has a remote unit that only displays information from the main sensor unit.
The Vault-1 remote unit is in Vault-1 Control and the RF-1 remote unit is in the Accelerator Lab.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_O2_main.jpg
    :scale: 20 %
    :align: center

    **Figure 4:** This is the O :sub:`2` main unit located in Vault-1. Under this condition there is no alarm.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_O2_remote.jpg
    :scale: 20 %
    :align: center

    **Figure 5:** This is the O :sub:`2` remote unit located in Vault-1 Control. Under this condition there is no alarm. 


Ionizing Radiation Monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 
    The ionizing radiation monitor may go through changes in the near future.
    This section will be updated when those changes are made.

Ionizing Radiation Emergency Stop Buttons
-----------------------------------------

Throughout the CXLS suite there are ionizing radiation emergency stop buttons. 
These e-stop buttons will cut power to the transmitters, putting the accelerator in a safe state.
Once the transmitters are crashed, there will not longer be a source of ionizing radiation.
When an ionizing radiation e-stop button is pressed, the LED on the unit will turn on, all red beacons will turn on, and the VIEWMARQ displays will show :red:`IONIZING RADIATION E-STOP ACTIVATED`.
To disengage the e-stop, rotate the button clockwise.

It is important to note that only the ionizing radiation emergency stop buttons will put the accelerator into a safe state. 
There is also laser emergency stop buttons that will only cut power to their specific laser if armed and do not affect thetransmitters.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_estop_off.jpg
    :scale: 20 %
    :align: center

    **Figure 6:** This is the ionizing radiation emergency stop button when not engaged.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_estop_on.jpg
    :scale: 20 %
    :align: center

    **Figure 7:** This is the ionizing radiation emergency stop button when engaged.

Search Procedure for Securing Vault-1
-------------------------------------

To arm the accelerator and transmitters, Vault-1 must be secured. 
To secure Vault-1, it must be cleared, searched, and the Vault-1 search buttons need to be pressed in the correct sequence. 
Starting at the west end of Vault-1, while verifying the vault is empty, press the search button labeled 1, see Figure 9. 
As you continue to search and clear press 2 then 3 as you're working your way towards the vault entrance. 
Once the 3rd search button is pressed, a chime will be audible and a # timer will start amd all the SECURE PEREIMETER SEARCH lamps on the Vault-1 Control IONZING RADIATION INTERLOCK protocase will be green. 
If the seach buttons are pressed out of order, or the search takes too long, the search will need to be restarted.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault1_Search_Buttons.png
    :scale: 35 %
    :align: center

    **Figure 8:** This is a diagram of the Vault-1 search buttons. The numbers indicate the order in which they need to be pressed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
    :scale: 20 %
    :align: center

    **Figure 9:** This one of the search buttons in Vault-1 when not pressed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** This one of the search buttons in Vault-1 when pressed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_searched.jpg
    :scale: 20 %
    :align: center

    **Figure 11:** This is the Vault-1 Control Ionizng Radiation Protocase when all searched buttons have been pressed in the correct order.

Holding down the close button to the right of the protocase, see figure 12, close the shield door till up to the yellow and black stripped tape.
Do not close the door where the tap is being covered at all.  
Once the door is fully closed and actuating the door switches the SHEILD DOOR lamp on the Vault-1 Control IONIZING RAIDTION INTERLOCK protocase will be green.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_door_buttons.jpg
    :scale: 20 %
    :align: center

    **Figure 12:** These are the Vault-1 sheild door control buttons. 

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_door.jpg
    :scale: 20 %
    :align: center

    **Figure 13:** This is the Vault-1 Control Ionizng Radiation Protocase when the shield door is closed.

Arming the Accelerator and Transmitters
---------------------------------------

Unarmable States
^^^^^^^^^^^^^^^^

Besides Vault-1 not being secured, if any ofthe area monitors are alarming or failing the AREA MONITOR lamp will turn red and the accelerator will not arm. 

Arming Procedure
^^^^^^^^^^^^^^^^

Once Vault-1 is secured the accelerator can be armed. 
To arm the accelerator, turn the ACCELERATOR ENABLE key on the Vault-1 IONZING RADIATION INTERLOCK protocase. 
The STATUS lamp will turn green. Now that the accelerator is armed, the transmitters can be armed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_accelerator_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 14:** This is the Vault-1 Control Ionizng Radiation Protocase when the accelerator is armed.

Like the accelerator, to arm the individual transmitters turn the TRANMISTTER ENABLE key on the Vault-1 Control IONZING RADIATION INTERLOCK protocase. 
The STATUS lamp will turn green for the transmitter you armed. 
Once either of the transmitters are armed the VIEWMARQ displays in Vault-1 Control and Accelerator Lab will display :red:`VAULT SECURE - RF ARMED` and the blue beacons next to the display will be on.
At this state the transmitters can be set to trig and power can be enabled into the RF structures.

The accelerator and transmitters can be disarmed by pressing the ACCELERATOR RESET button on the Vault-1 Control IONZING RADIATION INTERLOCK protocase.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_transmitter_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 15:** This is the Vault-1 Control Ionizng Radiation Protocase when a transmitter is armed.



Putting Vault-1 into a Non-Secure State
---------------------------------------

Once the transmitters are no longer triggering, the accelerator and transmitters can be disarmed.
This can be done by pressing the ACCELERATOR RESET button on the Vault-1 Control IONZING RADIATION INTERLOCK protocase, or simply opening the sheild door will disarm the system.
However, 2 minute must pass from the transmitters being brought to a safe state an the accelerator being disarmed before the Vault-1 door can be opened.

Vault-1 Radiation Survey Procedure
----------------------------------

To enter Vault-1 after the accelerator has been running, the vault must be scanned for ionizing radiation.
Once the 2 minute time has elapsed, the Vault-1 door can be opened to perform the survey.


.. figure:: /images/radiation_survey/dosimeter.png
    :align: center

    **Figure 16:** This is your personal dosimeter. This is to be worn at all times when in the CXLS suite. 

.. figure:: /images/radiation_survey/Ludlum_9DP.png
    :align: center

    **Figure 17:** This is the Ludlum 9DP pressurized ion gas chamber gamma detector. 

.. figure:: /images/radiation_survey/Ludlum_23.png
    :align: center

    **Figure 18:** This is the Ludlum 23 electronic personal dosimeter.




Overriding the Transmitters to Work in an Armed State
-----------------------------------------------------

When the transmitters are armed, attempting to remove the side panels for maintance will cause the transmitters to lose power. 
If work needs to be done on the transmitters in an armed state, you must override the interlocks on the transmitters. 
To do this turn the OVERRIDE key on the Vault-1 Control IONZING RADIATION INTERLOCK protocase. 
The STATUS lamp for the transmitter in override will turn orange. 
In this state, working on the armed transmitters will not cause the interlocks to trip.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_transmitter_override.jpg
    :scale: 20 %
    :align: center

    **Figure 19:** This is the Vault-1 Control Ionizng Radiation Protocase when a transmitter is in override.