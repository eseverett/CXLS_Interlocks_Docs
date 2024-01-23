.. These are used to call classes from the custom.css file.
.. role:: orange
.. role:: green
.. role:: blue

Vault-1 Laser Interlock System User Manual
==========================================

Vault-1 Laser Hazard Indicators
-------------------------------

For the Vault-1 laser interlocks system, there are multiple indicators that inform you of the state of the systems. 
This includes status beacons, LED display, and interlock warning modules.


Protocases
^^^^^^^^^^

The Pharos and Dira LASER ENCLOSURE INTERLOCK protocases show hazards in for the administrative override status of their specific enclosure. 

The PERIMETER section of the protocases has a laser warning module and door monitor module. 
The laser warning module displays if the Astrella is forced into a safe state. 
This means it will always show laser safe unless the interlocks are tripped. 
The door monitor shows if the enclosure doors are opened or closed. 
If the enclosure is put into an override state, then the monitor will always show closed because the interlocks are bypassed. 

The LOCAL INTERLOCK CONTACT CONTROL section of the protocases has two local interlock modules. 
These modules are for arming the UV and IV shutter controllers for manual operation. 
These can only be armed when the enclosure is armed. 
However, if the enclosure is not set to override, then these will disarm when opening the enclosure. 
The labeling of the Pharos and Dira protocases differs here. 
On the Pharos protocase the local interlock modules are labeled CONTACT #1 AND CONTACT #2, while on the Dira enclosure they are labeled AUX #1 and AUX #2. 
Though they are labeled differently, they function the same. 

The INTERLOCK OVERRIDE section of the protocases shows the status of the enclosure interlocks. 
If the key is set to OVERRIDE and the STATUS LED is :red:`red`, that means that the enclosure interlocks are bypass, and there could be a laser hazard if the enclosure is opened. 

.. figure:: /images/user_docs/Vault-1_laser/Pharos_protocase.jpg
   :scale: 20 %
   :align: center

   **Figure 1:** Vault-1 Pharos enclosure protocase. 
   It is located on the east wall of the Pharos enclosure.

.. figure:: /images/user_docs/Vault-1_laser/Dira_protocase.jpg
    :scale: 20 %
    :align: center

    **Figure 2:** Vault-1 Dira enclosure protocase. 
    It is located on the east wall of the Dira enclosure.

Beacon Stacks
^^^^^^^^^^^^^

There are beacon stacks in Vault-1 Control, on the Vault-1 east wall, on the Pharos LASER ENCLOSURE INTERLOCK protocase, and on the Dira LASER ENCLOSURE INTERLOCK protocase. 
The beacons stacks can notify you of the arming status for Vault-1, the Pharos enclosure, and the Dira enclosure. 
Also, the beacon stacks can notify you if there is an enclosure whose interlocks are in administrative override. 

.. list-table::
    :header-rows: 1

    * - Status
      - Beacon Color

    * - Vault-1 is not armed as a laser lab. Vault-1 is laser safe. 
      - :green-cell:`Beacon Color`

    * - Either the Pharos or Dira enclosures are set to administrative override. 

        This state is only possible if Vault-1 is armed.
      - :orange-cell:`Beacon Color`

    * - The Dira is armed.

        This state is possible with or without Vault-1 being armed.
      - :white-cell:`Beacon Color`

    * - The Pharos is armed.

        This state is possible with or without Vault-1 being armed. 
      - :blue-cell:`Beacon Color`


For the enclosure specific beacon stacks, the administrative override LED (:orange:`orange`) will only light if that specific enclosure is in override. 
The general Vault-1 and Vault-1 Control beacon stacks will light the administrative override LED (:orange:`orange`) if either of the enclosures are in override. 

The Pharos LASER ENCLOSURE INTERLOCK protocase is the only protocase without a white beacon. 
That is because the state of the Dira does not affect the state inside of the Pharos enclosure. 
However, the Dira LASER ENCLOSURE INTERLOCK protocase has a blue beacon because the Pharos exports a beam into the Dira enclosure, so the state of the Pharos affects the Dira enclosure.

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_Control_beacons.jpg
   :scale: 20 %
   :align: center

   **Figure 3:** This is the Vault-1 Control beacon stack.

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_beacons.jpg
    :scale: 20 %
    :align: center
    
    **Figure 4:** This is the Vault-1 beacon stack. 
    It is located on the east wall of Vault-1.


VIEWMARQ Display
^^^^^^^^^^^^^^^^

