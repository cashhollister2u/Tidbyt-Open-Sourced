import threading
import time

from Main_Components.display_select import display_loop
from Main_Components.http_server import run_flask_server, shared_user
from Main_Components.push_button import button_channel_change

if __name__ == "__main__":
     # run flask app in threaded instance
     thread = threading.Thread(target=run_flask_server)
     thread.daemon = True
     thread.start()

     button_controller = threading.Thread(target=button_channel_change, args=(shared_user,))
     button_controller.daemon = True
     button_controller.start()
     
     time.sleep(1) # a bandaid for the race condition between flask and display_loop

     display_loop(shared_user=shared_user)
