# Using pprint

import pprint  #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

m = 'a big fat hen'

count = {}

for character in m:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)

# Using Counter

from collections import Counter

m = 'a big fat hen'
count = Counter(m)
print(count)
