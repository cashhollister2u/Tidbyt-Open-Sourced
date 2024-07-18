from gpiozero import Button
import os
import time 


def button_channel_change(shared_user):
    user = None

    # Pin number where the button is connected
    BUTTON_PIN = 3  # GPIO 3

    possible_channels = ["clock_stock", "stock", "spotify2", "weather"]
    alt_channels = {"invalid_stock": 1, "invalid_zipcode":3, "no_device_active":2, "req_spot_auth":2, "req_stock_api_key":1 , "req_weather_api_key":3}

    press_time = None

    def shutdown_callback():
        print("Shutting down...")
        os.system("sudo shutdown -h now")

    # log initial press and time
    def button_pressed():
        nonlocal press_time
        press_time = time.time()

    # subtract the time when release from when pressed to get duration
    def button_released():
        nonlocal user
        nonlocal press_time
        hold_duration = time.time() - press_time if press_time else None
        press_time = None
        user = shared_user.get_user() # check if user is established

        if hold_duration:
            if hold_duration > 1:
                shutdown_callback()
            elif user:
                print("Short Press detected")
                if user.channel in possible_channels:
                    curernt_index = possible_channels.index(user.channel)
                    new_index = (curernt_index + 1) % len(possible_channels)
                    user.channel = possible_channels[new_index]
                elif user.channel in alt_channels:
                    curernt_index = alt_channels[user.channel]
                    new_index = (curernt_index + 1) % len(possible_channels)
                    user.channel = possible_channels[new_index]
    
    try:
        # Initialize the button with the specified pin
        button = Button(BUTTON_PIN, pull_up=True, hold_time=.05)

        # Attach the callback functions
        button.when_held = button_pressed
        button.when_deactivated = button_released

        print("Monitoring button press. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)  # Keep the thread running
    except Exception as e:
        print(f"An error occurred: {e}")

    print('Script exited for listen button')
