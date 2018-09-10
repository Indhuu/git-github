# 10 attempt password for loop


Attempt = 1
N = 0
for N in range(5):
    password = input('Enter the password : ')
    if password == 'charu' and Attempt == 1:
        print ('correct password')
        break
    else:
        N += 1
    break    
    print ('5 attemps over. 5 more left')

        
        
    

        
