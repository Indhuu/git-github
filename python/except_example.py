# except_example

print ('How many cats do you have?')
numcats = input()
try:
    if int(numcats) >= 4:
        print ('thats a lot of cats')
    else:
        print('It isnt that many cats')
except:
    print('please enter a number')
