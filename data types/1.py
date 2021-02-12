#	Write a Python program to count the number of characters (character frequency) in a string.
#	Sample String : google.com
#	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


def numbs(word):
    dicts = {}
    for i in word:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    print(dicts)

numbs("sangamb.com.np")