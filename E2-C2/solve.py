import time
import dns.resolver
import statistics
from concurrent.futures import ThreadPoolExecutor

def read_candidates(filename="suspicious_domains.txt"):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def measure_query_time(domain, resolver, sample_num=0):
    try:
        start = time.perf_counter()
        resolver.resolve(domain, "A")
        end = time.perf_counter()
        return end - start
    except Exception as e:
        print(f"Error querying {domain}: {e}")
        return None

def warmup_query(domain, resolver):
    try:
        resolver.resolve(domain, "A")
    except:
        pass

def identify_hot_domain():
    
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["127.0.0.1"]
    resolver .port =54 
    resolver.timeout = 1.0
    resolver.lifetime = 1.0
    
    candidates = read_candidates()
    print(f"[*] Testing {len(candidates)} candidates")
    
    results = {}
    measurements_per_domain = 5  
    print("[*] Phase 1: Quick screening...")
    for domain in candidates:
        times = []
        
        for i in range(measurements_per_domain):
            warmup_query(domain, resolver)
            time.sleep(0.05)  
            query_time = measure_query_time(domain, resolver)
            if query_time:
                times.append(query_time)
            
            time.sleep(0.1)
        
        if times:
            results[domain] = min(times)
            print(f"  {domain}: {results[domain]:.4f}s (min)")
    
    sorted_results = sorted(results.items(), key=lambda x: x[1])
    
    print("\n[*] Results (fastest first):")
    for domain, query_time in sorted_results[:5]:  
        print(f"  {domain}: {query_time:.4f}s")
    
    if sorted_results:
        hot_domain = sorted_results[0][0]
        print(f"\n[+] Hot domain identified: {hot_domain}")
        return hot_domain
    else:
        print("[-] Could not identify hot domain")
        return None

if __name__ == "__main__":
    identify_hot_domain()