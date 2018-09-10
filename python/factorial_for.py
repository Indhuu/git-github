# factorial program

def factorial(N):
    ans = 1
    for i in range(1,N+1):
        ans = ans * i
    print ('Retrieved factorial value for:' +str(N) + 'is :' +str(ans))
    return ans
value = factorial(4)
print ('Factorial of 4 is:' +str(value))        
        
