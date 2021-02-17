#	Write a Python program to check a list is empty or not.

def inp(x):
    if (len(x)>0):
        return "it's not empty"
    else:
        return "it's empty"

print(inp([0]))