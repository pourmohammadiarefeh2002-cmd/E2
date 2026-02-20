# Ex5: Vampire DDoS (Regex backtracking DoS)

Goal
- A web endpoint uses a vulnerable regular expression.
- You can trigger catastrophic backtracking to slow the server.
- The server prints a flag after it detects sustained slowness.

## SOLUTION

in this question the server needs to pars a reg experession, which can use to exploit the server, assuem that i send the string aaaa@example.co, when the parser pars the string it assumes that the string is like when ther is 4 a in the inner () and the * = 1
meaning the string is:
(aaaa)^1 @example.cp
the parser sees the error so it says i parsed wrongly so tries another way 
it assumes that in the inner () is "aa" and * = 2 so the reg is:
(aa)^2@example.co 
but again it sees error so this time assumes that in the inner () is a and * = 4 this time the same error it sees. 

in the example the numebr of the a was limited but in my code I tested from 30*a to 200*a with 10 as step and in the #a = 30 the exploit happens. 