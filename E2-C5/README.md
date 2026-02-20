# Ex6: Silent Jammer (selective jamming)

Goal
- A sender transmits frames.
- A receiver sends an ACK when a frame is correct.
- You can jam only the ACK at the right time.
- If you jam too much, the receiver detects you.

## SOLUTION
in this qiestion first i wait for the each following lines to recieve after that i sent 3 "jamming" messages:

"--- RF LINK ESTABLISHED ---\n"
"EVENT: DATA_FRAME_START\n"
"EVENT: DATA_FRAME_END\n"
"EVENT: SIFS_WAIT\n"
"EVENT: ACK_WINDOW_OPEN\n"

then i looked for the flag in the recieved messages. 
the result is in the image in the same directory. y
