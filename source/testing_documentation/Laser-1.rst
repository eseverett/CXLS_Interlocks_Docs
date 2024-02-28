.. these roles are defined to use custom css classes
.. role:: orange
.. role:: red
.. role:: green
.. role:: white-cell


Laser-1 Interlock System Testing Protocol
=========================================

The purpose of this protocol is to test the Laser-1 interlocks system. 
This includes:

- Arming Laser-1.
- Arming the Dira.


Starting Conditions
-------------------

#. The Vault-1 Control VIEWMARQ only displays :green:`LASER SAFE`.

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

.. list-table:: 
    :align: center
    
    * - .. image:: /images/user_docs/Vault-1_ionizing_radiation/Vault-1_Control_VIEWMARQ_safe.jpg
            :align: center
            :scale: 28 %

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_safe.jpg
            :align: center
            :scale: 20 %

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_safe.jpg
            :align: center
            :scale: 20 %

    * - This is the Vault-1 Control VIEWMARQ in a safe condition. :white-cell:`===================================`
      - This is the Laser-1 entrance VIEWMARQ in a safe condition. :white-cell:`==================================`
      - This is the Laser-1 airlock VIEWMARQ in a safe condition. :white-cell:`===================================`

.. table-caption::
    **Figure 1:** These are the VIEWMARQ displays that show the state of the Dira.

.. list-table:: 
  :align: center

  * - .. image:: /images/user_docs/Vault-1_laser/Vault-1_Control_beacons.jpg
        :scale: 76 %
        :align: center

    - .. image:: /images/user_docs/Vault-1_laser/Vault-1_beacons.jpg
        :scale: 20 %
        :align: center

    - .. image:: /images/user_docs/Vault-1_laser/Pharos_beacons.jpg
        :scale: 43 %
        :align: center

    - .. image:: /images/user_docs/Vault-1_laser/Dira_beacons.jpg
        :scale: 53 %
        :align: center

  * - Vault-1 Control beacon stack. :white-cell:`=========================================================`
    - Vault-1 beacon stack. :white-cell:`=================================================================`
    - Pharos LASER ENCLOSURE INTERLOCK protocase beacon stack. :white-cell:`==============================`
    - Dira LASER ENCLOSURE INTERLOCK protocase beacon stack. :white-cell:`================================`

.. table-caption:: 
    **Figure 2:** These are the Vault-1 laser interlock system beacon stacks.
    These all show the state of the Dira.




.. figure:: /images/user_docs/Laser-1/Laser-1_control_module_safe.jpg
    :scale: 20 %
    :align: center

    **Figure 3:** This is the control module in Laser-1 airlock in a safe condition


.. figure:: /images/user_docs/Laser-1/Laser-1_push_to_exit_safe.jpg
    :scale: 20 %
    :align: center

    **Figure 4:** THis is the push-to-exit module in Laser-1 airlock in a safe condition.



.. figure:: /images/user_docs/Laser-1/Laser-1_entry_safe.jpg
    :scale: 20 %
    :align: center

    **Figure 5:** This is the entry keypad in Laser-1 in a safe condition.


.. figure:: /images/testing_documentation/Laser-1/e-stop_off.jpg
    :scale: 20 %
    :align: center

    **Figure 6:** This is the e-stop module in Laser-1 in a safe condition.


.. figure:: /images/testing_documentation/Laser-1/RF_door.jpg
    :scale: 20 %
    :align: center

    **Figure 7:** This is the Laser-1 to RF-1 door monitor in a closed condition. 

    

.. figure:: /images/user_docs/Laser-1/Laser-1_arming_panel.jpg
    :scale: 20 %
    :align: center

    **Figure 8:** This is the arming panel for Laser-1.




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

#. Dira LASER ENCLOSURE INTERLOCK protocase laser warning module shows :red:`DANGER LASER ON`.

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


