#	Write a Python program to remove the nth index character from a non-empty string.

def rem(x,num):
    return x[:num]+x[num+1:]

print(rem("sangam",5))