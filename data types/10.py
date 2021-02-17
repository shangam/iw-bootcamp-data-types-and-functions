#	Write a Python program to remove the characters which have odd index values of a given string.

def inp(x):
    l1=len(x)
    a=""
    for i in range(l1):
       if(i%2==0):
         a+=x[i]
    print(a)

inp("sangam bhattarai")