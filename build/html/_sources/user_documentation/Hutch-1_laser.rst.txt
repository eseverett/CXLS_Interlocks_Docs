Hutch-1 Laser Interlock System User Manual
==========================================

Hutch-1 Laser Hazard Warning Indicators
---------------------------------------

For the Hutch-1 laser interlocks system, there are multiple indicators that inform you of the state of the systems. 
This includes status beacons, LED display, and interlock warning modules.

Protocase
^^^^^^^^^

The Astrella LASER ENCLOSURE INTERLOCK protocase shows hazards in for the administrative override status of the Astrella enclosure. 

The PERIMETER section of the Astrella LASER ENCLOSURE INTERLOCK protocase has a laser warning module and door monitor module. 
The laser warning module displays if the Astrella is forced into a safe state. This means it will always show DANGER LASER ON unless the interlocks are tripped. 
The door monitor shows if the enclosure doors are opened or closed. If the enclosure is put into an override state, then the monitor will always show closed because the interlocks are bypassed. 

The LOCAL INTERLOCK CONTACT CONTROL section of the Astrella LASER ENCLOSURE INTERLOCK protocase are two local interlock modules. 
These modules are for arming the UV and IV shutter controllers for manual operation. 
These can only be armed when the enclosure is armed. However, if the enclosure is not set to override, then these will disarm when opening the enclosure.

The INTERLOCK OVERRIDE section of the Astrella LASER ENCLOSURE INTERLOCK protocase shows the status of the enclosure interlocks. 
If the key is set to OVERRIDE and the STATUS LED is red, that means that the enclosure interlocks are bypass, and there could be a laser hazard if the enclosure is opened. 

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_protocase.jpg
    :scale: 20 %
    :align: center

    Astrella LASER ENCLOSURE INTERLOCK protocase

Beacon Stacks
^^^^^^^^^^^^^

There are beacon stacks in Hutch-1 Control and on the Astrella LASER ENCLOSUREI INTERLOCK protocase. 
The beacons stacks can notify you of the arming status for Hutch-1 and the Astella, as well as the interlock status of the enclosure.

.. role:: orange-cell
.. role:: green-cell
.. role:: white-cell

.. list-table::
    :header-rows: 1

    * - Status
      - Beacon Color

    * - Hutch-1 is not armed as a laser lab. 
      - :green-cell:`Beacon Color`

    * - The Astrella is set to administrative override.

        This state is only possible if Hutch-1 is armed.
      - :orange-cell:`Beacon Color`

    * - The Astrella is armed.

        This state is possible with or without Hutch-1 being armed.
      - :white-cell:`Beacon Color`

VIEWMARQ Display
^^^^^^^^^^^^^^^^

There is a VIEWMARQ display in Hutch-1 Control that states the status of potential laser hazards in Hutch-1. 
This display can notify you of the arming status for Hutch-1 and the Astella, as well as the interlock status of the enclosure.

+-------------------------------------------------------------+----------------------------------------------------+
| VIEWMARQ Display Notes                                      | VIEWMARQ Display Text                              |
+=============================================================+====================================================+
| This states if Hutch-1 is armed as a laser lab or not.      | :green:`LASER SAFE` / :green:`DANGER LASER HAZARD` |
+-------------------------------------------------------------+----------------------------------------------------+
| This states if the Astrella is armed.                       | :red:`Astrella ARMED`                              |
+-------------------------------------------------------------+----------------------------------------------------+
| This states if the Astrella is in administrative override.  | :red:`Astrella ADMIN OVERRIDE`                     |
+-------------------------------------------------------------+----------------------------------------------------+

The top line always will either display LASER SAFE or DANGER LASER HAZARD. 
All other possible states will only appear on the display when the hazard is presented. 

Laser Warming module
^^^^^^^^^^^^^^^^^^^^

There are laser warning modules throughout the Hutch-1 laser interlocks system. 
The location of the warning module dictates what the safe or danger status is indicating. 

.. figure:: /images/laser_safety_systems/warning_module.gif
    :align: center

    Laser Safety Systems laser area warning module. 

.. list-table::
  :header-rows: 1

  * - Module Location
    - Module Meaning
  * - | **General Area Module**
      | Hutch-1 Control
      | Hutch-1 Entry
    - | These are warning modules tell you if Hutch-1 is armed as a laser lab. 
      | :red:`DANGER LASER ON` = ARMED
  * - | **Enclosure Modules**
      | Astrella enclosure south wall
      | Astrella enclosure west wall
    - | These warning modules tell you if the enclosure is armed.
      | There is no indication on if the laser is armed. 
      | :red:`DANGER LASER ON` = ARMED
  * - | **Protocase Modules**
      | Astrella enclosure protocase
    - | These warning modules tell you if the enclosure is forced to a safe state. 
      | :red:`DANGER LASER HAZARD` = SAFE STATE IS NOT FORCED

The Hutch-1 entry module looks slightly different, being square instead of rectangular. 
That module is the laser interlock control module; however, it serves as a warning module as well. 

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_VIEWMARQ_laser_safe.jpg
    :scale: 20 %
    :align: center

    Hutch-1 Control VIEWMARQ display when Hutch-1 is armed as a laser lab.

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

Arming Hutch-1 Laser Systems
----------------------------

The laser systems that can be armed are Hutch-1, the Astrella enclosure, and the Astrella laser.

