clients=['127.0.0.1','192.0.0.1']
recvData=b'hello'
addr=('127.0.0.1', 4040)

for i in clients:
            print(f"recv: {recvData}  |  addr: {addr}  | i:{i}  |  clients: {clients}  |  len: {len(clients)}");