#	Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def inp(x):
    return x[-1]+x[1:]+x[0]

print(inp("abcd"))