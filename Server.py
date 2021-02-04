import socket
import codecs
import threading
import test
ContinueSaving = True
saveInterval = 120
#MainThread= threading.Thread(target=test.Main, name="Server")
Running = False
Header = 64
IP = socket.gethostname()
port = 4322
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, port))
Format = 'utf-8'
Disconnect_Message = "!Disconnect"

def Boot_Up_Server():
    #global MainThread
    global Running
    global ContinueSaving
    if Running == False:
        ContinueSaving = True
        print("accesssing new server")
        test.stoploop= False
        test.start()
        StartSaving()
    Running = True
    
def Close_Server():
    #global MainThread
    global Running
    global ContinueSaving
    if test.ServerStoped == False:
        print("shuting down server")
        ContinueSaving = False
        Running = False
        test.stop()
    else:
        print("server thread is not running right now either crashed or server is not being used")
        Running = False
    
    
def redefine_thread():
   # global MainThread
    MainThread = threading.Thread(target=test.Main, name="Server")

def StartSaving():
    global ContinueSaving
    if ContinueSaving==True:
        test.save_Timer()
        threading.Timer(saveInterval,StartSaving).start() #recursive threading 
    else:
        print("stoped saving and thread has been stoped")
        
def handle_client(conn, adder):
   
    print(f"[NEW CONNECTION] {adder} connected")
    connected =True
    while connected:
        msg_length = conn.recv(Header).decode(Format)
        if msg_length:
            msg_length= int(msg_length)
            msg = conn.recv(msg_length).decode(Format)
            if msg == Disconnect_Message:
                print(f"client disconnecting adress is {adder}")
                connected = False
                break;
            print(f"[{adder}] {msg}")
            if msg== "Run":
                print("booting up minecraft server")
                Boot_Up_Server()
            if msg == "Close":
                Close_Server()
            if msg == "!Command":
                commandlen = conn.recv(Header).decode(Format)
                if commandlen:
                    commandlen = int(commandlen)
                    command = conn.recv(commandlen).decode(Format)
                    test.command(command)
    print("exited loop")           
    conn.close()
    

def start():
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target= handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("server is staring")
start()


#we can still use other methods then main method becuase of the threading locking