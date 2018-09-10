# join operator

'''
fruits = input('fruits name:')
fruits = fruits.split(',')
print (fruits)
A = ':'.join(fruits)
print(A)




fruitlist = []
for i in range(3):
    print ('Enter the fruit name for index: ' + str(i))
    fruit = input()
    fruitlist.append(fruit)
A = ':'.join(fruitlist)
print (A)    

'''

fruitlist = []
i = 1
while i <= 3:
    print ('Enter the fruit name for index: ' + str(i))
    i += 1
    fruit = input()    
    fruitlist.append(fruit)
    
A = ':'.join(fruitlist)
print (A) 
    
