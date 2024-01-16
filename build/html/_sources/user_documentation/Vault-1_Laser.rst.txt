Vault-1 Laser Interlock System User Manual
==========================================

For the Vault-1 laser interlocks system, there are multiple indicators that inform you of the state of the systems. 
This includes status beacons, LED display, and interlock warning modules.


Protocases
----------

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
-------------

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
----------------

There is a VIEWMARQ display in Vault-1 Control that states the status of potential laser hazards in Vault-1. 
This display will notify you if Vault-1, the Pharos, or the Dira is armed. 
Also, it will notify you if the Pharos, the Dira, or both laser enclosures are in administrative override. 

+------------------------------------------------------------------+----------------------------------------------------+
| VIEWMARQ Display Notes                                           | VIEWMARQ Display Text                              |
+==================================================================+====================================================+
| This line states if Vault-1 is armed as a laser lab or not.      | :green:`LASER SAFE` / :green:`DANGER LASER HAZARD` |
+------------------------------------------------------------------+----------------------------------------------------+
| This line states which laser is armed.                           | :red:`PHAROS ARMED            DIRA ARMED`          |
+------------------------------------------------------------------+----------------------------------------------------+
| This line states if the Dira is in administrative override.      | :red:`DIRA ADMIN OVERRIDE`                         |
+------------------------------------------------------------------+----------------------------------------------------+
| This line states you if the Pharos is in administrative override.| :red:`PHAROS ADMIN OVERRIDE`                       |
+------------------------------------------------------------------+----------------------------------------------------+