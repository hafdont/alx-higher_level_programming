#!/usr/bin/python3

# Print the ASCII alphabet in revese order,

output = ""

for i in range(ord('z'), ord('a') - 1, -1):
    output += chr(i)
    i -= 32 if i % 2 == 0 else 0

print(output)
