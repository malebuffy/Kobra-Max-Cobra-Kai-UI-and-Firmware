# Kobra-Max-Cobra-Kai-UI-and-Firmware
New Kobra Max UI based on Cobra Kai and M117 Support, G-code Thumbnail Preview and Terminal App inside of Menu

Changelog:

v0.4<br>
-Enabled Linear Advance for those who are brave enough to try it :)<br>
-Fixed babystep bug<br>
-Added G-Code Terminal Application in Main Menu (send only at the moment, no display of results in the screen)<br>
  <br>
<img src="https://user-images.githubusercontent.com/23300461/229234694-ee81c843-e837-4f93-a992-ef81a38e1b2c.jpg" width=52% height=52%>


v0.2<br>
  -Added G-Code Preview function<br>
  -Cura Post-Script <br>
  <br>
  
![Preview](https://user-images.githubusercontent.com/23300461/228777395-b01aed67-0d09-40b6-a19e-0f7e892d1f24.png) 

v0.1<br>
  -Cobra Kai UI<br>
  -E-steps set to 427<br>
  -Z offset babysteps at 0.01<br>
  -M117 Enabled for comments (Layer height etc)<br>
  -49 Autolevel Mesh Points<br>

![M117](https://user-images.githubusercontent.com/23300461/228777351-6442d35b-c4c7-4670-8450-9886bdc6070f.png)

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

Instructions for installing G-Code Thumbnail Script in Prusa slicer:<br>
-Put the script somewhere where it will not be deleted. I did put it in the python311 folder<br>
-In printer settings, look at the firmware settings and change the size to 150x120 and PNG according to the below image.<br>
![postscript](https://user-images.githubusercontent.com/23300461/230036721-274c6de9-55e1-4c38-96b5-11063a6e04b4.png)

-In print settings in the output category, put the path as in the below picture. Change according to where you placed your script.<br>
![GcodeThumbnailSettings](https://user-images.githubusercontent.com/23300461/230036953-d3c77076-a38a-4a7e-acf8-648e81de2cfd.png)

<br>
For anyone that wants to tinker with firmware!<br>

-I am not invent the wheel again. Here are two tutorials on how you can compile the firmware<br>
<br>
https://www.reddit.com/r/anycubic/comments/y2waxu/tutorial_how_to_build_anycubic_marlin_source_code/<br>
<br>
-and here is the software to use to change the UI<br>
<br>
https://www.dwin-global.com/uploads/DGUS_V7641-0801.zip<br>
https://www.dwin-global.com/uploads/DGUS-Software-Run-Environment.rar<br>
