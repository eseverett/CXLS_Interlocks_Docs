.. CXLS Interlock System Documentation documentation master file, created by
   sphinx-quickstart on Wed Jan 10 08:39:18 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. This is a custom html command |small_space| that can be called to add an indent.
.. |small_space| raw:: html

    <div style="margin-bottom: 25px;"></div>   


Welcome to the CXLS Interlock System documentation!
===================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

About This Documentation
------------------------

The purpose of this documentation is to provide a complete guide to the CXLS interlock system. 
This document will outline user guides to all interlock subsystems, as well as provide documentation on testing and troubleshooting the system.

-----

CXLS Facility Overview
----------------------

.. image:: images/CXLS_FACILITIES.png
   :align: center
   :scale: 50%

|small_space|

-----

Ionizing Radiation Hazards
--------------------------

In the CXLS linear accelerator, relativistic electrons can interact with materials of beam pipes and LINACs. 
These Coulomb interactions between the relativistic electrons and atomic nuclei within these materials cause the electrons to experience acceleration and release a high energy photon. 
This process is known as Bremsstrahlung. These emitted gamma rays can then interact with nuclei and through the process of photodisintegration neutron radiation is produced. 
These processes cause elevated radiation felids in Vault-1 and Hutch-1. 

-----

Laser Hazards
-------------

There are three class 4 lasers used throughout the CXLS system. 
A UV laser is used at the photocathode to eject electrons in bunches via the photoelectric effect. 
Once these electrons are at relativistic speeds, they collide with an IR laser and through inverse Compton scattering produce hard x-ray pulses. 
These x-rays will interact with a test sample in pump-prove configuration where the pump laser can produce light in the THz spectrum. 
Due to these high power lasers throughout the facility, laser enclosures have been designed to create laser safe areas while lasers are operational. 

-----

Interlocks System
-----------------

The CXLS interlocks system is comprised of sets of sensors and components that send data to predefined digital logic systems. 
This digital logic decides to change the state of actuators and safety displays. 
These interlocks are designed to enforce proper sequential operations and control access to hazards. 
Redundancy is built into the system to increase reliability, as well as fail safe designs to ensure systems are put into a safe state incase of a user of system failure. 



.. toctree::
   :maxdepth: 1
   :caption: User Documentation:
   :hidden:

   user_documentation/Vault-1_ionizing_radiation
   user_documentation/Vault-1_laser
   user_documentation/Hutch-1_ionizing_radiation
   user_documentation/Hutch-1_laser
   user_documentation/Laser-1
   user_documentation/radiation_data

.. toctree::
   :maxdepth: 1
   :caption: Testing Documentation:
   :hidden:

   testing_documentation/Vault-1_ionizing_radiation
   testing_documentation/Hutch-1_ionizing_radiation
   testing_documentation/e-stop_testing
   testing_documentation/apantec_testing
   testing_documentation/narda_testing
   testing_documentation/O2_testing
   testing_documentation/Laser-1
   testing_documentation/Vault-1_laser
   testing_documentation/Hutch-1_laser
   testing_documentation/radiation_detection
   testing_documentation/testing_log

.. toctree::
   :maxdepth: 1
   :caption: Troubleshooting Documentation:
   :hidden:

   troubleshooting_documentation/IDEM_relay
   troubleshooting_documentation/apantec_ncf
   troubleshooting_documentation/viewmarq
   troubleshooting_documentation/laser_safety_systems

.. note:: 
   This documentation is a work in progress. 
   Last updated: March 07, 2024.


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
