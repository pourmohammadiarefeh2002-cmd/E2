# Ex7: SNI Ghost (domain fronting toy model)

Goal
- A middlebox blocks requests if it sees `forbidden.com` early in the connection.
- The origin server chooses content based on the `Host:` header.
- If you can make the middlebox see only `allowed.com` early, you can still reach the forbidden host at the origin.

### SOLUTION

We need to ensure "forbidden.com" appears AFTER the first 64 bytes. We need to send more than 64 bytes that don't contain forbidden.com. Then send the rest with the Host header. Actually, we use the fact that the middlebox only checks first 64 bytes.
    

    
    

