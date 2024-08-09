import pprint #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly

m = 'a big fat hen'

count = {}

for character in m.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
