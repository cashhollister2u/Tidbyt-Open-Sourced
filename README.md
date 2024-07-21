# Led Board and Application Set-Up

<br>
<br>

### Build your own retro pixel display. 
- This is a beginnner level project. This is a good project for learning how to solder (optional). It presents an opportunity to become more familiar within a terminal/shell. Modify the code and create your own custom views/displays.   

<br>
<br>

### Disclaimer: SSH or Remote Access is utilized to edit and install files on the Raspberry Pi. It is up to the user to configure the security settings to meet their specific needs. Disabling SSH after project completion is an option.

<br>
<br>

<img src="https://github.com/user-attachments/assets/ffe1a7d8-7a17-4cde-b46c-1fd84d1a3061" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/user-attachments/assets/f7e4883c-611c-47ab-a7d1-bc2b112cb581" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/user-attachments/assets/6e83f1fd-2e01-4eff-a60d-b235acf8fe58" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/user-attachments/assets/e327c2ea-b401-46d0-a617-a2618d8a0d00" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/user-attachments/assets/88915f8c-de44-4175-ab89-3b9e7b2c442a" alt="IMG_0584" width="300" height="200">

<br>
<br>

# 3D Printer Files and Settings (Bambu Labs P1S)
It may be a good idea to initiate the print before completing the Hardware/Software tutorials. Print time is roughly 6.5 hours.
Ensure a clean print plate for best adhesion. Most parts are flat and take up a large surface area.

- Files can be found on MakerWorld:
  - https://makerworld.com/en/models/543827

- Material:
  - Overture PETG
    
- Nozzel:
  - 0.4 nozzel
    
- Print Material Profile:
  - Bambu PETG Basic Filiment
    
- Screen Cover:
  - White PETG
  - Printed using "*0.08mm Extra Fine @BBL X1C"
  - All "Initial Layer Speeds" set to 50mm/s
  - All "Top Layers Speeds" set to 50mm/s
  - "Initial layer height" set to 0.1mm
  - "Layer height" set to 0.1mm
    
- Main Body, Back Cover, Button, Pi Mounting Plate:
 
   - A "Main Body" perform a "cut" at y=20 and isolate the mounting platform for the Pi.
   - Ensure the cut only selects the platform and not the walls of the main body.
   - "Connectors" (Snap) on each of the 6 pillars that support the platform
     - Depth ratio = 2.50mm / Size = 2.00mm (connector settings)
   - Prited using "0.28mm Extra Draft @BBL X1C"

- It is recommended to wait for parts to cool down to room temp before attempting to assemble.
  - ie. The LED Matrix panel is press fit to the main body.
  - WARNING: The board is a tight fit so take your time with its assembly. 

<br>
<br>

# iOS App
- Currently in Beta ***
- Download TestFlight from the iOS store
- Click on this link to Download the App via TestFlight:
  - https://testflight.apple.com/join/O1uEL3ar

<br>
<br>

