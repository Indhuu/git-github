# nested for loop[list]

list1 = []
for i in range(5):
    for j in range(5):
        list1.append([i,j])

print (list1)

# nested for loop dict

dict1 = {}
for i in range(10):
    for j in range(5):
        dict1.setdefault(i,[]).append(j)
print (dict1)

        
        
        
                

