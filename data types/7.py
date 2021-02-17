#	Write a Python function that takes a list of words and returns the length of the longest one.

def inp(x):
    a=[]
    for i in x:
     a.append(len(i))
     return sorted(a)

print(inp(["sangam bhattarai","sangam","bhatta"]))