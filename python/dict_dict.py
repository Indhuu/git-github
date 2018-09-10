# dictionary of dictionary

family = {
    'dict1':{'father':'Bharath','mother':'Indhu','child':'Sarvesh'},
    'dict2':{'father':'Raj' , 'mother':'jeevitha', 'child':'shruti'},
    'dict3':{'father':'Aravind' ,'mother':'shilpa' , 'child':'krishna'}
    }

for k,v in family.items():
    print ("Key is" +k + "Family members are, Father" + v['father'] + 'and Mother:' + v['mother'] + 'child is:' +v['child'])
    for k1 in v.items():
        print (k1)


       
    
    
   
