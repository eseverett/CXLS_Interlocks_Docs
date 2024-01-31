.. role:: orange
.. role:: blue
.. role:: yellow

Vault-1 Laser Interlock System Testing Protocol
===============================================

The purpose of this testing procedure if the Verify the functionality of the Vault-1 laser interlock system including arming Vault-1 as a laser lab, the Pharos enclosure, and the Dira enclosure. 


Starting Conditions
-------------------

#. VIEWMARQ in Vault-1 Control displays :green:`LASER SAFE`.

#. Vault-1 beacon stacks show :green:`green` LED on.

    - Vault-1 Control.
    - Vault-1 east wall.
    - Pharos LASER ENCLOSURE INTERLOCK protocase.
    - Dira LASER ENCLOSURE INTERLOCK protoacse.

#. Vault-1 entry keypad LED for :green:`RELEASED` is on.

#. Vault-1 laser warning modules show :green:`LASER SAFE`.

    - Vault-1 Control.
    - Pharos enclosure south wall.
    - Pharos enclosure north wall.
    - Dira LASER ENCLOSURE INTERLOCK protoacse.

#. Laser control module shows :green:`LASER SAFE`.
   When the Vault-1 door is open, the module shows :orange:`ACCESS`.

#. Laser warning module on the Pharos LASER ENCLOSURE INTERLOCK protocase shows :red:`DANGER LASER ON`.

#. None of the laser E-stops are engaged or glowing. 

    - Pharos enclosure east wall.
    - Pharos enclosure north wall.
    - Dira enclosure east wall.
    - Dira enclosure west wall.

#. All room interlock modules LED for :greenL`ROOM DISABLED (READY TO ARM)` is on.

    - Vault-1.
    - Pharos enclosure.

#. Local interlock modules LEDs for :green:`LOCAL CONTACTS DISARMED`, and :green:`ROOM NOT ARMED - LOCAL CONTACTS CANNOT ARM` is on.

    - Pharos enclosure.
    - Dira LASER ENCLOSURE INTERLOCK protocase AUX #1.
    - Dira LASER ENCLOSURE INTERLOCK protocase AUX #2.

#. Local interlock modules LEDs for :green:`LOCAL CONTACTS DISARMED` are on.
 
    - Pharos LASER ENCLOSURE INTERLOCK protocase CONTROL #1.
    - Pharos LASER ENCLOSURE INTERLOCK protocase CONTROL #2.

#. Administrative override keys are set to INTERLOCK, with STATUS LED :green:`green`.

    - Pharos LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE.
    - Dira LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE.

#. Both enclosures are closed, and the Door / Curtain Monitors should show :green:`CLOSED`.

    - Pharos enclosure.
    - Dira enclosure.

#. Push before exit buttons is not on.

.. warning:: NEEDS IMAGES


Arming Vault-1 as a Laser Lab
-----------------------------

#. While inside of Vault-1 with the vault door latched, press ARM on the room interlock arming module.
   It should light the LED for :orange:`ROOM ARMED`, and there will be an audible chime. 

#. The laser control module shows :red:`DANGER LASER ON`.

#. The push to exit button is on.

#. The Vault-1 door is magnetically locked.

#. The VIEWMARQ display in Vault-1 Control displays :red:`DANGER LASER ON`.

#. Vault-1 laser warning modules display :red:`DANGER LASER ON`.

#. Entry keypad LED for :red:`INTERLOCKED` is on.

#. They in a random pin. 
   The Vault-1 door will not unlock.

#. Type in the correct pin and open the Vault-1 door.

#. The entry keypad LED for :green:`RELEASED` is on.

#. Vault-1 beacon stacks show no LEDs on.

    - Vault-1 Control.
    - Vault-1 east wall.
    - Pharos LASER ENCLOSURE INTERLOCK protocase.
    - Dira LASER ENCLOSURE INTERLOCK protocase.

#. Leave the vault door open for :red:`x seconds` and allow the system to trip.

    - The Vault-1 laser interlock system should return to its initial conditions.
    - The Vault-1 room arming module should show :orange:`ROOM CRASHED (CANNOT ARM)`, then :green:`ROOM DISABLED (READY TO ARM)` once the door is closed.

.. warning:: NEEDS IMAGES


