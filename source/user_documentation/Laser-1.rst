.. these roles are here to use custom css classes
.. role:: white-cell
.. role:: orange

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
Additionally, because the Dira enclosure is in Vault-1 there is no protocase corresponding to Laser-1.

VIEWMARQ Display
^^^^^^^^^^^^^^^^

There is a VIEWMARQ display outside of the Laser-1 entrance and inside of the Laser-1 airlock.  

.. list-table::
        :header-rows: 1
        :align: center

        * - VIEWMARQ Display Notes
          - VIEWMARQ Display Text
        * - This states if Laser-1 is armed as a laser lab or not.
          - :green:`LASER SAFE` / :red:`DANGER LASER HAZARD`
        * - This states which hazard is armed.
          - :red:`IR HAZARD`        :red:`AUX 3 HAZARD`
        * - This states which hazard is armed.
          - :red:`UV HAZARD`     :red:`AUX 4 HAZARD`
        * - This states which hazard is armed.
          - :red:`AUX 2 HAZARD`

The top line of the Laser-1 entry VIEWMARQ will always either display :green:`LASER SAFE` or :red:`DANGER LASER HAZARD`. 
All other possible states will only appear on the display when the hazard is presented. 
Additionally, the VIEWMARQ display in the Laser-1 airlock will display the same message as the VIEWMARQ outside of Laser-1. 
The airlock VIEWMARQ can only support one-line messages, so the whole message is truncated to one line and moves across the display. 

.. .. figure:: /images/user_docs/Laser-1/Laser-1_entry_safe.jpg
..     :scale: 20 %
..     :align: center

..     Laser-1 entryway with the VIEWMARQ display showing LASER SAFE.

.. .. figure:: /images/user_docs/Laser-1/Laser-1_airlock_safe.jpg
..     :scale: 20 %
..     :align: center

    .. Laser-1 airlock with the VIEWMARQ display showing LASER SAFE.

.. list-table::
    :align: center

    * - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_safe.jpg
          :scale: 20 %
          :align: center

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_armed.jpg
          :scale: 20 %
          :align: center

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_IR.jpg
          :scale: 20 %
          :align: center

    * - This figure shows the Laser-1 entry VIEWMARQ in a safe condition. :white-cell:`============================`
      - This figure shows the Laser-1 entry VIEWMARQ when Laser-1 is armed. :white-cell:`==========================`
      - This figure shows the Laser-1 entry VIEWMARQ when the Dira is armed. :white-cell:`=========================`

.. table-caption::
    **Figure 1:** This is the Laser-1 entry VIEWMARQ in different states.


.. list-table::
  :align: center

  * - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_safe.jpg
        :scale: 20 %
        :align: center

    - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_armed.jpg
        :scale: 20 %
        :align: center

    - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_IR.gif
        :scale: 56 %
        :align: center

  * - This figure shows the Laser-1 airlock VIEWMARQ in a safe condition. :white-cell:`============================`
    - This figure shows the Laser-1 airlock VIEWMARQ when Laser-1 is armed. :white-cell:`==========================`
    - This figure shows the Laser-1 airlock VIEWMARQ when the Dira is armed. :white-cell:`=========================`

.. table-caption::
    **Figure 2:** This is the Laser-1 airlock VIEWMARQ in different states.




.. Laser Emergency Stop Buttons
.. ----------------------------

.. All the laser enclosures are equipped with laser emergency stop buttons. 
.. The e-stops on an enclosure can only crash that specific laser. 
.. Additionally, there are ionizing radiation emergency stop buttons in Vault-1 and Vault-1 Control. 
.. Those only serve the purpose of crashing the transmitters and are not located on the laser enclosures.


.. .. figure:: /images/user_docs/Vault-1_laser/laser_e-stop_off.jpg
..     :scale: 20 %
..     :align: center

..     **Figure 5:** This is a laser emergency stop button in the off state.

.. .. figure:: /images/user_docs/Vault-1_laser/laser_e-stop_on.jpg 
..     :scale: 20 %
..     :align: center

..     **Figure 6:** This is a laser emergency stop button in the on state.

Laser Safety System Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The laser interlock system is interfaced through the laser safety systems modules. Below is an outline of the modules and what they do. 

.. figure:: /images/laser_safety_systems/warning_module.gif
    :align: center

    **Figure 5:** Area Warming Module