.. list-table:: 
    :align: center 

    * - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_armed.jpg
          :scale: 20 %
          :align: center

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_armed.jpg
          :scale: 20 %
          :align: center      

    * - This is the Laser-1 entrance VIEWMARQ in an armed condition. :white-cell:`================================`
      - This is the Laser-1 airlock VIEWMARQ in an armed condition. :white-cell:`=================================`

.. table-caption:: 
    **Figure 9:** These are the Laser-1 VIEWMARQ displays when Laser-1 is armed.


.. figure:: /images/user_docs/Laser-1/Laser-1_control_module_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 10:** This is the control module in Laser-1 airlock in a safe condition


.. figure:: /images/user_docs/Laser-1/Laser-1_push_to_exit.jpg
    :scale: 20 %
    :align: center

    **Figure 11:** THis is the push-to-exit module in Laser-1 airlock in a safe condition.



.. figure:: /images/user_docs/Laser-1/Laser-1_entry_armed.jpg
    :scale: 20 %
    :align: center

    **Figure 12:** This is the entry keypad in Laser-1 in a safe condition.


.. figure:: /images/testing_documentation/Laser-1/e-stop_on.jpg
    :scale: 20 %
    :align: center

    **Figure 13:** This is the e-stop module in Laser-1 in a safe condition.


Arming the Dira
---------------

#. Arm the Dira local interlock module. 
   Dira local interlock module has LED on for :orange:`LOCAL CONTACTS ARMED`.

#. The VIEWMARQ display in Laser-1 airlock :red:`DANGER LASER ON - IR EYE PROTECTION REQUIRED`.

#. The VIEWMARQ display in the Laser-1 entrance shows :red:`DANGER LASER ON - IR HAZARD`.

#. The VIEWMARQ display in Vault-1 Control shows :green:`LASER SAFE` - :red:`DIRA ARMED`.

#. The Vault-1 beacon stacks should show :green:`green` and white LEDs on.

    - Vault-1 control.
    - Vault-1 east wall.
    - Dira LASER ENCLOSURE INTERLOCK protocase.

#. Beacon stack on the Pharos LASER ENCLOSURE INTERLOCK protocase will only have a :green:`green` LED on.

#. Dira LASER ENCLOSURE INTERLOCK protocase laser warning module shows :red:`DANGER LASER ON`.




.. list-table::
    :align: center 

    * - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_entry_IR.jpg
          :scale: 20 %
          :align: center

      - .. image:: /images/user_docs/Laser-1/Laser-1_VIEWMARQ_airlock_IR.gif
          :scale: 56 %
          :align: center      

      - .. image:: /images/testing_documentation/Laser-1/Vault-1_Control_VIEWMARQ_dira_armed.jpg
          :scale: 20 %
          :align: center

    * - This is the Laser-1 entrance VIEWMARQ when the Dira is armed. :white-cell:`===============================`
      - This is the Laser-1 airlock VIEWMARQ when the Dira is armed. :white-cell:`================================`
      - This is the Vault-1 Control VIEWMARQ when the Dira is armed. :white-cell:`================================`

.. table-caption::
    **Figure 14:** These are all the VIEWMARQ displays that will update when the Dira is armed. 


Safe Dira E-Stop Test
---------------------

#. Put the Dira into a powered down state.

#. Arm Laser-1 and the Dira. 

#. Press one of the Dira enclosure laser e-stops. 

#. Verify that the Dira power supply is cut off.


RF-1 Door
---------

#. With the Dira not armed, open the door between RF-1 and Laser-1.
   The door monitor module should display nothing.


.. figure:: /images/testing_documentation/Laser-1/door_monitor_open.jpg
    :scale: 20 %
    :align: center

    **Figure 15:** This is the Laser-1 to RF-1 door monitor when the door is open.

Crashing the Dira
-----------------

#. Once every 6 months, the Dira laser emergency stop buttons are testing that they can successfully cut power to the Dira from a fully armed state.
   Verify if the last testing date was 6 months ago. 

#. If 6 months have passed, arm the Dira laser and use one of the Dira laser e-stops to cut power from the Dira in an armed state.