Arming the Pharos Enclosure and Laser
-------------------------------------


#. With the Vault-1 unarmed, arm the room interlock module on the Pharos enclosure.

    - The room interlock module only lights the LED for :orange:`ROOM ARMED`.
    - The local interlock module will auto-arm only lights the LED for :orange:`LOCAL CONTACTS ARMED`.
    - The laser warning control module shows :red:`DANGER LASER ON`.

#. Laser E-stops buttons are on.

    - Pharos enclosure west wall
    - Pharos enclosure north wall

#. The VIEWMARQ in Vault-1 Control will display :green:`LASER SAFE` - :red:`PHAROS ARMED`.

#. Beacon stacks show :green:`green` and :blue:`blue` LEDs activated.

    - Vault-1 Control
    - Vault-1 east wall
    - Pharos LASER ENCLOSURE INTERLOCK protocase
    - Dira LASER ENCLOSURE INTERLOCK protocase

#. Change the Pharos LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from INTERLOCK to OVERRIDE. 
   The STATUS LED remains :green:`green`. Change back to INTERLOCK.

#. Rearm Vault-1 as a laser lab.

#. The VIEWMARQ in Vault-1 Control displays :red:`DANGER LASER HAZARD - PHAROS ARMED`.

#. Beacon stacks show :blue:`blue` LED activated.

    - Vault-1 Control
    - Vault-1 east wall
    - Pharos LASER ENCLOSURE INTERLOCK protocase
    - Dira LASER ENCLOSURE INTERLOCK protocase


Safe Pharos E-Stop Test
-----------------------

.. warning:: NEEDS IMAGES, need to develop this section.


Administrative Override on the Pharos Enclosure
-----------------------------------------------


#. With the Pharos and Vault-1 armed, arm the LOCAL INTERLOCK CONTACT CONTROL modules on the Pharos LASER ENCLOSURE INTERLOCK protocase.

    - CONTROL #1
    - CONTROL #2

#. Open the Pharos enclosure rolling doors. In response:

    - Pharos LASER ENCLOSURE INTERLOCK protocase laser warning module will display :green:`LASER SAFE`.
    - The LOCAL INTERLOCK CONTACT CONTROL modules will disarm and display :orange:`LOCAL CONTACTS DISARMED`.
    - Pharos LASER ENCLOSURE INTERLOCK protocase door monitor will display nothing.
    - Pharos UV and IR shutters will close.
    - Pharos UV and IR shutter controllers will display :red:`something`.

#. Rearm the contact controls manually.

    - East door
    - North door
    - South door

#. Turn the Pharos LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from :red:`INTERLOCK` to :red:`OVERRIDE`. 
   The STATUS LED changed to :red:`red`.

#. The VIEWMARQ in Vault-1 Control displays :red:`DANGER LASER HAZARD-PHAROS ARMED-PHAROS ADMIN OVERRIDE`.

#. Beacon stacks show :orange:`orange` and :blue:`blue` LEDs on.

    - Vault-1 Control
    - Vault-1 east wall
    - Pharos LASER ENCLOSURE INTERLOCK protocase

#. Beacon stack on Dira LASER ENCLOSURE INTERLOCK protocase only shows :blue:`blue` LED on.

#. Arm the LOCAL INTERLOCK CONTACT CONTROL modules on the Pharos LASER ENCLOSURE INTERLOCK protocase.

    - CONTROL #1
    - CONTROL #2

#. With the Pharos, Vault-1, and LOCAL INTERLOCK CONTACT CONTROL modules armed and the Pharos enclosure set to override, open one of the Pharos enclosure rolling doors. In response:

    - Pharos LASER ENCLOSURE INTERLOCK protocase laser warning module will display :red:`LASER ON`.
    - The LOCAL INTERLOCK CONTACT CONTROL modules will stay armed.
    - Pharos LASER ENCLOSURE INTERLOCK protocase door monitor will display :red:`CLOSED`.
    - Pharos UV and IR shutters will not close.
    - Pharos UV and IR shutter controllers will display :red:`something different`.

#. Turn the Pharos LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from :red:`OVERRIDE` to :red:`INTERLOCK`. 
   The STATUS LED changed to :green:`green`. 
   The VIEWMARQ display and beacon stacks show a non-override status.


