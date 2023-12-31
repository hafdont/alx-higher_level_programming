#!/usr/bin/python3

# Print the ASCII alphabet in revese order, alternating between upper and lower cases

for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i), end="")
    i -= 32 if i % 2 == 0 else 0
