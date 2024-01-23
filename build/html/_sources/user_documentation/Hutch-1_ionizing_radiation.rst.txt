.. This role was added beacuse the file was not recognizing the custom.css orange-cell class without it.
.. role:: orange-cell

Hutch-1 Ionzing Radiation Interlock System User Manual
======================================================

Hutch-1 Ionizing Radiation Hazard Indicators
--------------------------------------------

Unlike the Vault-1 ionizing radiation interlocks system, the VIEWMARQ display in Hutch-1 Control only shows the status of the Hutch-1 laser interlocks system. 

Protocase
^^^^^^^^^

The Hutch-1 Control IONIZING RADIATION INTERLOCK protocase shows multiple different hazards in Hutch-1.

The SERCURE PERIMETER section of the protocase shows the status of search buttons being engaged and if the sheild door is open. 
If all the lamps are :green:`green`, then Hutch-1 is in a secure state. When Hutch-1 is secure the hutch cannot be entered until the accelerator is put into an unarmed state.
If the shield door is opened with the accelerator and/or transmitters armed, then the interlock system will trip and close the double tungsten shutter. 
Once Hutch-1 is secured the allowed dose rate on the Hutch-1 ratemeters changes from the non-radiation facility user setpoint of 50 µS/hr to the radiation worker setpoint of 500 µS/hr.

The AREA MONITOR section of the protocase shows if any ratemeter in the CXLS suite is alarming. 
If the RADIATION lamp is :red:`red`, then there is either an alarm or fail status from one of the ratemeters. 
If any of the radiation meters alarm then the interlocks will trip, and the accelerator will be put into a safe state. 

The BEAM STOP section of the protocase shows if the beam stop is open. 
If the lamp is green, then the beam stop is open, and beam is being imported into Hutch-1. 
Above that are the BEAM STATUS AND BEAM SELECT lamps, which show if the divergent or collimated beam is being imported into Hutch-1. 
While these lamps should show the same thing, BEAM SELECT shows what the user has selected and BEAM STATUS shows the actual positions of the shutters, green being open. 

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_protocase.jpg
    :scale: 20 %
    :align: center

    **Figure 1:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase. In this state, Hutch-1 is not secured


O2 Main and Remote Units
^^^^^^^^^^^^^^^^^^^^^^^^

Ther eare two :math:`O_{2}` sensors in the Hutch-1 ionizing radiation interlock system. 
One is located on the Hutch-1 west wall and the other is located in the Astrella enclosure. 
These units will have an audible alarm and flash one of the AL# LEDs depending on the alarm setpoint it passed. 
Any :math:`O_{2}` reading below 19% will cause the sensors to alarm. 
Each :math:`O_{2}` sensor has a remote unit that only displays information from the main sensor unit.
The Hutch-1 west wall and Astrella enclosure :math:`O_{2}` remote units are located in Hutch-1 Control next to the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_O2_main.jpg
    :scale: 20 %
    :align: center

    **Figure 2:** This is the :math:`O_{2}` main unit located in Vault-1. Under this condition there is no alarm.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_O2_remote.jpg
    :scale: 20 %
    :align: center

    **Figure 3:** This is the :math:`O_{2}` remote unit located in Vault-1 Control. Under this condition there is no alarm. 

Beacons
-------

.. list-table::
    :header-rows: 1

    * - Status
      - Beacon Color
    * - The :red:`red` beacon indicated that an ionizing radiation emergency stop button had been

        pressed. This beacon is also on the Vault-1 Control protocase.
      - :red-cell:`Beacon Color`
    * - The orange beacon indicates that one of the O2 meters isreading below 19% oxygen

        levels.
      - :orange-cell:`Beacon Color`

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_protocase_beacon.jpg
    :scale: 20 %
    :align: center

    **Figure 4:** This is the Hutch-1 Control beacon that corresponds to the ionizing radiation emergency stop.

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_O2_beacon.jpg
    :scale: 20 %
    :align: center

    **Figure 5:** This is the Hutch-1 Control O2 beacon that corresponds to both Hutch-1 O2 sensors.


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

Search Procedure for Securing Hutch-1
-------------------------------------

To be able to allow either of the double tungsten shutters to be opened, Huth-1 must be secured. To secure Hutch-1, it must be cleared, searched, and the Hutch-1 search buttons need to be pressed in the correct sequence. 
Starting in the back of Hutch-1 while verifying the hutch is empty, press the search button labeled 1. 
As you continue to search press 2 then 3 as you're working your way towards the front of Hutch-1. 
Once the 3rd search button is pressed, a chime will be audible and a # timer will start. 
If the shield door is not completely closed by the end of the timer, the search buttons will reset, and Hutch-1 will need to be researched. 


.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch1_Search_Buttons.png
    :scale: 50 %
    :align: center

    **Figure 8:** This is a diagram of the Hutch-1 search buttons. The numbers indicate the order in which they need to be pressed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
    :scale: 20 %
    :align: center

    **Figure 9:** This one of the search buttons in Vault-1 when not pressed.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** This one of the search buttons in Vault-1 when pressed.

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_searched.jpg
    :scale: 20 %
    :align: center

    **Figure 11:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase when Hutch-1 is searched.

Once Hutch-1 is searched and all the search buttons have been pressed in the correct sequence, all the SECURE PEREIMETER SEARCH lamps on the Hutch-1 Control IONZING RADIATION INTERLOCK protocase will be :green:`green`. 
Unlike the Vault-1 door, this door is closed manually. 
Once the door is fully closed and actuating the door switches the SECURE PERIMETER SHEILD DOOR lamp on the Hutch-1 Control IONIZING RAIDTION INTERLOCK protocase will be :green:`green`. 

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_door.jpg
    :scale: 20 %
    :align: center

    **Figure 12:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase when Hutch-1 is secured.

Controlling the Beam Status in Hutch-1
--------------------------------------

The beam stop can only be opened once Hutch-1 is searched and secured. 
Once secured, the beam stop can be opened by turning the BEAM STOP OPEN key on the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase, the lamp should turn :green:`green` when the stop is open.
If the shield door is opened with the beam stop open, then the shutters will close, and Hutch-1 will no longer be secure.

.. note::
    Images need to be added showing the stages of using the BEAM STOP and BEAM SELECT sections.

At any point, the shutters can be closed again by hitting BEAM STOP RESET on the Hutch-1 IONIZING RADIATION INTERLOCK protocase. 

When the beam stop is open, the shutters will only allow either the collimated or divergent beam into Hutch-1. 
To select which beam is allowed into Hutch-1 use the BEAM SELECT key on the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase. 
The BEAM SELECT lamp shows what has been selected, and the BEAM STATUS lamp shows what the status of the shutters is. 

Putting Hutch-1 into a Non-Secure State
---------------------------------------

Once work in Hutch-1 is completed and is no longer required to be in a secure state, press the BEAM STOP RESET button on the Hutch-1 IONIZING RADIATION INTERLOCK protocase and open the shield door. 

