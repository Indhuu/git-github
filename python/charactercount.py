# charater count program

import pprint
message = 'April May June July August September October'
count  ={}
for character in message:
    count.setdefault(character , 0)
    count[character] = count[character] + 1
pprint.pprint (count)
