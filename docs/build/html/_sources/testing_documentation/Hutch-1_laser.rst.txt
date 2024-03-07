.. roles defined to use custom css classes
.. role:: orange
.. role:: yellow
.. role:: blue
.. role:: red
.. role:: green
.. role:: white-cell

Hutch-1 Laser Interlock System Testing Protocol
===============================================

The purpose of this document is to describe the testing protocol for the Hutch-1 laser interlock system including the interlocks for the Astrella laser and enclosure. 

-----

Starting Conditions
-------------------

#. VIEWMARQ in Hutch-1 Control displays :green:`LASER SAFE`.

#. Beacon Stacks have :green:`green` LED on.

    - Hutch-1 Control.
    - Astrella LASER ENCLOSURE INTERLOCK protocase.

#. Hutch-1 Control Entry keypad LED shows :green:`RELEASED`. 

#. Hutch-1 Control laser warning modules show :green:`LASER SAFE`.

    - Hutch-1 Control.
    - Astrella enclosure south wall.
    - Astrella enclosure west wall.

#. Hutch-1 Laser control module shows :green:`LASER SAFE`.
   The module will show :orange:`ACCESS` when the door is open.

#. The laser warning module on the Astrella LASER ENCLOSURE INTERLOCK protocase shows :red:`DANGER LASER ON`.

#. None of the Astrella laser e-stops are on.

    - Astrella enclosure outside south wall.
    - Astrella enclosure outside west wall.
    - Astrella enclosure inside south wall.
    - Astrella enclosure inside west wall.
    - Astrella enclosure inside east wall.
    - Hutch-1 experimental chamber.

#. All room interlock modules light the LED for :green:`ROOM DISABLED (READY TO ARM)`.

    - Hutch-1.
    - Astrella enclosure.

#. Local interlock modules light the LEDs for :green:`LOCAL CONTACTS DISARMED`, and :green:`ROOM NOT ARMED - LOCAL CONTACTS CANNOT ARM`.

    - Astrella enclosure.
    - Astrella LASER ENCLOSURE INTERLOCK protocase CONTROL #1.
    - Astrella LASER ENCLOSURE INTERLOCK protocase CONTROL #2.

#. Astrella LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE panel is set to interlock.

    - Administrative override key is set to INTERLOCK.
    - STATUS lamp is :green:`green`.

#. All Astrella enclosure curtain doors are closed, and the Door / Curtain Monitor should show :green:`CLOSED`.

    - West enclosure door 1.
    - West enclosure door 2.
    - North enclosure door 1.
    - North enclosure door 2.
    - East enclosure door 1.
    - East enclosure door 2.

#. Push before exit button is not on. 


.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_VIEWMARQ_laser_safe.jpg
    :align: center
    :scale: 20 %

    **Figure 1:** Hutch-1 Control VIEWMARQ showing LASER SAFE.

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_entry_disarmed.jpg
    :align: center
    :scale: 20 %

    **Figure 2:** Hutch-1 Control Entry Keypad showing RELEASED.

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_unarmed.jpg
    :align: center
    :scale: 20 %

    **Figure 3:** Hutch-1 Control showing all room interlock modules disabled.

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_enclosure_unarmed.jpg
    :align: center
    :scale: 20 %

    **Figure 4:** Astrella enclosure showing all local interlock modules disarmed.

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_protocase.jpg
    :align: center
    :scale: 20 %

    **Figure 5:** Astrella LASER ENCLOSURE INTERLOCK protocase showing the INTERLOCK OVERRIDE panel set to INTERLOCK.

.. figure:: /images/user_docs/Vault-1_laser/laser_e-stop_off.jpg
    :align: center
    :scale: 20 %

    **Figure 6:** Astrella enclosure showing all e-stops off.


-----

Arming Hutch-1 as a Laser Lab
-----------------------------


