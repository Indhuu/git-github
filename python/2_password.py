# 2 password


for N in range(5):
    entered_password1 = input('Enter Password 1 : ')
    entered_password2 = input('Enter Password 2 : ')
    password1 = entered_password1.lower()
    password2 = entered_password2.lower()
    if password1 == 'charu' and password2 == 'indhu':
        print ('correct password')        
        break
    elif password1 != 'charu' and password2 == 'indhu':
        print ('password 1 is incorrect.')
    elif password1 == 'charu' and (password2 != 'indhu'):
        print ('password 2 is incorrect.')
    else:
        print ('Both passwords are incorrect')
           
    if ((N == 4) and (password1 != 'charu') and (password2 != 'indhu') ):
        print ('incorrect password. All 5 Attempts expired ')
        
dict1 = {}
'''
dict1.setdefault('password1',password1)
dict1.setdefault('password2',password2)
'''

dict1['password1']= entered_password1
dict1['password2']= entered_password2


print ('The password dictionary is : ' + str(dict1))


