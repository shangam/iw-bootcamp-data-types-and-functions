#	Write a Python script to check whether a given key already exists in a dictionary.

d={1:20,2:40,3:60}
def ch(x):
    if x in d:
        print("key is there")
    else:
        print("not key")

ch(4)