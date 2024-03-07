Laser Safety Systems Troubleshooting Guide
==========================================

For the CXLS laser interlock systems, Laser Safety Systems modules are used to perform the majority of the interlocking function. 

.. pdfbutton:: Laser_Safety_Systems_user_manual.pdf


-----

Resolved Issues
---------------

#. The Laser-1 VIEWMARQ display was not updating when Laser-1 was armed.
   This was traced back to the the corresponding arming module relay was not being energized.
   This was due to loose contact terminals, barely holding onto the PCB, causing intermittent contact.
   Replacing the arming module fixed this issue.

#. Again, the Laser-1 VIEWMARQ display was not updating correctly.
   As well, the Laser-1 control module was showing dim lighting and the keypad was working, but with no LED or audible feedback.
   This was traced back to the Laser-1 control module. 
   The relay contact that sends a signal to the Laser-1 VIEWMARQ display was being energized by the push to exit button, not the arming button. 
   We are not sure why, nor why the keypad was affect, but replacing the Laser-1 control module fixed this issue.