There is a VIEWMARQ display in Vault-1 Control that states the status of potential laser hazards in Vault-1. 
This display will notify you if Vault-1, the Pharos, or the Dira is armed. 
Also, it will notify you if the Pharos, the Dira, or both laser enclosures are in administrative override. 

+-------------------------------------------------------------+----------------------------------------------------+
| VIEWMARQ Display Notes                                      | VIEWMARQ Display Text                              |
+=============================================================+====================================================+
| This states if Vault-1 is armed as a laser lab or not.      | :green:`LASER SAFE` / :green:`DANGER LASER HAZARD` |
+-------------------------------------------------------------+----------------------------------------------------+
| This states which laser is armed.                           | :red:`PHAROS ARMED            DIRA ARMED`          |
+-------------------------------------------------------------+----------------------------------------------------+
| This states if the Dira is in administrative override.      | :red:`DIRA ADMIN OVERRIDE`                         |
+-------------------------------------------------------------+----------------------------------------------------+
| This states you if the Pharos is in administrative override.| :red:`PHAROS ADMIN OVERRIDE`                       |
+-------------------------------------------------------------+----------------------------------------------------+

The top line always will either display LASER SAFE or DANGER LASER HAZARD. 
All other possible states will only appear on the display when the hazard is presented. 
See Figure 3.

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
    This warning module tells you if the local interlock is armed or not.


.. figure:: /images/laser_safety_systems/room_arm.png
    :align: center

    **Figure 7:** Room Arm Module

    This module is used to arming system systems in the laser interlock system.
    For example, there are two in Vault-1, one to arm the vault and one to arm the Pharos enclosure.


.. list-table::
  :header-rows: 1

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

  * - Module Message
    - Message Meaning
  * - :orange:`LOCAL CONTACTS ARMED`
    - If this LED is on, then the corresponding sub-system is armed.
  * - :green:`LOCAL CONTACTS DISARMED`
    - | If this LED is on, then the connected room module is aremd, 
      | but this module is not.
  * - | :green:`LOCAL CONTACTS DISARMED`
      | :green:`ROOM NOT ARMED`
      | :green:`LOCAL CONTACT CANNOT ARM`
    - | If this LED is on, then there was a fault that tripped, or the room 
      | module is not armed.


.. figure:: /images/laser_safety_systems/push_to_exit.png
    :align: center

    **Figure 9:** Push to Exit Module

    This module is used to exit when a room is armed as a laser lab.
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

    When the e-stop is presed, the LED in the center will turn on.
    To reset the e-stop, twist the button clockwise.


Arming Vault-1 Laser Systems
----------------------------

In Vault-1, the laser systems that can be armed are Vault-1 (as a laser lab), the Pharos enclosure, and the Pharos. 
The Dira is in Laser-1 and must be armed from Laser-1. 
The arming of the Dira is discussed in User Documentation: Laser-1.

Arming the Pharos Enclosure and Laser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because the Pharos is contained in an enclosure, Vault-1 does not need to be armed to arm the Pharos enclosure and laser. 
To arm the Pharos enclosure and laser, press arm on the room interlock module on the south wall of the Pharos enclosure. 
The room interlock module arms the enclosure. 
For the Pharos system only, the local interlock module arms the Pharos laser underneath the room interlock module auto-arms with the room interlock module.
The Pharos enclosure and laser always arm together.

Once the Pharos system is armed the following will change in the interlock system:

- The Pharos is now producing a laser beam.
- Beacon stack :blue:`blue` LEDs will tuen on, indicating the Pharos.
- The VIEWMARQ display will show :red:`PHAROS ARMED`.
- The laser warning modules on the Pharos enclosure will show :red:`DANGER LASER ON`.
- Pharos enclosure e-stop buttons will turn on, shown by the LED in the center. The e-stops are now functional and will crash the Pharos is pressed.

.. figure:: /images/user_docs/Vault-1_laser/Pharos_enclosure_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 13:** These are the modules for the arming of the Pharos enclosure. 
    This is how the modules look when the Pharos enclosure is not armed.

.. figure:: /images/user_docs/Vault-1_laser/Pharos_enclosure_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 14:** This is the modules after arming of the Pharos enclosure after it is armed.
    There is a laser hazard indicator module on the west wall of the enclosure that will also update once this is armed. 

