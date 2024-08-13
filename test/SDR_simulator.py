import socket

HOST = "192.168.0.2"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b"FFT-Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")