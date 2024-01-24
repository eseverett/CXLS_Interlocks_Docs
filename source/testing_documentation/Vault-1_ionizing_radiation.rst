.. defining roles for custom css classes that are not working without role definition
.. role:: blue
.. role:: orange

Vault-1 Ionzing Radiation Interlock Testing Protocol
====================================================

The objective of this testing procedure is to verify the funcationality of the Vault-1 ionizing radiation interlock system.
The following fall under the scope of this testing procedure:
- Vault-1 search and securing system.
- RF and accelerator arming.
- Tranmitter override.
- Ionzing radiation monitoring interlocks. 

Starting Conditions
-------------------

The default state for testing of the Vaut-1 ionizing radiation interlock system is in a completely disarmed state.

#. The IONIZING RADIATION INTERLOCK protocase in Vault-1 Control shows:

    - All SECURE PERIMETER lamps are :red:`red`.
    - All AREA MONITOR lamps are :green:`green`.
    - TRANSMITTERS and ACCERATOR lamps are :red:`red`.

#. VIEWMARQ in Vault-1 Control displays :green:`LASER SAFE`.
#. VIEWMARQ in Accererator Lab disaplys :green:`RF SAFE`.
#. All individual :red:`red`, :blue:`blue`, and :orange:`orange` beacons are off.

#. Search buttons LEDs are off in Vault-1.

    - 1
    - 2
    - 3

.. warning:: 
    search buttons and protocase images

Testing Unsecure Vault-1 Conditions
-----------------------------------

#. Switch the ENABLE key for the accelerator. 
   The accelerator lamp remains :red:`red`.
#. Swith the ENABLE keys for transmitters 1 and 2.
   Both transmitter lamps remain :red:`red`.


Searching Procedure
-------------------

#. Push search buttons three and two and verify they will not activate without going in the correct sequence. 

    - 3
    - 2

#. Go through the vault and in sequence, click the three search buttons. 
   The LED on the search button should glow and the corresponding lamp on the Vault-1 Control IONIZING RAIDATION INTERLOCK protocase should turn :green:`green`.

    - 1
    - 2
    - 3
    
#. When the third search button is hit, a chime should be audible.

#. Once all three search buttons have been hit in order, close the shield door. 
   The shield door lamp on the Vault-1 Control IONZING RADIATION INTERLOCK protocase will turn green once the mechanical door switches are fully actuated.