Arming Vault-1 as a Laser Lab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If work in an armed enclosure must be performed in Vault-1, then Vault-1 must be armed as a laser lab. 
To arm Vault-1 as a laser lab, press arm on the room interlock module in the Vault-1 entry. 
Unlike for the ionizing radiation interlock system, Vault-1 does not have search buttons, however it is the responsibility of the user to ensure that Vault-1 is cleared or proper PPE is distributed before arming Vault-1. 
Once Vault-1 is armed, the laser curtain door must be closed. The curtain door is not interlocked and it strickly the responsibility of the user.
When the laser curtain is open, there will be a chimming prompting the user to close the curtain.  

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 15:** These are the modules for arming Vault-1 as a laser lab. 
    This is how the modules look when Vault-1 is not armed.

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 16:** This is the moduels after arming Vault-1 as a laser lab.
    This also updates the laser hazard indicator in Vault-1 Control. 

Once Vault-1 is armed as a laser lab the following will change in the interlock system:

- Beacon stack LEDs will turn off, indicating that Vault-1 is not longer laser safe.
- The VIEWMARQ display will show :red:`DANGER LASER HAZARD`.
- The laser warning modules in Vault-1 Control and Vault-1 entry will show :red:`DANGER LASER ON`.
- The push to exit button will turn on, shown by the LED in the center.
- The Vault-1 door will be magnetically locked. 

Once Vault-1 is armed the door is magnetically locked. 
To get into Vault-1, you must type the Vault-1 laser pin into the keypad in Vault-1 Control. 
Once the pin is entered, the door will unlock for :red:`###`.
To exit Vault-1, you must push the push to exit button, which will unlock the door for :red:`###`.
It is important to note that Vault-1 will disarm itself and shutter all exposed laser hazards if the Vault-1 door is open for longer than the timer. 

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_entry_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 17:** These are the modules in Vault-1 Control for seeing the arming statsu and entering the armed vault.


User Laser Enclosure Interlock Protocases for Overriding Interlocks and Manual Shutter Control
----------------------------------------------------------------------------------------------

The shutters in the laser enclosures can be armed for manual control by the protocase LOCAL INTERLOCK CONTRACT CONTROL local interlock modules.
However, when the laser enclosures are interlocked, regardless of the arming status of the enclosure and Vault-1, if someone attempts to open the rolling enclosure doors the shutters will disarm and close.

What you will see happen on the enclosure protocase if the rolling door is opened when interlocked is:

- Laser warning modules will show LASER SAFE.
- Door monitor module will be blank, meaning open.
- LOCAL INTERLOCK CONTACT CONTROL local interlock modules will be disarmed if armed, automatically closing the shutters.

Interlock to Override
---------------------

The only way to work in the laser enclosures with light on the table is to change the enclosures interlocks to administrative override. 
In administrative override the interlocks system sees the rolling doors and closed even if they are opened, bypassing the interlocks.  

For a laser enclosure to be put into administrative override, both Vault-1 and the enclosure must be armed. 
Specifically for the working with the Dira, both the Pharos and Dira enclosures muss exports a beam into the Dira enclosure, so both enclosure interlocks need to be bypassed. 
t be set to administrative override. 
This is because the Pharo
The controls for the administrative overrides are on the enclosures LASER ENCLOSURE INTERLOCK protocase. 
Turn the key on the protocase under INERLOCK OVERRIDE from INTERLOCK TO OVERRIDE. 

Once the enclosure is put into override the following will change in the interlock system:

- The administrative override :orange:`orange` LED on the enclosure specific protocase will turn on.
- The Vault-1 Control and Vault-1 entry eat wall administrative override :orange:`orange` LEDs will turn on.
- The enclosure specific protocase STATUS LED will turn :red:`red`.
- If you open the enclosure, the laser warning module will still show :red:`LASER DANGER ON`, the door monitor module will show :green:`CLOSED`, and the local interlock modules for arming shutter manula control will not disarm. 

At this point, the LOCAL INTERLOCK CONTACT CONTROL interlock modules can be armed, and the shutters can be controlled manually without the interlocks disarming manual usage. 

.. figure:: /images/user_docs/Vault-1_laser/Pharos_protocase_override.jpg
    :scale: 20 %
    :align: center

    **Figure 18:** This is the Pharos enclosure protocase after it is set to administrative override.

Disarming the Laser Interlock System
------------------------------------

To take either enclosures out of administrative override, simply change the INTERLOCK OVERRIDE key on the LASER ENCLOSURE INTERLOCK protocase back from OVERRIDE to INTERLOCK. 
Also, all the arming laser modules have disarming buttons where you can either disarm specific modules you no longer need, or you can disarm the room modules to auto-disarm their local modules. 