# Using for loop
import pprint  #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

m = 'a big fat hen'

dict = {}

for character in m:
    dict.setdefault(character, 0)
    dict[character] += 1

pprint.pprint(dict)

# Simple way 
m = 'a big fat hen'
dict = {}

for character in m:
    if character in dict:
        dict[character] += 1
    else:
        dict[character] = 1

print(dict)

# Using Counter for Strings, Lists, Tuples

from collections import Counter

l = ('a', 'b', 'z')
m = ['a', 'b', 'c']
n = "a big fat hen"

countl = Counter(l)
countm = Counter(m)
countn = Counter(n)

print(countl)
print(countm)
print(countn)