#. While inside of Hutch-1, close the first curtain and press ARM on the Hutch-1 room interlock control module. It lights the LED for :orange:`ROOM ARMED`.

#. The laser control module shows DANGER LASER ON.

#. The Push Before Exit button is on.

#. The curtain door is locked magnetically locked.

#. Close the second curtain door. Verify that the second curtain door chimes when opened.

#. Use the Push Before Exit button to leave the Hutch, as you leave there is a chime sounding.

#. VIEWMARQ in Hutch-1 Control displays :red:`DANGER LASER HAZARD`.

#. Hutch-1 Control laser warning modules display :red:`DANGER LASER ON`.

#. Beacon stacks show no LEDs on.

    - Hutch-1 Control.
    - Astrella LASER ENCLOSURE INTERLOCK protocase.

#. Entry keypad lights the LED for :red:`INTERLOCKED`.

#. Type a random pin into the entry keypad. 
   The curtain door remains locked.

#. Type in the pin to open the Hutch curtain door.
#. Keypad module lights the LED for :green:`RELEASED`.

#. Leave the curtain door open and allow the system to trip. It should trip in :red:`x seconds/minutes`.

    - The Hutch-1 room arm module shows :orange:`ROOM CRASHED (CANNOT ARM)`, then :green:`ROOM DISARMED (READY TO ARM)`.
    - Hutch-1 is now in starting conditions.


.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_VIEWMARQ_laser_hazard.jpg
    :align: center
    :scale: 20 %

    **Figure 7:** Hutch-1 Control VIEWMARQ showing DANGER LASER HAZARD.

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_armed.jpg
    :align: center
    :scale: 20 %

    **Figure 8:** Hutch-1 Control showing the room interlock module armed.

.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_entry_armed.jpg
    :align: center
    :scale: 20 %

    **Figure 9:** Hutch-1 Control Entry Keypad showing INTERLOCKED.

-----

Arming the Astrella Enclosure and Laser 
---------------------------------------

#. Attempt to arm the Astrella by arming local room interlock module on the Astrella enclosure before arming the room module. 
   Astrella does not arm.

#. With Hutch-1 unarmed, arm the room interlock module on the Astrella enclosure. 

#. The room interlock module only lights the LED for :orange:`ROOM ARMED`. 

#. The local interlock module only lights the LED for :green:`LOCAL CONTACT DISARMED`. 

#. The laser warning control module shows :red:`LASER ON`.

#. Laser E-stops buttons should be on.

    - Outside enclosure south
    - Outside enclosure west
    - Experimental Chamber
    - Inside enclosure south
    - Inside enclosure east
    - Inside enclosure west 

#. Arm the local room interlock module on the Astrella enclosure. 
   The local interlock module only lights the LED for :green:`LOCAL CONTACTS ARMED`. 

#. VIEWMARQ in Hutch-1 Control displays :green:`LASER SAFE - ASTRELLA ARMED`.

#. Beacon stacks show green and white LEDs on.
    - Hutch-1 Control
    - Astrella LASER ENCLOSURE INTERLOCK protocase

#. Go through all Astrella enclosure curtain doors and open them one at a time. 
   In response:

    - The Astrella enclosure laser warning module displays :green:`LASER SAFE`. 
    - The Door/Curtain Monitor shows nothing. 
    - "MANUAL INTERLOCK OPEN" is flashing on the shutter controller. 
    
        - West enclosure door 1 
        - West enclosure door 2
        - North enclosure door 1
        - North enclosure door 2
        - East enclosure door 1
        - East enclosure door 2 

#. Arm CONTROL #1 local interlock module. 
   It lights the LED for :green:`LOCAL CONTACTS ARMED`. 

#. Open the Astrella enclosure, the system trips, and the local interlock module lights the LEDs for :green:`LOCAL CONTACTS DISARMED`, and :green:`ROOM NOT ARMED - LOCAL CONTACT CANNOT ARM`.

.. #. Rearm the Astrella enclosure only and go through each laser e-stop and push them. 
..    In response:

