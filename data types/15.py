#	Write a Python function to insert a string in the middle of a string.
#	Sample function and result :
#	insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#	insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def mid_st(x, val):
	return x[:2] + val + x[2:]

print(mid_st("[[]]","python"))