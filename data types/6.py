#	Write a Python program to find the first appearance of the substring 'not' and
#	'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#	substring with 'good'. Return the resulting string.
#	Sample String : 'The lyrics is not that poor!'
#	'The lyrics is poor!'
#	Expected Result : 'The lyrics is good!'
#	'The lyrics is poor!'

def checks(x):
    x1=x.find("not")
    x2=x.find("poor")

    if (x1>x2) and (x2>0):
        x=x.replace(x[-x1],"good")
        print(x)
    else:
        print(x)

checks("the lyrics is not that poor !")