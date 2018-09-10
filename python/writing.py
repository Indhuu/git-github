# writing
'''
helloFile = open ('C:\\Users\\Indhu\\Desktop\\python_video\\hello2.txt',  'w')    
A = helloFile.write('Hello!!!!')
helloFile.close()
print (A)
'''

baconFile = open('Bacon.txt','w')
print (baconFile.write('Bacon is not a vegetable'))
baconFile.close()

import os
print (os.getcwd())
baconFile = open ('Bacon.txt','a')
print (baconFile.write('\nBacon is delicious'))
baconFile.close()
