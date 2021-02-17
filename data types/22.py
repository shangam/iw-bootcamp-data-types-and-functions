#	Write a Python program to remove duplicates from a list

x=[1,2,3,12,3,4,1]
dup=set()
for i in x:
    if i not in dup:
        dup.add(i)
print(dup)