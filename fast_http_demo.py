import socket
import ssl
import time

def run():
    start = time.time()

    s = socket.socket()
    s.connect(("chatgpt.alexbers.com", 443))

    context = ssl.create_default_context()
    s = context.wrap_socket(s, server_hostname="chatgpt.alexbers.com")

    # send 1000 requests
    REQ_NUM = 1000

    for i in range(1, REQ_NUM+1):
        connection = "Connection: close" if i == REQ_NUM else "Connection: keep-alive"

        request = f"""GET /small/{i}.txt HTTP/1.1
    Host: chatgpt.alexbers.com
    {connection}
    
    """
        s.sendall(request.replace("\n", "\r\n").encode())


    # get answers

    while True:
        data = s.recv(10000)
        if not data:
            break
    end = time.time()
    return end - start


