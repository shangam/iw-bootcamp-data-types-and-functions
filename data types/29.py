#	Write a Python script to concatenate following dictionaries to create a new one.
#	Sample Dictionary :
#	dic1={1:10, 2:20}
#	dic2={3:30, 4:40}
#	dic3={5:50,6:60}
#	Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d1={"a":"nir","b":"aja"}
d2={"v":"jan"}
d3={"k":"dhakal"}
d4={}
for a in (d1,d2,d3):d4.update(a)
print(d4)