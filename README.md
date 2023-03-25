# Kobra-Max-Cobra-Kai-UI-and-Firmware
New Kobra Max UI based on Cobra Kai and M117 Support and G-code Thumbnail Preview

Changelog:

v0.2
  -Added G-Code Preview function<br>
  -Cura Post-Script <br>

v0.1
  -Cobra Kai UI<br>
  -E-steps set to 427<br>
  -Z offset babysteps at 0.01<br>
  -M117 Enabled for comments (Layer height etc)<br>
  -49 Autolevel Mesh Points<br>

Instructions for installing printer firmware:<br>

-Put the firmware.bin into the root of the SD and insert it to the 3D printer SD slot (Not the LCD)<br>
-Switch the 3D printer on and wait for the beeps. <br>

Instructions for installing the UI:<br>

-Put the DWIN_SET folder into the root of the SD and insert it to the 3D LCD SD slot (Not the printer slot)<br>
-Switch the 3D printer on and wait for the blue screen. After it's done,remove the SD card and restart the printer<br>

Instructions for installing G-Code Thumbnail Script in Cura:<br>

-Open the Config folder (Help - Show configuration Folder). Navigate to the Script folder. If that doesnt work the folder ist usually in the C:\Users\Your Name\AppData\Roaming\cura\5.x\scripts<br>
-Download and put the script here. Must have a .py extension<br>
-Restart Cura and go to Extensions - Post Processing - Modify G-Code and Add Script. Select Create Kobra Thumbnail.<br>
-Now whenever you slice a script, a thumbnail is created in the G-Code file that the Kobra Max can read. Only Thumbnails with this scripts are recognised.<br>


For anyone that wants to tinker with firmware!<br>

-I am not invent the wheel again. Here are two tutorials on how you can compile the firmware<br>
<br>
https://www.reddit.com/r/anycubic/comments/y2waxu/tutorial_how_to_build_anycubic_marlin_source_code/<br>
<br>
-and here is the software to use to change the UI<br>
<br>
https://www.dwin-global.com/uploads/DGUS_V7641-0801.zip<br>
https://www.dwin-global.com/uploads/DGUS-Software-Run-Environment.rar<br>
