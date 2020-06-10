# Problem: https://open.kattis.com/problems/avion

# External imports
import sys

# Init var
cia_blimps = []
index = 1

# Check if each blimp belongs to the FBI. If it does,
# append the index of the blimp to the cia blimp list
for line in sys.stdin:
    if "FBI" in line:
        cia_blimps.append(index)
    index += 1

# If there are any entries in the cia blimp list, print them,
# space separated. If there are not, indicate that no cia
# blimps were found
if len(cia_blimps) > 0:
    print(*cia_blimps)
else:
    print("HE GOT AWAY!")
