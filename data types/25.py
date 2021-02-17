#	Write a Python program to check whether all dictionaries in a list are empty or not.
#	Sample list : [{},{},{}]
#	Return value : True
#	Sample list : [{1,2},{},{}]
#	Return value : False

def dict_check(dicts):
 
 print(all(not  checks for checks in dicts ))
 
dict_check([{},{},{1,2}])