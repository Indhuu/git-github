# Multiples of 5
'''
# total = 0
total = 1
for i in range(5,101,5):
    total = total * i
    #total = total+i
print (total)'''


N = 0
while True:
    password = input('Enter the password:')
    N = N+1
    if N == 5:
        print ('Access Denied')
        break
    elif password == 'charu':
        print ('Access Granted')
        break









