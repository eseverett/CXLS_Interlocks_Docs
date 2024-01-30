.. defining roles for custom css classes that are not working without role definition
.. role:: blue
.. role:: orange

Vault-1 Ionzing Radiation Interlock Testing Protocol
====================================================

The objective of this testing procedure is to verify the functionality of the Vault-1 ionizing radiation interlock system.
The following fall under the scope of this testing procedure:

- Vault-1 search and securing system.
- RF and accelerator arming.
- Transmitter override.
- Ionizing radiation monitoring interlocks.


Starting Conditions
-------------------

The default state for testing of the Vault-1 ionizing radiation interlock system is in a completely disarmed state.

#. The IONIZING RADIATION INTERLOCK protocase in Vault-1 Control shows:

    - All SECURE PERIMETER lamps are :red:`red`.
    - All AREA MONITOR lamps are :green:`green`.
    - TRANSMITTERS and ACCERATOR lamps are :red:`red`.

#. VIEWMARQ in Vault-1 Control displays :green:`LASER SAFE`.
#. VIEWMARQ in Accererator Lab disaplys :green:`RF SAFE`.
#. All individual :red:`red`, :blue:`blue`, and :orange:`orange` beacons are off.

#. Search buttons LEDs are off in Vault-1.

    - Button 1
    - Button 2
    - Button 3

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 search buttons off

   Vault-1 search buttons off

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 search buttons on

   Vault-1 search buttons on

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 protocase

   Vault-1 protocase



Testing Unsecure Vault-1 Conditions
-----------------------------------

#. Switch the ENABLE key for the accelerator. 
   The accelerator lamp remains :red:`red`.
#. Swith the ENABLE keys for transmitters 1 and 2.
   Both transmitter lamps remain :red:`red`.


Searching Procedure
-------------------

#. Push search buttons three and two and verify they will not activate without going in the correct sequence. 

    - Button 3
    - Button 2

#. Go through the vault and in sequence, click the three search buttons. 
   The LED on the search button should glow and the corresponding lamp on the Vault-1 Control IONIZING RAIDATION INTERLOCK protocase should turn :green:`green`.

    - Button 1
    - Button 2
    - Button 3
    
#. When the third search button is hit, a chime should be audible.

#. Once all three search buttons have been hit in order, close the shield door. 
   The shield door lamp on the Vault-1 Control IONZING RADIATION INTERLOCK protocase will turn green once the mechanical door switches are fully actuated.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_searched.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 searched

   Vault-1 searched

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_door.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 door

   Vault-1 door

Arming the Accererator and transmitters
---------------------------------------

#. With the shield door still closed, enable the accelerator on the Vault-1 Control IONIZING RADIATION INTERLOCK protocase using the ENABLE key.
   The accelerator status lamp should turn :green:`green`.

#. Turn the ENABLE key for transmitter 1 on the Vault-1 Control IONIZING RADIATION INTERLOCK protocase.
   The transmitter 1 status lamp should turn :green:`green`.

#. Once the transmitter is enabled, the VIEWMARQ diaplys will show :red:`VAULT SECURE - RF ARMED`.

    - Vault-1 Control
    - Accererator Lab

#. The :blue:`blue` beacons next to each VIEWMARQs are on.

    - Vault-1 Control
    - Accererator Lab

#. Hit the reset button and repeat 2-4 with transmitter 2.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_accelerator_armed.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 protocase accelerator armed

   Vault-1 protocase accelerator armed

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_transmitter_armed.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 protocase transmitter armed

   Vault-1 protocase transmitter armed

.. warning::
   NEEDS VIEMARQ IMAGES

Overriding and Reseting Transmitters and Accererator
----------------------------------------------------

#. With the accelerator and transmitters aremed, swithc the OVERRIDE keys on the Vault-1 Control IONIZING RADIATION INTERLOCK protocase.
   The TRANSMITTERS lamps will turn :orange:`orange`.

#. Switch the OVERRIDE keys back to interlock. 
   The TRANSMITTERS lamps will turn :green:`green`.

#. Hit the reset button on the Vault-1 Control IONIZING RADIATION INTERLOCK protocase.
   The ACCELERATOR and TRANSMITTERS lamps will turn :red:`red`.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_protocase_transmitter_override.jpg
   :scale: 20 %
   :align: center
   :alt: Vault-1 protocase transmitter override

   Vault-1 protocase transmitter override


Timing out the Shield Door and Search sequence
----------------------------------------------

#. Rearm the accelerator and transmitters and open the shield door.
   The accelerator and transmitter lamps should turn :red:`red`.

#. Push only the first search button. 
   After :red:`x` seconds, the button LED should turn off.

#. Go through the search procedure again except do not close the shield door and allow the system to trip.
   After :red:`x`, the search lamps should turn :red:`red`.




Return to Starting Conditions
-----------------------------

#. Return Vault-1 ionizing radiation interlock system to the default state.