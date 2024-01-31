.. role:: orange


Laser-1 Interlock System Testing Protocol
=========================================

The purpose of this protocol is the Laser-1 laser interlocks.


Starting Conditions
-------------------

#. The Vault-1 Control VIEWMARQ does not display :red:`DIRA ARMED - DIRA ADMINISTRATIVE OVERRIDE`.

#. The Vault-1 beacon stacks show only green LEDs on.

    - Vault-1 Control
    - Vault-1 east wall
    - Pharos LASER ENCLOSURE INTERLOCK protocase
    - Dira LASER ENCLOSURE INTERLOCK protocase

#. Dira enclosure e-stops are not engaged, and the LEDs are off.

    - East wall
    - West wall

#. The Laser Lab VIEWMARQs display :green:`LASER SAFE`.

    - Laser-1 entrance.
    - Laser-1 airlock.

#. Laser warning module in Laser-1 entrance shows :green:`LASER SAFE`.

#. Entry keypad has :green:`RELEASE` LED on.

#. Control module in Laser-1 airlock shows :green:`LASER SAFE`.

#. Push to exit module is not on.

#. Laser-1 -estops are not engaged and LEDs are off.

    - Laser-1 south-West
    - Laser-1 north-West
    - Laser-1 north
    - Laser-1 east

#. Laser-1 room interlock module has LED on for :green:`ROOM DISARMED (READY TO ARM)`.

#. All local interlock modules have LEDs on for :green:`LOCAL CONTACTS DISARMED` and :green:`ROOM NOT ARMED - LOCAL CONTACT CANNOT ARM`.

#. All local interlock modules have LEDs on for :green:`LOCAL CONTACT DISARMED` and :green:`ROOM NOT ARMED - LOCAL CONTACT CANNOT ARM`.

    - Dira
    - AUX 1
    - AUX 2
    - AUX 3
    - AUX 4

#. Door closure module next to RF-1 / Laser-1 door displays :green:`CLOSED`.

.. warning:: NEEDS IMAGES



Arming Laser-1
--------------

#. When entering Laser-1, there should be an audible chime.

#. Attempt to arm all the local interlock modules before arming Laser-1. 
   The Dira will not arm.

#. Arm the Laser-1 room control interlock module. 
   Laser-1 room interlock module has LED on for :orange:`ROOM ARMED`.

#. All local interlock modules have LEDs on for :green:`LOCAL CONTACTS DISARMED`.

    - Dira
    - AUX 1
    - AUX 2
    - AUX 3
    - AUX 4

#. VIEWMARQ displays show :red:`DANGER LASER ON`.

    - Laser-1 entrance.
    - Laser-1 airlock.

#. Dira LASER ENCLOSURE INTERLOCK protocase laser wrning module shows :red:`DANGER LASER ON`.

#. Dira LASER ENCLOSURE INTERLOCK protocase CONTROL CONTACTS AUX #1 and #2 should be auto-armed from arming Laser-1.
   They cannot be disarmed. 

#. Laser warning module displays :red:`DANGER LASER ON`.

#. Entry keypad has LED on for :green:`INTERLOCKED`.

#. Laser control module displays :red:`DANGER LASER ON`.

#. The push to exit button is on.

#. The airlock / corridor door is magnetically locked.

#. Use the push to exit button to leave Laser-1.

#. Use a random pin on the entry keypad module and scan your badge.
   The door should remain locked.

#. Use the correct pin and scan your badge.
   Hold the door open for :red:`x seconds` and allow the interlock system to trip.
   The system should return to a completely disarmed state. 

.. warning:: NEEDS IMAGES


Arming the Dira
---------------

#. Arm the Dira local interlock module. 
   Dira local interlock module has LED on for :orange:`LOCAL CONTACTS ARMED`.

#. The VIEWMARQ display in Laser-1 airlock :red:`DANGER LASER ON - IR EYE PROTECTION REQUIRED`.

#. The VIEWMARQ display in the Laser-1 entrance shows :red:`DANGER LASER ON - IR HAZARD`.

#. The VIEWMAEQ display in Vault-1 Control shows :green:`LASER SAFE` - :red:`DIRA ARMED`.

#. The Vault-1 beacon stacks should show green and white LEDs on.

    - Vault-1 control.
    - Vault-1 east wall.
    - Dira LASER ENCLOSURE INTERLOCK protocase.

#. Beacon stack on the Pharos LASER ENCLOSURE INTERLOCK protocase will only have a :green:`green` LED on.

#. Dira LASER ENCLOSURE INTERLOCK protocase laser warning module shows :red:`DANGER LASER ON`.

.. warning:: NEEDS IMAGES

Safe Dira E-Stop Test
---------------------

.. warning:: This section now needs to be completely developed.


RF-1 Door
---------

#. With the Dira not armed, open the door between RF-1 and Laser-1.
   The door monitor module should display nothing.


Crashing the Dira
-----------------

#. Once every 6 months, the Dira laser emergency stop buttons are testing that they can successfully cut power to the Dira from a fully armed state.
   Verify if the last testing date was 6 months ago. 

#. If 6 months have passed, arm the Dira laser and use one of the Dira laser e-stops to cut power from the Dira in an armed state.
