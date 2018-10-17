import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    # socket is tcp by default, so this is required to specify udp connection
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('Server Started')
    while True:
        # udp is connectionless, we don't have a connection to recieve from
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Message from: ' + str(addr))
        print('From connected user: ' + data)
        data = data.upper()
        print('Sending: ' + data)
        s.sendto(data.encode('utf-8'), addr)

    c.close()

if __name__ == '__main__':
    Main()
