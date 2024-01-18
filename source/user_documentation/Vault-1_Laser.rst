Vault-1 Laser Interlock System User Manual
==========================================

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
If the key is set to OVERRIDE and the STATUS LED is red, that means that the enclosure interlocks are bypass, and there could be a laser hazard if the enclosure is opened. 

.. figure:: /images/user_docs/Vault-1_laser/Pharos_protocase.jpg
   :scale: 20 %
   :align: center

   **Figure 1:** Vault-1 Pharos enclosure protocase.

.. figure:: /images/user_docs/Vault-1_laser/Dira_protocase.jpg
    :scale: 20 %
    :align: center

    **Figure 2:** Vault-1 Dira enclosure protocase.

Beacon Stacks
^^^^^^^^^^^^^

There are beacon stacks in Vault-1 Control, on the Vault-1 east wall, on the Pharos LASER ENCLOSURE INTERLOCK protocase, and on the Dira LASER ENCLOSURE INTERLOCK protocase. 
The beacons stacks can notify you of the arming status for Vault-1, the Pharos enclosure, and the Dira enclosure. 
Also, the beacon stacks can notify you if there is an enclosure whose interlocks are in administrative override. 

.. This role was added beacuse the file was not recognizing the custom.css orange-cell, green-cell, white-cell class without it.
.. role:: orange-cell
.. role:: green-cell
.. role:: white-cell

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
      - :blue-cell:`Beaconq Color`

For the enclosure specific beacon stacks, the administrative override LED (orange) will only light if that specific enclosure is in override. 
The general Vault-1 and Vault-1 Control beacon stacks will light the administrative override LED (orange) if either of the enclosures are in override. 

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

Laser Warming module
^^^^^^^^^^^^^^^^^^^^

There are laser warning modules throughout the Vault-1 laser interlocks system. 
The location of the warning module dictates what the safe or danger status is indicating. 

.. figure:: /images/laser_safety_systems/warning_module.gif
    :align: center

    Laser Safety Systems laser area warning module. 

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

The Vault-1 entry module looks slightly different, being square instead of rectangular. 
That module is the laser interlock control module; however, it serves as a warning module as well. 

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

Arming Vault-1 Laser Systems
----------------------------

In Vault-1, the laser systems that can be armed are Vault-1, the Pharos enclosure, and the Pharos. 
The Dira is in Laser-1 and must be armed from Laser-1. 
The arming of the Dira is discussed in User Documentation: Laser-1.

Arming the Pharos Enclosure and Laser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because the Pharos is contained in an enclosure, Vault-1 does not need to be armed to arm the Pharos enclosure and laser. 
To arm the Pharos enclosure and laser, press arm on the room interlock module on the south wall of the Pharos enclosure. 
The room interlock module arms the enclosure. 
For the Pharos system only, the local interlock module arms the Pharos laser underneath the room interlock module auto-arms with the room interlock module. 

Once the Pharos system is armed the following will change in the interlock system:

- Light is now on the tabels in the Pharos and Dira enclosures.
- Beacon stack blue LEDs will tuen on, indicating the Pharos.
- The VIEWMARQ display will show PHAROS ARMED.
- The laser warning modules on the Pharos enclosure will show DANGER LASER ON.
- Pharos enclosure e-stop buttons will turn on, shown by the LED in the center. The e-stops are now functional and will crash the Pharos is pressed.

.. figure:: /images/user_docs/Vault-1_laser/Pharos_enclosure_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 7:** This is the Pharos enclosure before it is armed.

.. figure:: /images/user_docs/Vault-1_laser/Pharos_enclosure_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 8:** This is the Pharos enclosure after it is armed.

Arming Vault-1 as a Laser Lab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If work on armed lasers needs to be performed in Vault-1, then Vault-1 must be armed as a laser lab. 
To arm Vault-1 as a laser lab, press arm on the room interlock module in the Vault-1 entry. 
There is no local interlock module that is part of arming Vault-1, once the room module is armed Vault-1 is secured. 
Once Vault-1 is armed, the laser curtain door must be closed. The curtain door is not interlocked. 

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 9:** This is Vault-1 before it is armed.

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** This is Vault-1 after it is armed.

