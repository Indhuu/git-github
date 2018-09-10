# regular expressions

import re
birthdate = re.compile(r'\d\d/\d\d/\d\d\d\d')
print (birthdate.findall('Charu was born on 07/07/2015'))

