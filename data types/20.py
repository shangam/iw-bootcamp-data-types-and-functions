#	Write a Python program to count the number of strings where the string
#	length is 2 or more and the first and last character are same from a given list of
#	strings.
#	Sample List : ['abc', 'xyz', 'aba', '1221']
#	Expected Result : 2

l1=['abc','xyz','aba','1231']
a=0
for i in l1:
    if (len(i)>=3) and (i[0]==i[-1]):
        a+=1
print(a)