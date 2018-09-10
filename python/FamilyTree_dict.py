# Family Tree Dict
familyTree = {}
for i in range(2):
    fatherSon = input ('Enter Father : Son pair ')
    (father,son) = fatherSon.split(':')
    familyTree[father] = son
    print (father)
print (familyTree)
