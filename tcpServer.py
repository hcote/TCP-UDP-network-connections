import socket

def Main():
     # setting server
    host = '127.0.0.1'
    port = 5000

    # setting socket object
    s = socket.socket()
    # bind host and port to socket
    s.bind((host,port))

    # listen for one connection at a time
    s.listen(1)

    # accept the connection with the client and the address it came from
    c, addr = s.accept()


    print('Connection from: ' + str(addr))
    # setting server to run indefinitely
    while True:
        # we will recieve data from the client and will come through as bites, so need to decode it
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print('From connected user: ' + data)
        data = data.upper()

        # senidng data back to the client
        print('Sending: ' + data)
        c.send(data.encode('utf-8'))

    c.close()

if __name__ == '__main__':
    Main()


