Apantec Ionizing Radiation Sensor No Count Fail Troubleshooting Guide
=====================================================================

The each gamma and neutron probe for the Apantec area monitoring system has a no count fail time (NCFT) setting.
This set point tells the probe that if radiation is not detected over a certain period of time, then the probe if failing. 

This NCFT has caused false fails because of the during of time we go without running the beam. 
The CXLS interlock system is currently in an override state, bypassing the fail signal so that the accelerator can be armed.
Once RF is enabled in to the accelerator structures and the probes see radiation, the fail is cleared. 

.. note::
    We are currently exploring ways to work with the NCFT.
    This could mean changing the setting, or working in a manual reset in the radiation monitoring software. 