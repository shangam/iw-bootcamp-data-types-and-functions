#	Write a Python program to sum all the items in a list.

def inp(x):
    a=0
    for i in range(len(x)):
     a+=x[i]
    return a
print(inp([1,2]))