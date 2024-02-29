.. defining roles to make color classes work
.. role:: blue
.. role:: yellow
.. role:: orange
.. role:: white-cell

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

.. .. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
..    :align: center
..    :scale: 20 %

..    **Figure 2:** Hutch-1 search button LEDs are off.

.. .. figure:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
..    :align: center
..    :scale: 20 %

..    **Figure 3:** Hutch-1 search button LEDs are on.

.. list-table::
   :align: center
      
   * - .. image:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_off.jpg
            :scale: 20 %
            :align: center

     - .. image:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_search_on.jpg
            :scale: 20 %
            :align: center

   * - Hutch-1 search button off. :white-cell:`============================================================`
     - Hutch-1 search button on. :white-cell:`=============================================================`
       
.. table-caption::
    **Figure 2:** This is an example of the Hutch-1 search buttons in both states.


.. .. figure:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_1.jpg
..    :align: center
..    :scale: 92 %

..    **Figure 4:** Hutch-1 double tungsten shutter contact set 1.

.. .. figure:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_2.jpg
..    :align: center
..    :scale: 92 %

..    **Figure 5:** Hutch-1 double tungsten shutter contact set 2.


.. list-table:: 
    :align: center

    * - .. image:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_1.jpg
            :scale: 92 %
            :align: center

      - .. image:: /images/testing_documentation/Hutch-1_ionizing_radiation/shutter_contacts_2.jpg
            :scale: 92 %
            :align: center

    * - Hutch-1 double tungsten shutter contact set 1. :white-cell:`============================================`
      - Hutch-1 double tungsten shutter contact set 2. :white-cell:`============================================`

.. table-caption::
    **Figure 3:** These are the contract blocks for the double tungsten shutters in the Hutch-1 aggregator panel.
    The specific sets being referenced here are the blue and yellow contact blocks next to the red IDEM relays. 
    If there is 24VDC across these contact blocks, the shutters are open.


.. list-table::
    :align: center

    * - .. image:: /images/testing_documentation/Hutch-1_ionizing_radiation/double_tungsten_shutter.jpg
            :scale: 20 %
            :align: center

      - .. image:: /images/testing_documentation/Hutch-1_ionizing_radiation/double_tungsten_shutter_zoom.jpg
            :scale: 20 %
            :align: center

    * - This is the upright double tungsten shutter. :white-cell:`===============================================`
      - This is a zoomed in image of the upright double tungsten shutter. 
        It can be seen here that the contact plate is on the bottom sensors. :white-cell:`====`

.. table-caption::
    **Figure 4:** This is the upright double tungsten shutter, and an example of this shutter being in the closed position.
    If the plate where to be on the top sensors, the shutters would be open.
    Additionally, the other double tungsten shutter is rotated 180 degrees from this one, which can be seen in the first image as the closer shutter only shows its top.
    Because it is rotated, the contact on the upper sensors is the closed position for the other shutter. 

Search Procedure
----------------

#. Push search buttons three and two in Hutch-1 and verify they will not activate without going in the correct sequence.

    - Button 3
    - Button 2

#. Go through Hutch-1 and in the correct sequence, click the three search buttons. The LED on the search button should turn on and the corresponding lamp on the Hutch-1 Ionizing Radiation interlock protocase should turn :green:`green`.

    - Button 1
    - Button 2
    - Button 3

#. When the third search button is hit, there will be an audible chime and a flashing light. 

#. Once all three search buttons have been hit in order, close the shield door. The Hutch-1 Control Ionizing Radiation Interlock protocase shield door lamp turns :green:`green`.

#. The Hutch-1 Control Ionizing Radiation Interlock protocase Beam Select Divergent lamp turns :green:`green`. 

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_searched.jpg
    :scale: 20 %
    :align: center

    **Figure 5:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase when Hutch-1 is searched.

.. figure:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_door.jpg
    :scale: 20 %
    :align: center

    **Figure 6:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase when Hutch-1 is secured.



Changing Beam status
--------------------

#. Turn the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase BEAM STOP key to Open. 
   The Beam Stop lamp turn :green:`green`.

#. The Hutch-1 Control IONIZING RADIATION INTERLOCK protocase BEAM STATUS DIVERGENT lamp turn :green:`green`.

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

.. list-table:: 
    :align: center

    * - .. image:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_Divergent_open.jpg
            :scale: 20 %
            :align: center

      - .. image:: /images/user_docs/Hutch-1_ionizing_radiation/Hutch-1_Collimated_open.jpg
            :scale: 20 %
            :align: center

    * - Divergent beam open. :white-cell:`===============================================================`
      - Collimated beam open. :white-cell:`==============================================================`


.. table-caption::
    **Figure 7:** This is the Hutch-1 Control IONIZING RADIATION INTERLOCK protocase when either shutter is open. 
    When the beam stop is open a shutter will automatically open to whatever beam select is set to before hand. 


Returning to Starting Conditions
--------------------------------

#. Return the Hutch-1 ionizing radiation interlock system back to starting conditions. 