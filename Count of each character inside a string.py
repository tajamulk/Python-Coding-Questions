# Using pprint

import pprint  #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

m = 'a big fat hen'

dict = {}

for character in m:
    dict.setdefault(character, 0)
    dict[character] += 1

pprint.pprint(dict)

# Using Counter

from collections import Counter

m = 'a big fat hen'
dict = Counter(m)
print(dict)

# Simple Way

m = 'a big fat hen'
dict = {}

for character in m:
    if character in dict:
        dict[character] += 1
    else:
        dict[character] = 1

print(dict)
