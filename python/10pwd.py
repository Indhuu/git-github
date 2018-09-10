# 10 attempt password

N = 0
while True:
    password = input('Enter the password : ')
    N = N+1
    if N == 5:
        print ('5 Attemps over. 5 more left')
        
    elif N == 10:
        print('incorrect password')
        break
    elif password == 'charu':
        print ('correct password')
        break
    
        
        
                
        
    
