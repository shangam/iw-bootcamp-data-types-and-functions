#	Write a Python program to replace the last element in a list with another list.
#	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

def l_element(l1,l2):
    l1[-1:]=l2
    print(l1)
l_element([1,2,3],[4,5,6])