#!/usr/bin/python3

# Print the ASCII alphabet in revese order,

# Print the ASCII alphabet in reverse order, alternating upper and lower cases

output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    output += "{:c}".format(i) if i % 2 == 0 else "{:c}".format(i -32)

print(output, end="")
