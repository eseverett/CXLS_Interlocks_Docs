.. defining roles to make color classes work
.. role:: blue
.. role:: yellow
.. role:: orange

Hutch-1 Ionizing Radiation Interlock System Testing Protocol
============================================================

The objective of this testing procedure is to verify the functionality of the Hutch-1 ionizing radiation interlock system. 
The following fall under the scope of this testing procedure: 

- Hutch-1 search and securing system. 
- Trouble tungsten shutter control. 
- Ionizing radiation monitoring interlocks.


Starting Conditions
------------------- 

The default state for testing of the Hutch-1 ionizing radiation interlock system is in a completely disarmed state.

#. Search button LEDs are off in Hutch-1. 

    - Button 1
    - Button 2
    - Button 3

#. The following Hutch-1 Control Ionizing Radiation Interlock protocase lamps are :red:`red`.

    - SECURE PERIMETER
    - BEAM SELECT
    - BEAM STOP

#. THe following Hutch-1 Control Ionizing Radiation Interlock protocase lamps are :green:`green`.

    - AREA MONITOR
    - BEAM status

#. Hutch-1 Control Ionizing Radiation Interlock protocase BEAM SELECT key is set to DIVERGENT.
#. Hutch-1 Control VIEWMARQ displays :green:`LASER SAFE`.
#. There is no 24VDC across the :blue:`blue` and :yellow:`yellow` contact blocks in Hutch-1 panel for the double tungsten shutters.

    - Set 1
    - Set 2

#. The double tungsten shutters are in the closed position.


.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_protocase.jpg
   :align: center
   :scale: 20 %

   **Figure 1:** Hutch-1 Control Ionizing Radiation Interlock protocase.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
   :align: center
   :scale: 20 %

   **Figure 2:** Hutch-1 search button LEDs are off.

.. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
   :align: center
   :scale: 20 %

   **Figure 3:** Hutch-1 search button LEDs are on.

.. figure:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_1.jpg
   :align: center
   :scale: 92 %

   **Figure 4:** Hutch-1 double tungsten shutter contact set 1.

.. figure:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_2.jpg
   :align: center
   :scale: 92 %

   **Figure 5:** Hutch-1 double tungsten shutter contact set 2.


Search Procedure
----------------

#. Push search buttons three and two in Hutch-1 and verify they will not activate without going in the correct sequence.

    - Button 3
    - Button 2

#. Go through Hutch-1 and in the correct sequence, click the three search buttons. The LED on the search button should turn on and the corresponding lamp on the Hutch-1 Ionizing Radiation interlock protocase should turn :green:`green`.

    - Button 1
    - Button 2
    - Button 3

#. When the third search button is hit, there is an audible chime. 

#. #. Once all three search buttons have been hit in order, close the shield door. The Hutch-1 Control Ionizing Radiation Interlock protocase shield door lamp turns :green:`green`.

#. The Hutch-1 Control Ionizing Radiation Interlock protocase Beam Select Divergent lamp turns :green:`green`. 

.. warning::
    NEED IMAGES


Changing Beam status
--------------------

#. Turn the Hutch-1 Control Ionizing Radiation Interlock protocase Beam Stop key to Open. 
   The Beam Stop lamp turn :green:`green`.

#. The Hutch-1 Control Ionizing Radiation Interlock protocase Beam Status Collimated lamp turn :red:`red`.

#. Change the Hutch-1 Ionizing Radiation Interlock protocase Beam Select key to Collimated.

    - The Beam Select Divergent lamp turn :red:`red`.
    - The Beam Select Collimated lamp turn :green:`green`.
    - The Status Divergent lamp turns :red:`red`.
    - The Beam Status Collimated lamp turn :orange:`orange` while the shutter is moving, and then turns :green:`green` when the shutter is closed. 
    - Verify that the shutters are physically closed.

#. Change the Beam Select key back to Divergent. The inverse of step three should occur. 

    - The Beam Select Collimated lamp turns :red:`red`.
    - The Beam Select Divergent lamp turns :green:`green`.
    - The Beam Status Collimated lamp turns :red:`red`.
    - The Beam Status Divergent lamp turns :orange:`orange` while the shutter is moving, and then turns :green:`green` when the shutter is closed.
    - Verify that the shutters are physically closed.

#. Press the Reset button. 
   All Hutch-1 Control Ionizing Radiation Interlock protocase Beam Status lamps are :green:`green`.
   Verify the shutters are physically in the correct position.

.. warning::
    NEED IMAGES

Returning to Starting Conditions
--------------------------------

#. Return the Hutch-1 ionizing radiation interlock system back to starting conditions. 