# String example
import sys
str = input ('Enter a string value : ')
if str.isalpha() == False:
    print ('Error message')
    sys.exit() 
    
elif str.isalpha() == True:
    print (len(str))
if (len(str)%2) == 1:
    print ('odd number')
else:
    print ('even number')
            


    
    
    
