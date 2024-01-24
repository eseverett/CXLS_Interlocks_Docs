.. CXLS Interlock System Documentation documentation master file, created by
   sphinx-quickstart on Wed Jan 10 08:39:18 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. This is a custom html command |small_space| that can be called to add an indent.
.. |small_space| raw:: html

    <div style="margin-bottom: 25px;"></div>   


Welcome to CXLS Interlock System Documentation's documentation!
===============================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

About This Documentation
------------------------

The purpose of this documentation is to provide a complete guide to the CXLS interlock system. 
This documentent will outline user guides to all interlock subsystems, as well as provide documentation on testing and troubleshooting the system.

CXLS Facility Overview
----------------------

.. image:: images/CXLS_FACILITIES.png
   :align: center
   :scale: 50%

|small_space|

Ionzing Radiation Hazards
-------------------------

In the CXLS linear accerator, the relativistic electrons can interact with materials of beampipes and LINACs. 
These interactions are Columb forces between the relativistic electrons and atomic nuclei within these materials where the electron experiences negative acceleration and releases a high energy photon, gamma radiation. 
This process is known as Bremsstrahlung. These emitted gamma rays can then interact with nuclei and through the process of photodisintegration neutron radiation is produced. 
Because of the high radiation feilds generated in Vault-1, this area is off limits during operations. 
As well, when x-rays are enabled into Hutch-1, this area is also off limits.

Laser Hazards
-------------

In the CXLS, there are three class 4 lasers used throughout the system. 
A UV laser is used at the photocathode to eject electrons in bunches via the photoelectric effect. 
Once these electrons are at relativistic speeds, they collide with an IR laser to induce inverse Compton scattering to produce hard x-ray pulses. 
These x-rays will interact with a test sample in pump-prove configuration where the pump laser can produce light in the THz spectrum. 
Because of these high power lasers through the facility, laser enclosures have been design to create laser safe areas while lasers are operational. 


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

   User Documentation is under revisons.
   
   Testing and Troubleshooting Documentation is starting development.


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
