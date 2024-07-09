# Led Board and Application Set-Up

## Required Hardware Refrenced at the Bottom
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/8d0cddf8-83f3-448e-90b9-70a758afb57e" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/bb6920f6-ff4d-49ce-815f-a3bd049cfb54" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/1f8c8b90-3964-40ef-b4b5-e148caa803fe" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/7fb41a0d-764e-4189-bd65-df001cf257da" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/0bf04dc4-fd7b-4d76-9d15-3d24ce158498" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/fff90604-6f77-404c-9fad-a8ef23ce79ab" alt="IMG_0584" width="300" height="200">
<img src="https://github.com/cashhollister2u/Led_App_Prod/assets/153677541/5357fde8-a1d5-40a6-84a5-42ef1514189a" alt="IMG_0584" width="300" height="200">

# 3D Printer Files
- It may be a good idea to initiate the print before completing the tutorials. Print time is roughly 6.5 hours (Bambu Labs P1S)
- Files:
  - 

# Hardware Set-Up
- This page provides detailed instructions on how to propperly connect the bonnet to either the Raspberry Pi 4 or the RaspBerry Pi Zero 2 as well as connecting the bonnet to the LED Matrix.
  - https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices



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

## Download Raspberry Pi Imager
- https://www.raspberrypi.com/software/

## RaspBerry Pi 4 Set-Up (Software)
### STEP 1:
- Download the custom image from here:
  - https://www.dropbox.com/scl/fi/tlmi47h2n2p46aot2ipix/Raspi_Led_App_v4.img.zip?rlkey=r1qr4sp8x33adcpea82q7anmc&st=849psice&dl=0
- Insert Micro SD into computer
- Open Raspberry Pi imager

## STEP 2:
- Click on "Choose Device"
- Select Raspberry Pi 4
- Click on "Choose OS"
- Select "Use Custom"
- Select Raspi_Led_app_v4.img
- Click on "Choose Storage"
- Select Micros SD
- Click "Next"
- Click "No" (don’t use custom settings)
- Click "YES"
- Wait for install to complete

## STEP 3:
- Unplug Micro sd and insert into Raspberry Pi  (Ensure Pi is off)
- Plug Raspberry Pi 4 into monitor via hdmi
- Turn on Raspberry Pi 4
- (Pi may cycle through a initial boot and reboot for the first boot cycle)

## STEP 4:
- The Pi will boot into a terminal screen
- Log in using pre set credentials:
  - username: “led_app"
  - password: "led_app”
- Connect to WiFi: (note I was unable to connect to my iPhone hot spot if that is giving you trouble)
  - Type the following command into the terminal "sudo raspi-config"
  - Click "enter" on "System Options"
  - Click "enter" on "S1 Wireless LAN"
  - Use down arrow to select your country and click "enter"
  - Click "enter" on "OK" to confirm
  - Type SSID (WiFi name) into text input
  - Use "Tab" to select "OK" and click "enter"
  - Next enter your WiFi password into the passphrase text input
  - Use "Tab" again and click "enter"
  - Wait till back on main config menu
  - Click "Tab" twice to select "Finish" and click "enter"
  - The screen may look frozen but the input bar is at the bottom just type “clear” and click "enter"

## STEP 5:
- Connect Api Keys from the free accounts you created:
  - Type the following command into the terminal “sudo nano /home/led_app/Led_App_Prod/Secrets/api_keys.py"
  - Ensure the file contains text information and that it is not blank (if blank check your command for typos)
  - Type in the Api Keys from the free accounts you created between the provide quotes
  - Save by clicking “CTRL + x” then “y” then “Enter”
  - The screen may look frozen but the input bar is at the bottom just type “clear” and click "enter"
- Type the following command into the terminal “sudo reboot -h now” (reboots / device boot can take 30s - 60s)

## STEP 6: (Optional ONLY if you are skipping the soldering in the hardware set-up)
- Type the following commands into the terminal:
  - "cd"
  - "sudo bash rgb-matrix.sh"
  - All this does is replace the current “rpi-rgb-led-matrix” directory
  - Then follow the prompts
    - Refer to "Step 6" in this link if you have isses : https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices
  - When prompted choose “convenience” instead of "quality"

## That completes the software set up for the Raspberry Pi 4 
- If the hardware is configured propperly you should see the LED Display propt you to connect the iOS app

### Hardware List (Raspberry Pi 4)
- Raspbery Pi 4
  - https://www.adafruit.com/product/4296
