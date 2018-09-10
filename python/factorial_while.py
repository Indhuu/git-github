# factorial using while


def factorial (n):
    i = 1
    while n >= 1:
        i = i * n
        n = n-1

    return i
#value = factorial(5)
#print ('Factorial of 5 is:' +str(value)) 
integer = input('Enter an integer:')
for num in range(1,11):
    factorial(num)
value = factorial(num)
print ('factorial of num is:'+ str(value))