..     - E-stop turns off.
..     - Astrella enclosure room interlock module lights the LED for :orange:`ROOM CRASHED (CANNOT ARM)`.
..     - Laser warning module on the Astrella enclosure is slowly flashing :green:`LASER SAFE`.
..     - Once e-stop is unengaged the Astrella enclosure will return to unarmed condition
..         - Outside enclosure south
..         - Outside enclosure west
..         - Experimental Chamber
..         - Inside enclosure south
..         - Inside enclosure east
..         - Inside enclosure west 

#. Rearm Hutch-1 as a laser lab and rearm the Astrella. 
   All laser warning modules display :red:`DANGER LASER ON`.

#. VIEWMARQ in Hutch-1 Control displays :red:`DANGER LASER HAZARD - ASTRELLA ARMED`.

#. Beacon stacks show white LED on.

    - Hutch-1 Control
    - Astrella LASER ENCLOSURE INTERLOCK protocase



.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_VIEWMARQ_laser_hazard_armed.jpg
    :align: center
    :scale: 20 %

    **Figure 10:** Hutch-1 Control VIEWMARQ showing DANGER LASER HAZARD - ASTRELLA ARMED.



.. figure:: /images/user_docs/Hutch-1_laser/Astrella_enclosure_armed.jpg
    :align: center
    :scale: 20 %

    **Figure 11:** Astrella enclosure showing the room interlock module armed.


-----

Administrative Override on the Astrella Enclosure
-------------------------------------------------

#. Turn the Astrella LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from INTERLOCK to OVERRIDE. 
   The STATUS lamp will not change.

#. With Hutch and Astrella armed, turn the Astrella LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from INTERLOCK to OVERRIDE. 
   The STATUS lamp turns :red:`red`.

#. VIEWMARQ in Hutch-1 Control displays :red:`DANGER LASER HAZARD - ASTRELLA ARMED - ASTRELLA ADMIN OVERRIDE`.

#. Beacon stacks show white and :orange:`orange` LEDs activated.

    - a. Hutch-1 Control
    - b. Astrella LASER ENCLOSURE INTERLOCK protocase

#. Open the Astrella enclosure door. 
   The laser warning module displays :red:`DANGER LASER ON`, and the Door/Curtain Monitor shows :green:`CLOSED`.

#. Close the Astrella enclosure and arm CONTROL #1 local interlock module, it lights the LED for :orange:`LOCAL CONTACTS ARMED`.

#. Open the Astrella enclosure. "MANUAL\_" is flashing on the shutter controller.


.. figure:: /images/user_docs/Hutch-1_laser/Hutch-1_VIEWMARQ_override.jpg
    :align: center
    :scale: 20 %

    **Figure 12:** Hutch-1 Control VIEWMARQ showing DANGER LASER HAZARD - ASTRELLA ARMED - ASTRELLA ADMIN OVERRIDE.

.. figure:: /images/user_docs/Hutch-1_laser/Astrella_override.jpg
    :align: center
    :scale: 20 %

    **Figure 13:** Astrella enclosure showing the INTERLOCK OVERRIDE panel set to OVERRIDE.


-----

Safe Astrella E-Stop Test
-------------------------

#. Put the Astrella into a powered down state.

#. Arm the Astrella and Astrella enclosure. 

#. Press one of the Astrella enclosure e-stops. 

#. Verify that the Astrella power supply is cut off.


-----

Crashing the Astrella
---------------------

#. Once every 6 months, the Astrella laser emergency stop buttons are testing that they can successfully cut power to the Astrella from a functional state.
   Verify if the last testing date was 6 months ago.

#. If 6 months have passed, arm the Astrella laser and use one the the Astrella laser e-stop to crash the laser and verify that power has been cut. 

-----

Return to Starting Conditions
-----------------------------

#. Return the Hutch-1 laser interlock system back to starting conditions. 