- Raspbery Pi 4 hdmi cable
  - [Amazon](https://www.amazon.com/UGREEN-Adapter-Ethernet-Compatible-Raspberry/dp/B06WWQ7KLV/ref=sr_1_2_sspa?crid=1TJVR5LOR0ZVQ&dib=eyJ2IjoiMSJ9.mG7d4qh54EEt0ySlw3Qox8Fider4Fqa4TIJ4RvVTUT8RibE054g-2Olxoj0AVMYhcq4W_dbP6ksV4vGkveEgQnM8y23nU_Jysm-nVsRY8-R85reSgPzhdH1hFb_-AvIKrVAUydInu-pvDdsV2PWPyuEEhS_70bPaIZawUehITPM6M6uhSucYKBg0H9AlbjSAAfnLRG_TGcCHtlmnjjMzI59GLkjpOgbFhtT_raRf4xI._pB6ebddXfmq2JEhPSYQ13dGDaIlRoy-J01Dnrcdsx0&dib_tag=se&keywords=raspberry%2Bpi%2B4%2Bhdmi%2Bcable&qid=1720499082&sprefix=raspberry%2Bpi%2B4%2Bhdmi%2Bcable%2Caps%2C134&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
- 32 gb Micro SD Card for Raspberry Pi
  - [Amazon](https://www.amazon.com/SanDisk-Ultra-microSDXC-Memory-Adapter/dp/B073JWXGNT/ref=sr_1_8?crid=3BA0SAU4Z3BVC&dib=eyJ2IjoiMSJ9.gma2hVfUgy-OBJ-COHM6pbshqICnhWgymisufu6qkTikGx9DMDOT-3dc7naXHtt0GM5F7Dc-Kzp8nmsDFj5eZRuSTCXBZHiIuxiikhiAopv-ALnQMJtZZVEZLa4dxi8Tr1MkCnvShyoG4zFOWRbtyg1_XfMy-BaL2RcxbW6T4j0bIq9oyaprOGw9gEz1MJSrd4Xhy54847gErjsLfFbm8xlkS_w2olOighTBk9fXdI329hnd6R0Gkh-Ykuode-GpM0Fs1ZgVM-bJ4eExbhLlgDixoFgMeH63-s7JflFici0.Aj76Y7zJJKxqQMwN3vLCvcBD0_9C8W23b6iYM99UH6c&dib_tag=se&keywords=32+gb+micro+sd&qid=1720498866&s=electronics&sprefix=32+gb+micro+sd%2Celectronics%2C131&sr=1-8)

- gpio extention
  - https://www.adafruit.com/product/2223?gad_source=1&gbraid=0AAAAADx9JvRoR7oa6Xt2MOaaaoUYxxSop&gclid=CjwKCAjwnK60BhA9EiwAmpHZw2OqCtdnE_kqISjUMuYMXSpIDnCF-1EZaFNnZ6MPz9KHeC91vC1JABoCNKQQAvD_BwE
- IPhone (used for LED Board controller)
- Monitor (edit 2 files on Raspberry Pi)
- KeyBoard (edit 2 files on Raspberry Pi) (must use usb)
- Adafruit Matrix Bonnet
  - https://www.adafruit.com/product/3211
- 32 X 64 3mm pitch LED Matrix (Ive found that 3mm is best for Desktop Visibility) (3D files built to support 3mm pitch)
  - [Amazon](https://www.amazon.com/Waveshare-Full-Color-Individual-Adjustable-Brightness/dp/B0B5N5HPKX/ref=sr_1_2?crid=3EE2RLGAFVNC0&dib=eyJ2IjoiMSJ9.6oWrmhaCysWQ6qbBZtvRPtuQFAcbo_KZfVjT3w0WNRURf4c_8LdoDPCJzGhy9tWullLorzWBjrTn1PlSDj-DX7ZxVfj83l0zLvIAVLbHu0bE95X980lZwgOa7jkOEbl_Enki0Q3Jo-yasOGaD7XEsSKcH8O2vhA2hQwktcXNVlq-TFHk7Sfo1ZQ-2zCC3MNrgMAuG0W_xDqNSZJfmaBb1N-TG0UULugbZZ1GlVODYvs.AxmNy8pyNuM09ZaFkDXfzJ-czBjdJapyLn1JC3J6bL0&dib_tag=se&keywords=32+X+64+3mm+pitch+LED+Matrix&qid=1720499174&sprefix=32+x+64+3mm+pitch+led+matrix%2Caps%2C214&sr=8-2)
- 5V 10 Amp charger with Barrel Connector Male (Power both the LED board and Raspberry Pi)
  - [Amazon](https://www.amazon.com/10A-Power-Supply-Adapter-Switching/dp/B07H9XRZBP/ref=sr_1_2?crid=31A60WJNMKB4L&dib=eyJ2IjoiMSJ9.je877a0xnR4pfYxTF_0U6VDr9ZWNS3ATxNAOGSqhnWM__La7IzTYY-_Mg6yM072tnJQ8MZD80hURwLODE9jFtcwCrMps8yq-YBtffrXRhZI8poQBa3unZHCNaHB_90uOPAmM2O-sTZ-_fa6W8CyureTFLDfdoQTdiTz8Bvg_fhH1QWd44OH97XIj0_Qqs0qsn-s-NyyGDLf-SiQkKKxLwJ04E0gCHSD87Zubs4jyWnQ.B6CIy5o4OmhKjVlphmawFai7AqbyU_APljyTN0I94Vw&dib_tag=se&keywords=5V+10+Amp+charger+cool&qid=1720499223&sprefix=5v+10+amp+charger+cool%2Caps%2C99&sr=8-2)
- RaspBerry Pi Brass Spacer Kit with M2 Nuts and Screws
  - [Amazon](https://www.amazon.com/Geekworm-Raspberry-Installation-Standoff-Accessories/dp/B0756CW6Y2/ref=sr_1_6?crid=1WIJ52THVGKAP&dib=eyJ2IjoiMSJ9.4vBz5jbdFFOUtiz9dlUIeNocA1PZrMFELvxfpBsJEauqSijKi8LOeXqvuXxtIXUkgwOsq_9PlPbgfsAGFdJaNxzQZgTj-yARI76t3xqQWNyB9At3IsBCIWPSF6dq5QvkSnASFhCdwWz463ftttUuG7MaqhrD9E-eNHP1ojmMRMxDNMBSbyNPwyLDj4hL06kszQLs6uqNLImpSXhbkOveOf-zzTU06B8clHoEHzymkRY.cGx_1wekEp3kUjAIoMOEXhOosZFJUN_5ML_G8om5nY0&dib_tag=se&keywords=RaspBerry+Pi+Brass+Spacer+Kit&qid=1720499301&sprefix=raspberry+pi+brass+spacer+kit%2Caps%2C102&sr=8-6)
- Solder Iron / Jumper Wire (This can be skipped but reduces quality) (Would also have to reinstall the bonnet library refer to above instructions)
- Access to 3D Printer (for housing)
- Small Skrew Driver