Once Vault-1 is armed as a laser lab the following will change in the interlock system:

- Beacon stack LEDs will turn off, indicating that Vault-1 is not longer laser safe.
- The VIEWMARQ display will show DANGER LASER HAZARD.
- The laser warning modules in Vault-1 Control and Vault-1 entry will show DANGER LASER ON.
- The push to exit button will turn on, shown by the LED in the center.
- The Vault-1 door will be magnetically locked. 

Once Vault-1 is armed the door is magnetically locked. 
To get into Vault-1, you must type the Vault-1 laser pin into the keypad in Vault-1 Control. 
Once it is entered the door will be temporarily unlocked. 
To exit Vault-1, you must push the push to exit button. Once pressed the door will be temporarily unlocked. 
It is important to note that Vault-1 will disarm itself and shutter all exposed laser hazards if the Vault-1 door is open for too long. 

.. figure:: /images/user_docs/Vault-1_laser/Vault-1_entry_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 11:** This is the Vault-1 entry after it is armed.


User Laser Enclosure Interlock Protocases for Overriding Interlocks and Manual Shutter Control
----------------------------------------------------------------------------------------------

The shutters in the laser enclosures can be armed for manual control by the protocase LOCAL INTERLOCK CONTRACT CONTROL local interlock modules. 
However, when the laser enclosures are interlocked, regardless of the arming status of the enclosure and Vault-1, if someone attempts to open the rolling enclosure doors the shutters will close.

What you will see happen on the enclosure protocase if the rolling door is opned when interlocked is:

- Laser warning modules will show LASER SAFE.
- Door monitor module will be blank, meaning open.
- LOCAL INTERLOCK CONTACT CONTROL local interlock modules will be disarmed if armed, automatically closing the shutters.

Interlock to Override
^^^^^^^^^^^^^^^^^^^^^

The only way to work in the laser enclosures with light on the table is to change the enclosures interlocks to administrative override. 
In administrative override the interlocks system sees the rolling doors and closed even if they are opened, bypassing the interlocks.  

For a laser enclosure to be put into administrative override, both Vault-1 and the enclosure must be armed. 
Specifically for the working with the Dira, both the Pharos and Dira enclosures must be set to administrative override. 
This is because the Pharos exports a beam into the Dira enclosure, so both enclosure interlocks need to be bypassed. 

The controls for the administrative overrides are on the enclosures LASER ENCLOSURE INTERLOCK protocase. 
Turn the key on the protocase under INERLOCK OVERRIDE from INTERLOCK TO OVERRIDE. 

Once the enclosure is put into override the following will change in the interlock system:

- The administrative override orange LED on the enclosure specific protocase will turn on.
- The Vault-1 Control and Vault-1 entry eat wall administrative override orange LEDs will turn on.
- The enclosure specific protocase STATUS LED will turn red.
- If you open the enclosure, the laser warning module will still show LASER DANGER ON, the door monitor module will show CLOSED, and the local interlock modules for arming shutter manula control will not disarm. 

At this point, the LOCAL INTERLOCK CONTACT CONTROL interlock modules can be armed, and the shutters can be controlled manually without the interlocks disarming manual usage. 

.. figure:: /images/user_docs/Vault-1_laser/Pharos_protocase_override.jpg
    :scale: 20 %
    :align: center

    **Figure 12:** This is the Pharos enclosure protocase after it is set to administrative override.

Disarming the Laser Interlock System
------------------------------------

To take either enclosures out of administrative override, simply change the INTERLOCK OVERRIDE key on the LASER ENCLOSURE INTERLOCK protocase back from OVERRIDE to INTERLOCK. 
Also, all the arming laser modules have disarming buttons where you can either disarm specific modules you no longer need, or you can disarm the room modules to auto-disarm their local modules. 