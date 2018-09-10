# nested for loop

list1 = []
dict1 = {}
for i in range(5):
    
    for j in range(5):
        dict1[i] = j
    list1.append(dict1)
print (list1)
        
        