.. warning:: NEEDS IMAGES


Arming the Dira Enclosure and Laser
-----------------------------------

#. Disarm Vault-1 and the Pharos.

#. See Laser Lab testing procedure for arming the Dira. 
   The laser warning module on Dira enclosure displays DANGER LASER ON.

#. Change the Dira LASER ENCLOSURE INTERLOCK protocase INTERLOCK OVERRIDE key from INTERLOCK to OVERRIDE. 
   The STATUS LED remains green. Change back to INTERLOCK.


Administrative Override on the Dira Enclosure
---------------------------------------------

#. Open the Dira enclosure rolling doors. 
   In response:

    - Dira and Pharos LASER ENCLOSURE INTERLOCK protocase laser warning module will display :green:`LASER SAFE`
    - The LOCAL INTERLOCK CONTACT CONTROL modules will disarm and display :orange:`LOCAL CONTACTS DISARMED` on the Dira and Pharos protocases.
    - Dira and Pharos LASER ENCLOSURE INTERLOCK protocase door monitor will display nothing.
    - Pharos UV and IR shutters will close.
    - Dira will lose power.
    - Pharos UV and IR shutter controllers will display :red:`something`.

#. Rearm the Dira.

#. With Vault-1, the Dira armed, and the Pharos armed turn the INTERLOCK OVERRIDE key on the Dira LASER ENCLOSURE INTERLOCK protocase from :red:`INTERLOCK` to :red:`OVERRIDE`. 
   The STATUS LED will change to :red:`red`.

#. The VIEWMARQ displays :red:`DANGER LASER HAZARD-PHAROS ARMED-DIRA ARMED-DIRA ADMIN OVERRIDE`.

#. Beacon stacks show :orange:`orange`, white, and :blue:`blue` LEDs on.

    - Vault-1 Control
    - Vault-1 east wall
    - Dira LASER ENCLOSURE INTERLOCK protocase.

#. Beacon stack on the Pharos LASER ENCLOSURE INTERLOCK protocase will show :blue:`blue` LEDs on.

#. Turn the INTERLOCK OVERRIDE key on the Pharos LASER ENCLOSURE INTERLOCK protocol case from :red:`INTERLOCK` to :red:`OVERRIDE`. The STATUS LED will change to :red:`red`.

#. The VIEWMARQ in Vault-1 Control will display :red:`DANGER LASER ON - PHAROS ARMED - DIRA ARMED - PHAROS ADMIN OVERRIDE - DIRA ADMIN OVERRIDE`.

#. The beacon stack on the Pharos LASER ENCLOSURE INTERLOCK protocase will show :orange:`orange` and :blue:`blue` LEDs on.

#. With the Pharos, Dira, Vault-1, and LOCAL INTERLOCK CONTACT CONTROL armed and the Dira and Pharos enclosures set to override, open one of the Dira enclosure rolling doors. 
   In response:

    - Pharos LASER ENCLOSURE INTERLOCK protocase laser warning module will display :red:`DANGER LASER ON`
    - The LOCAL INTERLOCK CONTACT CONTROL modules will disarm on the Pharos.
    - Pharos UV and IR shutters will not close.
    - Pharos UV and IR shutter controllers will display :red:`something different`.

#. With the Pharos, Dira, and Vault-1 armed and the Dira and Pharos enclosures set to override, open one of the Dira enclosure rolling doors. 
   In response:

    - Dira LASER ENCLOSURE INTERLOCK protocase warning module will display :red:`DANGER LASER ON`.
    - Dira LASER ENCLOSURE INTERLOCK protocase door monitor will display :red:`CLOSED`.
    - Pharos LASER ENCLOSURE INTERLOCK protocase door monitor will display nothing.
    - Pharos UV and IR shutters will close.


Crashing the Pharos Laser
-------------------------

#. Once every 6 months, the Pharos laser emergency stop buttons are tested that they can successfully cut power to the Pharos from a functional state. 
   Verify if the last testing date was 6 months ago.
 
#. If 6 months have passed, arm the Pharos laser, and use one of the laser e-stops to crash the laser and verify that power has been cut. 


Return to Starting Conditions
-----------------------------

#. Return the Vault-1 laser interlock system back to starting conditions. 


