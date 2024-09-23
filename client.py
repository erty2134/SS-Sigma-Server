import sys
import socket
import threading
import os

BUFFERSIZE=1024

class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
msg="hello";
hostIP:str="localhost";

connected:bool=False;

def recvFunc():
    while (True):
        print(f"received: {str(soc.recv(BUFFERSIZE))[2:-1]}");
recvThread = threading.Thread(target=recvFunc, daemon=True);

def main(argc:int, argv:list[str]):
    soc.bind(("0.0.0.0",2020));

    while (not connected):
        hostIP=str(input("connect: "));

        try:
            soc.sendto("PING".encode("utf-8"),(str(hostIP),5050));
            print(f"ECHO: {str(soc.recv(BUFFERSIZE))[2:-1]}" );
        except:
            print(f"{BCOLORS.FAIL}BindError: Did Not Reconize IP \"{hostIP}\" %s"%BCOLORS.ENDC);
            print("Enter new IP");
            connected=False;

    print(f"connected to {hostIP} \n (ping sent and received)");

    recvThread.start()
    while (True):
        msg=str(input("SEND\n"));
        if(msg[0:2]=="::"):
            if(msg[2:len(msg)]=="clear"):
                try:
                    os.system("clear");
                except:
                    os.system("cls");
            
            elif(msg[2:len(msg)]=="spam"):
                print(int(msg[8:len(str(msg))]));
                for i in range(10):
                    soc.sendto(str("*"*1000).encode("utf-8"), (str(hostIP),5050));

            else:
                print(f"{BCOLORS.FAIL}CLIError: \"{msg[2:len(msg)]}\" is not a valid command!%s"%BCOLORS.ENDC);
        else: pass
        soc.sendto(msg.encode("utf-8"), (str(hostIP),5050));
        



if (__name__=="__main__"): 
    try:
        main(len(sys.argv), sys.argv);
    except KeyboardInterrupt:
        print("exit: ^C")