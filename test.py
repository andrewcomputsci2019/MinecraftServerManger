import os
import subprocess
import sys
import filecmp
import shutil
import time
from datetime import datetime
stoploop = ''
ThreadWorking = False
ServerStoped = True
wokringdir= os.getcwd()
os.chdir(r"C:\Users\sprgg\Downloads\java server")
server =''
saveTime = 60
SaveTimer= True


#cd C:\Users\sprgg\Downloads\"java server"
#java -Xmx2012M -Xms2012M -jar server.jar

def start():
    global server
    global ServerStoped
    global SaveTimer
    if ServerStoped:
        server = subprocess.Popen("java -Xmx2012M -Xms2012M -jar server.jar --nogui", stdin=subprocess.PIPE, shell=True)
        SaveTimer = True
    else:
        print("server is already running")
    ServerStoped = False
    
def stop():
    global SaveTimer
    global server
    global ServerStoped
    SaveTimer = False
    command("say shuting down server now")
    time.sleep(3)
    server.stdin.write(("stop"+"\n").encode())
    server.stdin.flush()
    server.kill()
    ServerStoped = True
    return 1
    
    
def save():
    global server
    global ServerStoped
    if ServerStoped == False:
        server.stdin.write(("save-all flush"+"\n").encode())
        server.stdin.flush()
    else:
        print("server is not running")

def command(pramater):
    global server
    global ServerStoped
    if ServerStoped == False:
        server.stdin.write((pramater + "\n").encode())
        server.stdin.flush()
        print("excuted command " + pramater)
    else:
        print("server is not running")
#dont use out of date method of running the server
def Main():
    global server
    global ServerStoped
    global stoploop
    global ThreadWorking
    print("entering minecraft server hanlding")
    start()
    print("server started")
    while stoploop!=True:
        try:
            ThreadWorking= False
            time.sleep(saveTime)
            ThreadWorking = True
            save()
        except:
            print("encounter error quiting server handler after killing server")
            server.kill()
            ServerStoped = True
            print("server killed in attempt to deal with error encounterd :(")
            ThreadWorking = False
            stoploop =True
            break;
    
def save_Timer():
    global server
    global ServerStoped
    global SaveTimer

    if SaveTimer:
        try:
            save()
            print(str(datetime.now())+" saved!")
        except:
            print("save did not work killing server :(")
            command("say server is going down due to error on hanlding")
            ServerStoped = True
            try:
                stop()
            except:
                server.kill() # more evnaisve option of killing the server
            SaveTimer = False
