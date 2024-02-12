Laser-1 Interlock System User Manual
====================================

This document provides a user overview for the Laser-1 Laser Interlock System.
It covers the laser modules, hazard indicators, control protocases, VIEWMARQ display, and the beacons in Vault-1 and Vault-1 Control.
The laser modules are used for indicating the status of the laser interlock system and arming the laser systems.
The control protocase allows the users to view the override state of the laser enclosure and control the manual shutter control. 
The VIEWMARQ display provides a quick overview of the laser hazard status in Vault-1.
The beacons are used to indicate the state of laser hazards in Vault-1 and the laser enclosures.

Laser-1 Laser Hazard Warning Indicators
---------------------------------------

Unlike the Vault-1 and Hutch-1 laser interlocks systems, there are no beacon stacks for displaying the state of the laser interlock system. 
Additionally, because the Dira enclosure is in Vault-1 there is no protocase discussed in this manual. 

VIEWMARQ Display
^^^^^^^^^^^^^^^^

There is a VIEWMARQ display outside of the Laser-1 entrance and inside of the Laser-1 airlock.  

+-------------------------------------------------------------+----------------------------------------------------+
| VIEWMARQ Display Notes                                      | VIEWMARQ Display Text                              |
+=============================================================+====================================================+
| This states if Laser-1 is armed as a laser lab or not.      | :green:`LASER SAFE` / :red:`DANGER LASER HAZARD`   |
+-------------------------------------------------------------+----------------------------------------------------+
| This states which hazard is armed.                          | :red:`IR HAZARD`        :red:`AUX 3 HAZARD`        |
+-------------------------------------------------------------+----------------------------------------------------+
| This states which hazard is armed.                          | :red:`UV HAZARD`     :red:`AUX 4 HAZARD`           |
+-------------------------------------------------------------+----------------------------------------------------+
| This states which hazard is armed.                          | :red:`AUX 2 HAZARD`                                |
+-------------------------------------------------------------+----------------------------------------------------+

The top line always will either display LASER SAFE or DANGER LASER HAZARD. 
All other possible states will only appear on the display when the hazard is presented. 
Additionally, the VIEWMARQ display in the Laser-1 airlock will display the same message as the VIEWMARQ outside of Laser-1. 
The airlock VIEWMARQ can only support one-line messages, so the whole message is truncated to one line and moves across the display. 

.. figure:: /images/user_docs/Laser-1/Laser-1_entry_safe.jpg
    :scale: 20 %
    :align: center

    Laser-1 entryway with the VIEWMARQ display showing LASER SAFE.

.. figure:: /images/user_docs/Laser-1/Laser-1_airlock_safe.jpg
    :scale: 20 %
    :align: center

    Laser-1 airlock with the VIEWMARQ display showing LASER SAFE.


Laser Emergency Stop Buttons
----------------------------

All the laser enclosures are equipped with laser emergency stop buttons. 
The e-stops on an enclosure can only crash that specific laser. 
Additionally, there are ionizing radiation emergency stop buttons in Vault-1 and Vault-1 Control. 
Those only serve the purpose of crashing the transmitters and are not located on the laser enclosures.


.. figure:: /images/user_docs/Vault-1_laser/laser_e-stop_off.jpg
    :scale: 20 %
    :align: center

    **Figure 5:** This is a laser emergency stop button in the off state.

.. figure:: /images/user_docs/Vault-1_laser/laser_e-stop_on.jpg 
    :scale: 20 %
    :align: center

    **Figure 6:** This is a laser emergency stop button in the on state.


Arming Laser-1 Laser Systems
----------------------------

In Laser-1, there are arming modules for Laser-1, the Dira, and 4 auxiliary hazards. All laser modules for arming systems are located on the arming panel. 

.. figure:: /images/user_docs/Laser-1/Laser-1_arming_panel.jpg
    :scale: 20 %
    :align: center

    **Figure 7:** This is the arming panel for Laser-1.


Arming Laser-1 and the Dira Enclosure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Laser-1 must be armed to do laser work. To arm Laser-1, press arm on the room interlock module labeled Laser-1. 
The Laser-1 arming module also serves as the arming module for the Dira enclosure. 

When Laser-1 is armed, the following will happen to the interlock system:

- The VIEWMARQ display will show DANGER LASER HAZARD.
- Laser emergency stop buttons in Laser-1 and around the Vault-1 Dira enclosure will turn on. 
- Laser warning modules outside of Laser-1, inside of the Laser-1 airlock, and on the Dira LASER ENCLOSURE INTERLOCK protocase will display DANGER LASER ON.


Once Laser-1 is armed the door is magnetically locked. 
To get into Vault-1, you must type the Laser-1 laser pin into the keypad in Vault-1 Control. 
Once it is entered the door will be temporarily unlocked. 
To exit Laser-1, you must push the push to exit button. Once pressed the door will be temporarily unlocked. 
It is important to note that Laser-1 will disarm itself and shutter all laser hazards if the Laser-1 door is open for  #. 

.. figure:: /images/user_docs/Laser-1/Laser-1_control_module_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 8:** This is the Laser-1 arming module in the armed state.

.. figure:: /images/user_docs/Laser-1/Laser-1_push_to_exit.jpg
    :scale: 20 %
    :align: center

    **Figure 9:** This is the push to exit button for Laser-1.

.. figure:: /images/user_docs/Laser-1/Laser-1_entry_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** This is the Laser-1 entryway with the VIEWMARQ display showing DANGER LASER HAZARD.


Arming the Dira
^^^^^^^^^^^^^^^

To arm the Dira, press arm on the local interlock module labeled Dira. 
Because the Dira exports a laser hazard into Vault-1, Vault-1 laser hazard indicators will update.

When the Dira is armed, the following will happen to the interlock system:

- The VIEWMARQ displays will show IR HAZARD.
- The VIEWMARQ in Vault-1 Control will display DIRA ARMED.
- The beacon stacks in the Vault-1 laser interlock system will turn on the white Dira armed LED.


Arming Auxiliary hazards
------------------------

.. note::

    The auxiliary hazards are not currently in use.


Disarming the Laser Interlock System
------------------------------------

All the arming laser modules have disarming buttons. 
You can either disarm specific modules you no longer need, or you can disarm the room modules to auto-disarm their local modules. 
