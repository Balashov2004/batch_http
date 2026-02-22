import socket
import ssl


HOST = "chatgpt.alexbers.com"
PORT = 443
TOTAL_REQUESTS = 1000
CONNECTIONS = 10


def worker(start_i, end_i):
    s = socket.socket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((HOST, PORT))

    context = ssl.create_default_context()
    s = context.wrap_socket(s, server_hostname=HOST)

    for i in range(start_i, end_i + 1):
        connection = "Connection: close" if i == end_i else "Connection: keep-alive"

        request = f"""GET /small/{i}.txt HTTP/1.1
Host: {HOST}
{connection}

"""
        s.sendall(request.replace("\n", "\r\n").encode())

    while True:
        data = s.recv(65536)
        if not data:
            break

    s.close()