# Hardware Set-Up
- Pre-Made Button for On/Off switch (optional)
  - [amazon](https://www.amazon.com/Twidec-Normal-Momentary-Pre-soldered-PBS-110-XR/dp/B07RV1D98T/ref=sr_1_2?dib=eyJ2IjoiMSJ9.cc92CYD6puREW-x_KclpTxxF9dJcV70bwpHP-jv-Wn2_PPcrELPjwRkWQH12hJr2dz5d-kDj8Gqh3-SzwORFMF7KfkKKUL8Gr94a0AC91_Qm8w9eVfvEArO9o3QgMDzNxYQhj0qf56dxpL16K72le_0ZEBwkry7Zh9IWC3ZaSD_FYDiE5sCKnJWk8Xk_RDVnh1xd3hJFhQKd1CObGwGfsE0Od-4hqoPX3EcL7heuV00.3lw6QoZoAzrgV8Qc4Dn2bHNZNRAPMQfgz7cn0diES90&dib_tag=se&keywords=Raspberry%2BPi%2BPower%2BButton&qid=1720996822&sr=8-2&th=1)
- If utilizing the button it must be soldered to the "SCL" and "GND" pins of the Matrix Bonnet. The orientation of the wires does not matter. (optional)
- <img src="https://github.com/user-attachments/assets/fcf34ac5-c3ea-4da0-820d-abdcc2f5171a" alt="IMG_0584" width="300" height="200">
- For the best quality image solder pin 4 and pin 18 with a jumper wire. (Further details and pictures in the adafruit link below the "Recommendations" section) (optional)

<br>
<br>

- ### Recommendations:
  - Complete all soldering before connecting the Raspberry Pi to the Matrix Bonnet.
  - After connecting to the Pi to the Bonnet and Matrix. Complete the Software Set-Up and ensure all functionality before proceeding with assembly. 
  - Attach the pi to the 3D printed mounting platform before connecting the platform to the main body.
    
- This page provides detailed instructions on how to propperly connect the bonnet to either the Raspberry Pi 4 or the RaspBerry Pi Zero 2 as well as connecting the bonnet to the LED Matrix.
  - Refer to "3D Print Assembly" before following the tutorial below.
  - https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices

<br>
<br>

- ### 3D Print Assembly:
  - NOTE: For this use case the PI and the Matrix Bonnet are both powered by the 5V 10amp charger. (unlike the Adafruit instructions)
  - NOTE: No heating element is required for press fitting of parts.
  
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/e8a1d252-b02a-4dae-baf6-41169f29b965" alt="IMG_0584" width="300" height="200">
  - Press the LED Matrix into the grid and ensure it is fully seated.
  - Be patient and take your time.
  - Inspect corners and check for imperfections in the 3D print.
   
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/5c3ad6b3-e747-45ac-81a8-a2008dacf2e1" alt="IMG_0584" width="200" height="200">
  - Press 4 M2.5 Nuts into the designated slots.
  
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/7591a1ad-b411-4995-ba34-72711d964276" alt="IMG_0584" width="300" height="200">
  - Loosly fix 4 M2.5 Nuts to the bottom of the Pi Zero 2 using brass spacers. (Spacer orientation/length may vary based on set up)
   
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/18092f95-6b54-448c-b287-f98f52648602" alt="IMG_0584" width="300" height="200">
  - Screw the Pi to the Mounting Plate in this orientation.
   
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/0f1811aa-7da6-4f4e-b10d-cedf0ff81c21" alt="IMG_0584" width="300" height="200">
  - Connect the Bonnet to the Pi and Connect the Matrix Power Cables to the Bonnet.
  - There may be a gap between the bonnet and the Pi Zero 2 that exposes the GPIO Pins. This is OK and may be required based on spacer orientation.
     
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/bd807093-b3a3-48ce-be67-4c692df9c3af" alt="IMG_0584" width="300" height="200">
  - Press the Mounting Plate into the snap connectors (Can be Re-Used if removed carefully).
  - Assemble the Push Button (optional). (Insert Button into the frame and use the provided washer to secure from the exterior)
  
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/c52055da-5a29-41c1-82c6-a9a016c38896" alt="IMG_0584" width="200" height="300">
  - Press fit the 3D printed button cover over the cap of the Push Button (optional).
   
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/86a10883-a1e5-46aa-b2e4-a2e793339b4a" alt="IMG_0584" width="300" height="200">
  - Route the wires and insert the 5V 10amp external power source into the bonnet. Ensure the plastic cylinder attached to the power cable is inside the housing as in the picture. It acts as a strain relief for the Pi.
  - Press 4 M2.5 Nuts in the four corners of the frame.
   
  <br>
  <br>
  
  - <img src="https://github.com/user-attachments/assets/66329423-7f69-448b-9951-19eb4568c578" alt="IMG_0584" width="300" height="200">
  - Utilize 4 M2.5 screws to fix the back plate onto the Main Body.
    
<br>
<br>

# Software Set-Up

## Sign-Up For Free API Services:
- All api services provided by the led application utilize the free trials of the following. 
### Twelve Market Data
- https://twelvedata.com/pricing
- API key required for led application 
### Open Weather Map
- https://openweathermap.org/price
- API key required for led application
### Spotify Developer Account
- https://developer.spotify.com/documentation/web-api/tutorials/getting-started
- IGNORE everything after "Create an App" the led applicaiton handles the rest
- Ensure "REDIRECT URI" is set to http://localhost:8080/
- CLIENT ID AND CLIENT SECRET are required for the led application
    - To Locate go to "DashBoard" select the app you created and click on "Settings" in the top right corner.

<br>
<br>

## Download Raspberry Pi Imager
- https://www.raspberrypi.com/software/

<br>
<br>

## RaspBerry Pi Zero 2 Set-Up (Software)
### STEP 1:
- Insert Micro SD into computer
- Open Raspberry Pi imager

## STEP 2:
- Click on "Choose Device"
- Select Raspberry Pi Zero 2 
- Click on "Choose OS"
- Select Raspberry Pi OS (Other) 
- Select Raspberry Pi OS Lite (32-bit)
- Click on "Choose Storage"
- Select Micros SD
- Click "Next"
- Click "EDIT Settings"
- Select General
- Set Hostname: “LedApp”.local (IMPORTANT)
- Set username: “led_app” (IMPORTANT)
- Set password: Your Choice
- Configure wifi
- Select Services
- Enable SSH
- Enable Password or Public-Key Auth
- Click Save
- Click "YES" (use custom settings)
- Click "YES" (erase previous data)
- Wait for install to complete

## STEP 3:
- Unplug Micro sd and insert into Raspberry Pi  (Ensure Pi is off)
- Turn on Raspberry Pi
- Gain remote access to the Raspberry Pi run the following command in your PC/Laptop's Terminal:
  - “ssh led_app@LedApp.local”
- Pi will cycle through a initial boot and reboot for the first boot cycle if it takes longer than 10 minutes to get a responce repeat steps 1 and 2 data may be corrupted
- Run the following commands after gaining access and logging into the Raspberry Pi:
  - "sudo apt update" (update available software)
  - "sudo apt install git" (needed for the "git clone" command)
  - "git clone https://github.com/cashhollister2u/Tidbyt-Open-Sourced.git" (download this repository)
  - "sudo ./Tidbyt-Open-Sourced/Bash_Scripts/install.sh" (refer to "Bash_Scripts/install.sh")
- Follow the prompts that the terminal displays
- Have the api keys associated with the accounts you created. You will be prompted for them.
- When prompted to reboot select "y" or yes for changes to take effect.
- It may take 30s - 1min to reboot
- NOTE: If you are concerned about security or are unfamiliar with ssh you can run this command on the raspberry pi to disable ssh.
  - "sudo systemctl disable ssh"
  - By doing so you will no longer be able to access the device and will have to repeat the software installation process again to make any changes.
  - To confirm the command do any of the following:
    - "sudo reboot -h now"
    - Turn off the device via the push button (optional)
    - Turn off the device via the iOS app controller

<br>
<br>

## That completes the software set up for the Raspberry Pi 
- If the hardware is configured propperly you should see the LED Display propt you to connect the iOS app
- Download the app from TestFlight 
- Open the app
- Click "Settings"
- Click "Show" next to the Spotify Auth
- Click "Authenticate"
- Click "Home" on the app display and select one fo the four display options
  - If selecting "Spotify" ensure Spotify is currently playing. Otherwise the screen may display an error.

<br>
<br>

## Basic Operation:
- The board takes ~23s to prompt a connection to iOS after it is turned on.
- Plug in the board to turn on or press the (optional) physical button
- To connect, select one of the 4 displays in the iOS app when the LED Matrix prompts you to "connect to iOS"
- To turn off the board use the power button in the iOS app or (optional) physical button
  - To be safe look through the vent holes in the back for the green light to stop flashing on the Raspberry Pi (The Matrix Bonnet has a green light that will remain lit)
- WARNING: If the board is unpluged without using the iOS app / physical button it may corrupt the files.
- WARNING: Spotify Updates every 8 seconds (this is for program stability) / Song titles DO NOT scroll (this is for album cover image stability)
- NOTE: If anyone actually uses this I can post an update fixing the Warnings above.

<br>
<br>

# Support The Project:
- Donations to support the project/creator can be made here:
  - https://buymeacoffee.com/cashhollister

<br>
<br>

# Questions/Recommendations/iOS Beta Access
- Utilize this email for any support questions, recommendations for the project, or access to the iOS Beta:
  - ledappcontroller@gmail.com

<br>
<br>

## Debugging Hardware / Software
- If the board displays lights but does not appear as expected or jumbled, first follow the steps here:
  - https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/help
- If chosen to take the soldering approach re-check solder connections between the pi zero 2 and the gpio pins.
- Continuity Test (LED Method) (I'm sure there is a better method)
  - First remove the Matrix Bonnet and ensure nothing is connected to the GPIO Pins.
  - Assemble a circuit utilizing an led and a 33 ohm resistor
  - <img src="https://github.com/user-attachments/assets/49c3d4c7-943d-475e-ba8f-c8a3ca3559d8" alt="IMG_0584" width="300" height="200">
  - The yellow wire stay connected as in the image (ground)
  - the blue is connected to the pin being tested
  - Pin refrence here - https://pinout.xyz
  - I recommend testing the control, address, and color pins refrenced here - https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/pinouts
  - Locate the test_pins.py file in the Tidbyt-Open-Sourced" directory
  - With the ground (yellow) connected to ground and the positive (blue) connected to the pin being tested run the python script.
  - You will be prompted to enter the pin you are testing
  - If the connection is good the led will flash red once
- If the continuity test is successfull and the image is only partially distorted diagnose the issue based on the pin functionality description here - https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/pinouts
  - ie. Pi GPIO #16 - Matrix G2 (Green row2) pin: This pin controls the green LEDs on the bottom half of the display
  - Then re-affirm the solder conenction at that pin

<br>
<br>

# Hardware List (Raspberry Pi Zero 2) (Hardware for other pi variants may be different)
### Total Cost ~ $85.00 - $100.00

<br>

- Raspbery Pi Zero 2 
  - [https://www.adafruit.com/product/4296](https://www.adafruit.com/product/5291)
- GPIO header pins (solderless) (OPTION 1)
  - https://www.adafruit.com/product/3662?gad_source=1&gbraid=0AAAAADx9JvQF9r4jQa4XoDPi65FgIZNb-&gclid=EAIaIQobChMI4IuM2eWnhwMVJ25_AB0yUQ59EAQYASABEgJf4_D_BwE
- GPIO header pins (soldering req) (OPTION 2)
  - https://www.adafruit.com/product/2822
- 16 or 32 gb Micro SD Card for Raspberry Pi
  - [Amazon](https://www.amazon.com/SanDisk-Ultra-microSDXC-Memory-Adapter/dp/B073JWXGNT/ref=sr_1_8?crid=3BA0SAU4Z3BVC&dib=eyJ2IjoiMSJ9.gma2hVfUgy-OBJ-COHM6pbshqICnhWgymisufu6qkTikGx9DMDOT-3dc7naXHtt0GM5F7Dc-Kzp8nmsDFj5eZRuSTCXBZHiIuxiikhiAopv-ALnQMJtZZVEZLa4dxi8Tr1MkCnvShyoG4zFOWRbtyg1_XfMy-BaL2RcxbW6T4j0bIq9oyaprOGw9gEz1MJSrd4Xhy54847gErjsLfFbm8xlkS_w2olOighTBk9fXdI329hnd6R0Gkh-Ykuode-GpM0Fs1ZgVM-bJ4eExbhLlgDixoFgMeH63-s7JflFici0.Aj76Y7zJJKxqQMwN3vLCvcBD0_9C8W23b6iYM99UH6c&dib_tag=se&keywords=32+gb+micro+sd&qid=1720498866&s=electronics&sprefix=32+gb+micro+sd%2Celectronics%2C131&sr=1-8)
- A device to insert the Micro SD into your laptop or PC to install Pi OS.
- gpio extention (optional)
  - https://www.adafruit.com/product/2223?gad_source=1&gbraid=0AAAAADx9JvRoR7oa6Xt2MOaaaoUYxxSop&gclid=CjwKCAjwnK60BhA9EiwAmpHZw2OqCtdnE_kqISjUMuYMXSpIDnCF-1EZaFNnZ6MPz9KHeC91vC1JABoCNKQQAvD_BwE
- Pre-Made Button for On/Off switch (optional)
  - [amazon](https://www.amazon.com/Twidec-Normal-Momentary-Pre-soldered-PBS-110-XR/dp/B07RV1D98T/ref=sr_1_2?dib=eyJ2IjoiMSJ9.cc92CYD6puREW-x_KclpTxxF9dJcV70bwpHP-jv-Wn2_PPcrELPjwRkWQH12hJr2dz5d-kDj8Gqh3-SzwORFMF7KfkKKUL8Gr94a0AC91_Qm8w9eVfvEArO9o3QgMDzNxYQhj0qf56dxpL16K72le_0ZEBwkry7Zh9IWC3ZaSD_FYDiE5sCKnJWk8Xk_RDVnh1xd3hJFhQKd1CObGwGfsE0Od-4hqoPX3EcL7heuV00.3lw6QoZoAzrgV8Qc4Dn2bHNZNRAPMQfgz7cn0diES90&dib_tag=se&keywords=Raspberry%2BPi%2BPower%2BButton&qid=1720996822&sr=8-2&th=1)
- IPhone (used for LED Board controller)
- Adafruit Matrix Bonnet
  - https://www.adafruit.com/product/3211
- 32 X 64 3mm pitch LED Matrix (Ive found that 3mm is best for Desktop Visibility) (3D files built to support 3mm pitch)
  - [Amazon](https://www.amazon.com/Waveshare-Full-Color-Individual-Adjustable-Brightness/dp/B0B5N5HPKX/ref=sr_1_2?crid=3EE2RLGAFVNC0&dib=eyJ2IjoiMSJ9.6oWrmhaCysWQ6qbBZtvRPtuQFAcbo_KZfVjT3w0WNRURf4c_8LdoDPCJzGhy9tWullLorzWBjrTn1PlSDj-DX7ZxVfj83l0zLvIAVLbHu0bE95X980lZwgOa7jkOEbl_Enki0Q3Jo-yasOGaD7XEsSKcH8O2vhA2hQwktcXNVlq-TFHk7Sfo1ZQ-2zCC3MNrgMAuG0W_xDqNSZJfmaBb1N-TG0UULugbZZ1GlVODYvs.AxmNy8pyNuM09ZaFkDXfzJ-czBjdJapyLn1JC3J6bL0&dib_tag=se&keywords=32+X+64+3mm+pitch+LED+Matrix&qid=1720499174&sprefix=32+x+64+3mm+pitch+led+matrix%2Caps%2C214&sr=8-2)
- 5V 10 Amp charger with Barrel Connector Male (Power both the LED board and Raspberry Pi)
  - [Amazon](https://www.amazon.com/10A-Power-Supply-Adapter-Switching/dp/B07H9XRZBP/ref=sr_1_2?crid=31A60WJNMKB4L&dib=eyJ2IjoiMSJ9.je877a0xnR4pfYxTF_0U6VDr9ZWNS3ATxNAOGSqhnWM__La7IzTYY-_Mg6yM072tnJQ8MZD80hURwLODE9jFtcwCrMps8yq-YBtffrXRhZI8poQBa3unZHCNaHB_90uOPAmM2O-sTZ-_fa6W8CyureTFLDfdoQTdiTz8Bvg_fhH1QWd44OH97XIj0_Qqs0qsn-s-NyyGDLf-SiQkKKxLwJ04E0gCHSD87Zubs4jyWnQ.B6CIy5o4OmhKjVlphmawFai7AqbyU_APljyTN0I94Vw&dib_tag=se&keywords=5V+10+Amp+charger+cool&qid=1720499223&sprefix=5v+10+amp+charger+cool%2Caps%2C99&sr=8-2)
- RaspBerry Pi Brass Spacer Kit with M2.5 Nuts and Screws
  - [Amazon](https://www.amazon.com/Geekworm-Raspberry-Installation-Standoff-Accessories/dp/B0756CW6Y2/ref=sr_1_6?crid=1WIJ52THVGKAP&dib=eyJ2IjoiMSJ9.4vBz5jbdFFOUtiz9dlUIeNocA1PZrMFELvxfpBsJEauqSijKi8LOeXqvuXxtIXUkgwOsq_9PlPbgfsAGFdJaNxzQZgTj-yARI76t3xqQWNyB9At3IsBCIWPSF6dq5QvkSnASFhCdwWz463ftttUuG7MaqhrD9E-eNHP1ojmMRMxDNMBSbyNPwyLDj4hL06kszQLs6uqNLImpSXhbkOveOf-zzTU06B8clHoEHzymkRY.cGx_1wekEp3kUjAIoMOEXhOosZFJUN_5ML_G8om5nY0&dib_tag=se&keywords=RaspBerry+Pi+Brass+Spacer+Kit&qid=1720499301&sprefix=raspberry+pi+brass+spacer+kit%2Caps%2C102&sr=8-6)
- Solder Iron / Jumper Wire (This can be skipped but reduces quality)
- Access to 3D Printer (for housing)
- Small Skrew Driver
- A micro usb charger may be usefull for debugging hardware but not required 
