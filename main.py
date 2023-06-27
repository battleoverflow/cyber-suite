import os, sys

from scripts.anarchy import anarchy
from scripts.keylogger import keylogger

def main():
    print("\nAvailable options:")
    print("0 => Anarchy (DDoS)")
    print("1 => Keylogger")
    print("\nChoose your script (Type h for help):")

    while True:
        script_name = input("CyberSuite > ")

        if script_name == "h" or script_name == "help":
            print("\nCommands:")
            print("h, help  Help menu")
            print("e, exit  Exit program")
            print("clear    Clear terminal")

            print("\nAvailable options:")
            print("0 => Anarchy (DDoS)")
            print("1 => Keylogger")
            print("\n")
        elif script_name == "clear":
            os.system("clear")
        elif script_name == "0" or script_name == "anarcy":
            target_ip = input("IP Address: ")
            port = input("Port: ")
            anarchy(target_ip, port)
        elif script_name == "1" or script_name == "keylogger":
            keylogger()
        elif script_name == "e" or script_name == "exit":
            print("Author: azazelm3dj3d (https://github.com/azazelm3dj3d)")
            sys.exit(0)
        else:
            print(f"'{script_name}' command not found")

if __name__ == '__main__':
    main()
