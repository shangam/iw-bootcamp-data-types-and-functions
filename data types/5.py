#	Write a Python program to add 'ing' at the end of a given string (length should
#	be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#	string length of the given string is less than 3, leave it unchanged.
#	Sample String : 'abc'
#	Expected Result : 'abcing'
#	Sample String : 'string'
#	Expected Result : 'stringly'

def changes(x):
    a=len(x)
    if(a<3):
        return a
    if (a>=3):
        ch=x[-3:]

        if (ch=="ing"):
            return x+"ly"
        else:
            return x+"ing"         
    
print(changes("string"))