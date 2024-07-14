#!/bin/bash


# alter permissions to write and read to error log
chmod 666 error_log.txt
echo "changed permissions on error log file"

# alter permissions for writing and reading token file 
chmod 666 spotify_refresh_token.json
echo "changed permissions on spotify refresh token file"

# make the off command executable
chmod +x off_command.py
echo " off command file is now executable"

# change sudoers file to allow for shutdown w/out password
SUDOERS_TEMP_FILE="/tmp/sudoers.temp"
echo "ALL ALL=NOPASSWD: /sbin/shutdown" | sudo tee -a $SUDOERS_TEMP_FILE > /dev/null # write command to temp file
sudo visudo -cf $SUDOERS_TEMP_FILE && sudo cp $SUDOERS_TEMP_FILE /etc/sudoers.d/ # if format is correct copy it to the sudoers dir
shutdown_nopasswd # name of file
echo "Sudoers file updated to allow shutdown without password"

# turn off sound module
BLACKLIST_FILE="/etc/modprobe.d/blacklist-sound.conf"
echo "blacklist snd_bcm2835" | sudo tee $BLACKLIST_FILE > /dev/null
echo "Blacklist file created at $BLACKLIST_FILE to blacklist snd_bcm2835"

# install flask
sudo apt-get install python3-flask

# Append isolcpus=3 to /boot/firmware/cmdline.txt for better visual quality
CMDLINE_FILE="/boot/firmware/cmdline.txt"
if grep -q "isolcpus=3" $CMDLINE_FILE; then
    echo "isolcpus=3 is already present in $CMDLINE_FILE"
else
    echo "Appending isolcpus=3 to $CMDLINE_FILE"
    sudo sed -i '$ s/$/ isolcpus=3/' $CMDLINE_FILE
    echo "isolcpus=3 added to $CMDLINE_FILE"
fi

# Create and configure the led_app.service file
SERVICE_FILE="/etc/systemd/system/led_app.service" # path to systemctl file
sudo tee $SERVICE_FILE > /dev/null <<EOL # write the following to said file
[Unit]
Description=Led App Service
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/home/led_app/Led_App_Prod       
ExecStart=/usr/bin/python3 /home/led_app/Led_App_Prod/main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOL
echo "Service file created at $SERVICE_FILE"

# Reload the systemd daemon to recognize the new service
sudo systemctl daemon-reload

# Enable the new service to start on boot
sudo systemctl enable led_app.service

# Start the new service immediately
sudo systemctl start led_app.service
echo "led_app.service has been started and enabled to start on boot"

# download adafruit matrix driver
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh

# run demo file to test board
sudo ./demo -D0 --led-rows=32 --led-cols=64