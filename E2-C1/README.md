# Ex1: The Ghost in the Stream (TCP reassembly mismatch)

Goal
- A “smart” middlebox firewall inspects TCP payloads and blocks the string `GIMME_FLAG`.
- The firewall and the server reassemble overlapping TCP segments differently.

## SOLUTION

As explained in the comments of the firewall, it just checks the current packet but the server do the normal packet construction, so as a result i sent "GIMME" in one packet and "_FLAG" in another packet the firewall inspect each one seprately but the server see them in a stream and returns the flag. 
the result is shown in the picture in the same directory. 