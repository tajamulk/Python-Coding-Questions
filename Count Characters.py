# Using for loop
import pprint  #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

m = 'a big fat hen'

dict = {}

for character in m:
    dict.setdefault(character, 0)
    dict[character] += 1

pprint.pprint(dict)

# For Loop Counter
m = 'a big fat hen'
dict = {}

for character in m:
    if character in dict:
        dict[character] += 1
    else:
        dict[character] = 1

print(dict)

# Using Counter for Strings, Lists, Tuples - Easy

from collections import Counter

m = 'a big fat hen'

countm = Counter(m)
print(countm)