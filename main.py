import threading
import time

from Main_Components.display_select import display_loop
from Main_Components.http_server import run_flask_server, user, shared_user

if __name__ == "__main__":
     # run flask app in threaded instance
     thread = threading.Thread(target=run_flask_server)
     thread.daemon = True
     thread.start()
     
     time.sleep(1) # a bandaid for the race condition between flask and display_loop

     display_loop(user=user, shared_user=shared_user)