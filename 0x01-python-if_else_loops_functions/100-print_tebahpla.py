#!/usr/bin/python3

# Print the ASCII alphabet in revese order,

for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i), end="")
    i -= 32 if i % 2 == 0 else 0