.. list-table::
  :header-rows: 1

  * - Module Location
    - Module Meaning
  * - | **General Area Module**
      | Vault-1 Control
      | Vault-1 Entry
    - | These are warning modules tell you if Vault-1 is armed as a laser lab. 
      | :red:`DANGER LASER ON` = ARMED
  * - | **Enclosure Modules**
      | Pharos enclosure south wall
      | Pharos enclosure west wall
    - | These warning modules tell you if the enclosure is armed.
      | There is no indication on if the laser is armed. 
      | :red:`DANGER LASER ON` = ARMED
  * - | **Protocase Modules**
      | Pharos enclosure protocase
      | Dira enclosure protocase
    - | These warning modules tell you if the enclosure is forced to a safe state. 
      | :red:`DANGER LASER HAZARD` = SAFE STATE IS NOT FORCED

.. figure:: /images/laser_safety_systems/control_module.gif
    :align: center

    **Figure 6:** Control Module

    This module is a control module for the local laser interlock, however, for the users it serves as another warning module.
    This warning module tells you if the room interlock is armed or not.


.. figure:: /images/laser_safety_systems/room_arm.png
    :align: center

    **Figure 7:** Room Arm Module

    This module is used to arm systems in the laser interlock system.
    For example, there are two in Vault-1, one to arm the vault and one to arm the Pharos enclosure.


.. list-table::
  :header-rows: 1
  :align: center

  * - Module Message
    - Message Meaning
  * - :orange:`ROOM ARMED`
    - | If this LED is on, then the corresponding system is armed 
      | and interlocked.
  * - :green:`ROOM DISARMED (READY TO ARM)`
    - | If this LED is on, the the system is the correct state to armed
      | the module.
  * - :orange:`ROOM CRASHED (CANNOT ARM)`
    - | If this LED is on, then there was a fault that tripped the 
      | system, or a fault that will not allow the system to be armed. 



.. figure:: /images/laser_safety_systems/local_arm.png
    :align: center

    **Figure 8:** Local Arm Module

    This module is used to arm the local interlock modules that are sub-systems of the room arm modules.
    For example, one the Pharos enclosure is armed, it enables the laser and the shutters to be armed by their local arming modules.

.. list-table::
  :header-rows: 1
  :align: center

  * - Module Message
    - Message Meaning
  * - :orange:`LOCAL CONTACTS ARMED`
    - | If this LED is on, then the corresponding sub-system is armed.
  * - :green:`LOCAL CONTACTS DISARMED`
    - | If this LED is on, then the connected room module is armed, 
      | but this module is not.
  * - | :green:`LOCAL CONTACTS DISARMED`
      | :green:`ROOM NOT ARMED`
      | :green:`LOCAL CONTACT CANNOT ARM`
    - | If this LED is on, then there was a fault that tripped, or the room 
      | module is not armed.


.. figure:: /images/laser_safety_systems/push_to_exit.png
    :align: center

    **Figure 9:** Push to Exit Module

    When the rooms are armed, the doors are magnetically locked.
    This button will temporarily unlock the door to allow you to exit the room.

.. figure:: /images/laser_safety_systems/key_pad.jpg
    :align: center

    **Figure 10:** Keypad

    This is the key pad that is used to enter a room that is armed as a laser lab. 
    This keypad has a primary pin for permanent users, and a secondary pin for temporary users that is meant to be changed frequently.

.. figure:: /images/laser_safety_systems/door_monitor.jpg
    :align: center

    **Figure 11:** Door Monitor Module

    This module is used to monitor the state of a door or curtain.
    It will display does not show :green:`CLOSED`, then it is open. 
    If the system is put into an administrative override state, then the door monitor will always show :green:`CLOSED`.


.. figure:: /images/laser_safety_systems/e_stop.png
    :align: center

    **Figure 12:** Laser Emergency Stop Button. 

    All the laser enclosures are equipped with laser emergency stop buttons. 
    The e-stops on an enclosure can only crash that specific laser. 

Additionally, there are ionizing radiation emergency stop buttons in Vault-1 and Vault-1 Control. 
Those only serve the purpose of crashing the transmitters and are not located on the laser enclosures.
When the e-stop is pressed, the LED in the center will turn on.
To reset the e-stop, twist the button clockwise.


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
