#	Write a Python program to get a single string from two given strings, separated
#	by a space and swap the first two characters of each string.
#	Sample String : 'abc', 'xyz'
#	Expected Result : 'xyc abz'

def swaps(x,y): 
 x,y=y,x
 print (x,y)

swaps("abc","xyz")