# Ex2: Oracles Pulse (DNS timing side channel)

Goal
- A resolver caches DNS answers.
- A bot keeps one internal domain hot in cache.

# NOTE 

I was not able to build docker compose due to network errors so I run the python files on my system, to avoid port conflicts i changed the port from 53 to 54.

### SOLUTION 

The upstream DNS server introduces a 200ms delay for all queries, making cached responses significantly faster than uncached ones. The solution implements a warmup-then-measure strategy for each candidate domain from suspicious_domains.txt, performing multiple measurements and taking the minimum response time to minimize network variance. By configuring the resolver to target the local upstream server on port 54 and using careful timing with small delays between measurements to avoid interference, the script successfully identifies the cached domain with the consistently fastest response time.