# Ex4: DoH Whispers (size fingerprinting)

Goal
- The capture is encrypted-like traffic, but the response sizes leak which domain was queried.
- Your job is to map each query to a domain using only packet sizes.

### SOLUTION

By analyzing the UDP traffic on ports 4433/44333 in the provided pcap file, I observe a clear pattern: each query (49-byte packet) is followed by a response from the server with one of three distinct sizes (45, 51, or 71 bytes). These size differences correspond to different DNS response types—NXDOMAIN responses are smallest, single A record responses are medium, and responses with multiple records or CNAMEs are largest.

Using the assumption that response sizes sorted from smallest to largest map to the candidate domains sorted alphabetically, I can fingerprint each transaction. The 45-byte responses correspond to "medium-site.com" (likely NXDOMAIN), 51-byte responses to "short.com" (single A record), and 71-byte responses to "super-secret-whistleblower-site.org" (multiple records)
