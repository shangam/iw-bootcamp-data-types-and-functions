#	Write a Python program to count the occurrences of each word in a given sentence.

def inp(x):
    occ={}
    x=x.split()
    for i in x:
        if i in occ:
            occ[i]+=1
        else:
            occ[i]=1
    return occ
print(inp("I am Sangam Bhattarai"))