Arming the Astrella Enclosure and Laser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because the Astrella is contained in an enclosure, Hutch-1 does not need to be armed to arm the Astrella enclosure and laser. 
To arm the Astrella enclosure, press arm on the room interlock module on the south wall of the enclosure. 
The room interlock module arms the enclosure. 

Once the Astrella enclosure is armed, the Astrella laser can be armed with the local interlock module to the right of the room interlock module. 

Once the Astrella system is armed the following will change in the interlock system:

- Light is now on the table in the Astrella enclosure.
- Beacon stack white LEDs will turn on, indicating that the Astrella is armed.
- The VIEWMARQ display will show ASTRELLA ARMED.
- The laser warning module on the Astrella enclosure protocase will show DANGER LASER ON.
- Astrella enclosure e-stop buttons will turn on, shown by the LED in the center. The e-stops are now functional and will crash the Astrella laser if presesd.

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_enclosure_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 7:** Astrella enclosure unarmed.

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_enclosure_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 8:** Astrella enclosure armed.


Arming Hutch-1
^^^^^^^^^^^^^^

If work on armed lasers needs to be performed in Hutch-1, then Hutch-1 must be armed as a laser lab. 
To arm Hutch-1 as a laser lab, press arm on the room interlock module in the Hutch-1 entry. 
There is no local interlock module that is part of arming Hutch-1. once the room module is armed Hutch-1 is secured. 
The 2nd layer laser curtain door must be closed.  

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_unarmed.jpg
    :scale: 20 %
    :align: center

    **Figure 9:** Hutch-1 unarmed.

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** Hutch-1 armed.

These are the laser safety modules in the Hutch-1 entry. 
On the left are the modules in an unarmed state, and on the right are the modules in an armed state. 
In these images, from the top down are the laser control module (serving as a warning module), the push to exit button, and the room interlock module (arms Hutch-1 as a laser lab).

Once Hutch-1 is armed as a laser lab the following will change in the interlock system:

- Beacon stack green LEDs will turn off, indicating that Hutch-1 is armed.
- The VIEWMARQ display will show DANGER LASER HAZARD in place of LASER SAFE.
- The laser warning modules in Hutch-1 Control and Hutch-1 Entry will show DANGER LASER ON.
- The push to exit button will be on, shown by the LED in the button. 
- The Hutch-1 curtain door will be magnetically locked.

Once Hutch-1 is armed the curtain door is magnetically locked. 
To get into Hutch-1, you must type the Hutch-1 laser pin into the keypad in Hutch-1 Control. 
Once it is entered the door will be temporarily unlocked. 
To exit Hutch-1, you must push the push to exit button. 
Once pressed the door will be temporarily unlocked. 
It is important to note that Hutch-1 will disarm itself and shutter all laser hazards if the Hutch-1 door is open for longer than # . 

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_entry_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 11:** Hutch-1 entry armed.

Using Laser Enclosure Interlock Protocase for Overriding Interlocks and Manual Shutter Control
----------------------------------------------------------------------------------------------

The shutters in the laser enclosures can be armed for manual control by the protocase LOCAL INTERLOCK CONTRACT CONTROL local interlock modules. 
However, when the laser enclosures are interlocked, regardless of the arming status of the enclosure and Hutch-1, if someone attempts to open the enclosure doors the shutters will close.

What you will see happen on the enclosure protocase if the door is opened when interlocked is:

- Laser warning module will show LASER SAFE.
- Door monitor module will be blank, meaning open.
- LOCAL INTERLOCK CONTACT CONTROL local interlock modules will disarm if armed, automatically closing the shutters.

Interlock to Override
^^^^^^^^^^^^^^^^^^^^^

The only way to work in the laser enclosures with light on the table is to change the enclosures interlocks to administrative override. 
In administrative override the interlocks system sees the rolling doors and closed even if they are opened, bypassing the interlocks.

For a laser enclosure to be put into administrative override, both Hutch-1 and the enclosure must be armed. 
The controls for the administrative overrides are on the enclosures LASER ENCLOSURE INTERLOCK protocase. 
Turn the key on the protocase under INERLOCK OVERRIDE from INTERLOCK TO OVERRIDE. 

Once the enclosure is put into override the following will change in the interlock system:

- The VIEWMARQ display will show ASTRELLA ADMIN OVERRIDE.
- The Hutch-1 Control and Hutch-1 protocase beacon stack orange administrative override LED will turn on.
- If you open the enclosure,  the laser warning module will still show DANGER LASER ON, the door monitor module will show CLOSED, and the local interlock modules for arming shuttters manual control will not disarm.

At this point, the LOCAL INTERLOCK CONTACT CONTROL local interlock modules can be armed, and the shutters can be controlled manually without the interlocks disarming manual usage. 

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_override.jpg
    :scale: 20 %
    :align: center

    **Figure 12:** Astrella enclosure override.


Disarming the Laser Interlock System
------------------------------------

To take the Astrella enclosure out of administrative override, simply change the INTERLOCK OVERRIDE key on the Astrella LASER ENCLOSURE INTERLOCK protocase back from OVERRIDE to INTERLOCK. 
Also, all the arming laser modules have disarming buttons where you can either disarm specific modules you no longer need, or you can disarm the room modules to auto-disarm their local modules. 
