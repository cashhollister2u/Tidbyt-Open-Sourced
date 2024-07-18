#!/bin/bash

# alter permissions to write and read to error log
chmod 666 /home/led_app/Tidbyt-Open-Sourced/Error_Logs/error_log.txt
echo "changed permissions on error log file"

# alter permissions for writing and reading token file 
chmod 666 /home/led_app/Tidbyt-Open-Sourced/Secrets/spotify_refresh_token.json
echo "changed permissions on spotify refresh token file"

# make the off command executable
chmod +x /home/led_app/Tidbyt-Open-Sourced/Bash_Scripts/off_command.py
echo " off command file is now executable"

# change sudoers file to allow for shutdown w/out password
SUDOERS_TEMP_FILE="/tmp/sudoers.temp"
echo "ALL ALL=NOPASSWD: /sbin/shutdown" | sudo tee -a $SUDOERS_TEMP_FILE > /dev/null # write command to temp file
sudo visudo -cf $SUDOERS_TEMP_FILE && sudo cp $SUDOERS_TEMP_FILE /etc/sudoers.d/shutdown_nopasswd # if format is correct copy it to the sudoers dir
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


# Create and configure the loading_display.service file
SERVICE_FILE="/etc/systemd/system/loading_display.service" # path to systemctl file
sudo tee $SERVICE_FILE > /dev/null <<EOL # write the following to said file
[Unit]
Description=Led App loading

[Service]
User=root
Group=root
WorkingDirectory=/home/led_app/Tidbyt-Open-Sourced       
ExecStart=/usr/bin/python3 /home/led_app/Tidbyt-Open-Sourced/loading.py
Restart=always

[Install]
WantedBy=multi-user.target
EOL
echo "Service file created at $SERVICE_FILE"

# Reload the systemd daemon to recognize the new service
sudo systemctl daemon-reload

# Enable the new service to start on boot
sudo systemctl enable loading_display.service

# Start the new service immediately
sudo systemctl start loading_display.service
echo "loading_display.service has been started and enabled to start on boot"


# Create and configure the led_app.service file
SERVICE_FILE="/etc/systemd/system/led_app.service" # path to systemctl file
sudo tee $SERVICE_FILE > /dev/null <<EOL # write the following to said file
[Unit]
Description=Led App Service
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/home/led_app/Tidbyt-Open-Sourced       
ExecStart=/usr/bin/python3 /home/led_app/Tidbyt-Open-Sourced/main.py
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

# input api keys into api_keys.py
# Prompt the user for Spotify inputs
read -p "Enter your Spotify Client ID: " spotify_client_id
read -p "Enter your Spotify Client Secret: " spotify_client_secret

# Prompt the user for Twelve Data API key
read -p "Enter your Twelve Data API Key: " twelve_api_key

# Prompt the user for OpenWeatherMap API key
read -p "Enter your OpenWeatherMap API Key: " weather_api_key

# Path to the api_keys.py file
API_KEYS_FILE="/home/led_app/Tidbyt-Open-Sourced/Secrets/api_keys.py"

# Insert the inputs into the api_keys.py file using sed
sed -i "s|CLIENT_ID = \"\"|CLIENT_ID = \"$spotify_client_id\"|" $API_KEYS_FILE
sed -i "s|CLIENT_SECRET = \"\"|CLIENT_SECRET = \"$spotify_client_secret\"|" $API_KEYS_FILE
sed -i "s|TWELVE_API_KEY = \"\"|TWELVE_API_KEY = \"$twelve_api_key\"|" $API_KEYS_FILE
sed -i "s|WEATHER_API_KEY = \"\"|WEATHER_API_KEY = \"$weather_api_key\"|" $API_KEYS_FILE

echo "API keys have been set in $API_KEYS_FILE."

# Prompt the user for zip code 
read -p "Enter the zip code: " zip_code

# Prompt the user for stock
read -p "Enter the stock: " stock

# Create the JSON file and write the user inputs
cat <<EOF > /home/led_app/Tidbyt-Open-Sourced/Secrets/user_inputs.json
{
    "zip_code": "$zip_code",
    "stock": "$stock",
    "channel": "weather"
}
EOF

chmod 666 /home/led_app/Tidbyt-Open-Sourced/Secrets/user_inputs.json
echo "user_inputs.json has been created with the provided values."

# download adafruit matrix driver
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh

