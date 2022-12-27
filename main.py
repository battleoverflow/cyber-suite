import os, sys

class CyberSuite:

    def main(self):

        print("\n")

        print("Available options:")

        print("0 => Anarchy (DDoS)")
        print("1 => Keylogger")

        print("\n")

        print("Choose your script (Type h for help):")

        while True:
            script_name = input("CyberSuite > ")

            if script_name == 'h' or script_name == 'help':

                print("\n")

                print("Commands:")
                print("h, help  Help menu")
                print("e, exit  Exit program")
                print("clear    Clear terminal")

                print("\n")

                print("Available options:")

                print("0 => Anarchy (DDoS)")
                print("1 => Keylogger")

                print("\n")
            elif script_name == 'clear':
                os.system('clear')
            elif script_name == '0':
                os.system("python3 scripts/ddos/anarchy.py")
            elif script_name == '1':
                os.system("python3 scripts/keylogger/keylogger.py")
            elif script_name == 'e' or script_name == 'exit':
                print("\nThank you for checking out my personal Cyber Suite! - azazelm3dj3d")
                print("Author: https://github.com/azazelm3dj3d")
                sys.exit(0)
            else:
                print(f"Command {script_name} not found")

if __name__ == '__main__':
    CS = CyberSuite()
    CS.main()