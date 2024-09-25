import sys
import socket

BUFFERSIZE:int=1024;

recvData:bytes;
clients:list=[];
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);

def main(argc:int, argv:list[str]):
    soc.bind(("0.0.0.0",5050));
    print("Server Running");
    while (True):
        recvData, addr = soc.recvfrom(BUFFERSIZE);
        print(f"recv: {recvData} from: {addr}");

        if (not addr[0] in clients): clients.append(addr[0]);
        for i in clients:
            print(f"recv: {recvData}  |  addr: {addr}  | i:{i}  |  clients: {clients}  |  len: {len(clients)}");
            soc.sendto(recvData, (i,2020));



if (__name__=="__main__"): 
    try:
        main(len(sys.argv), sys.argv);
    except KeyboardInterrupt:
        print("exit: ^C")