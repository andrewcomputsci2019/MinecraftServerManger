import socket
import time
HEADER = 64
Port = 4322
Ip = socket.gethostname()
Format = "utf-8"
Command = "!Command"
Disconnect_message = "!Disconnect"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Ip, Port))


def send(msg):
    message = msg.encode(Format)
    msg_length = len(message)
    send_length = str(msg_length).encode(Format)
    send_length+= b' ' * (HEADER-len(send_length))
    s.send(send_length)
    s.send(message)

def tester():
    send("Hello World!")
    time.sleep(5)
    send("Run")
    time.sleep(30)
    send(Disconnect_message)

def Commandtester():
    send(Command)
    send("time set day")
    time.sleep(10)
    send(Disconnect_message)


def tester2():
    send("Hello World Test2!")
    time.sleep(10)
    send("Close")
    send(Disconnect_message)

case = int(input("enter 1 or 2 or 3"))

if case == 1:
    tester()
elif case == 2:
    Commandtester()
elif case == 3:
    tester2()




