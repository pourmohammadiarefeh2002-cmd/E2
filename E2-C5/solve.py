#!/usr/bin/env python3
import socket
import time

def solve():
    host = 'localhost'
    port = 5555
    
    print(f"[*] Connecting to {host}:{port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Receive initial message
    data = sock.recv(1024).decode()
    print(f"[*] {data.strip()}")
    
    jam_count = 0
    expected_jams = 3
        
    while True:
        line = sock.recv(1024).decode().strip()
        print(f"  {line}")
        
        # Wait for data frame end
        line = sock.recv(1024).decode().strip()
        print(f"  {line}")
        
        # Wait for SIFS wait
        line = sock.recv(1024).decode().strip()
        print(f"  {line}")
        
        # Wait for ACK window open
        line = sock.recv(1024).decode().strip()
        print(f"  {line}")
        
        if "ACK_WINDOW_OPEN" in line:
            print(f"[*] Jamming ACK #{jam_count + 1}...")
            sock.send(b"JAM\n")
            
            result = sock.recv(1024).decode().strip()
            print(f"  {result}")
            
            if "JAMMED" in result:
                jam_count += 1
                print(f"[+] Successful jam! Progress: {jam_count}/{expected_jams}")
                
                if jam_count >= expected_jams:
                    time.sleep(0.1)
                    
                    try:
                        sock.settimeout(0.5)
                        flag_data = sock.recv(1024).decode().strip()
                        
                        if flag_data and ("CTF{" in flag_data or "SELECTIVE_JAM" in flag_data):
                            print(f"\n[+] FLAG FOUND: {flag_data}")
                            return flag_data
                        else:
                            # If not, maybe it's the next event and the flag was sent with the result
                            # Let's check if the result actually contained the flag
                            if "CTF{" in result or "SELECTIVE_JAM" in result:
                                print(f"\n[+] FLAG FOUND IN RESULT: {result}")
                                return result
                    except socket.timeout:
                        pass
            else:
                print("[-] Jam failed? Resetting counter")
                jam_count = 0
    
    sock.close()

if __name__ == "__main__":
    solve()