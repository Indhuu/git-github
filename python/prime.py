# prime number
N = int (input ('Enter a number : '))
if N > 1:
    for i in range(2,N):
        if (N % i) == 0:
            print (str(N) + " is not a prime number")
            break
    else:
        print (str (N) + " is a prime number")
else:
    print('It is not a prime number')
        


    
    


        
            


    
             
   
