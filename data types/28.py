#	Write a Python script to add a key to a dictionary.
#	Sample Dictionary : {0: 10, 1: 20}
#	Expected Result : {0: 10, 1: 20, 2: 30}

m1={1:2,4:5}
m={6:8}
m.update(m1)
print(m)