# example


# dictionary of list
fruits = ['apple','mango', 'orange']
vegetables = ['carrot','peas','beans']
dict1 = {'fruits':fruits , 'vegetables':vegetables}
print (dict1)
for k,v in dict1.items():
    print (k,v)

# dictionary of dictionaries
my_dict={
'charu':{'painting':100,'puzzle':100},
'milo':{'painting':90,'puzzle':95}
}
print (my_dict['charu']['painting'])
