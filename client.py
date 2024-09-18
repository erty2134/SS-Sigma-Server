import sys
import socket
import threading

BUFFERSIZE=1024

soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
msg="hello";

def recvFunc():
    while (True):
        print(f"received: {str(soc.recv(BUFFERSIZE))[2:-1]}");
recvThread = threading.Thread(target=recvFunc, daemon=True);

def main(argc:int, argv:list[str]):
    soc.bind(("localhost",2020))

    recvThread.start()
    while (True):
        msg=input("SEND\n");

        soc.sendto(msg.encode("utf-8"), ("localhost",4040))
        



if (__name__=="__main__"): 
    try:
        main(len(sys.argv), sys.argv);
    except KeyboardInterrupt:
        print("exit: ^C")