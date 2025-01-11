# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[ 'even' if num%2==0 else 'odd' for num in l1]
# print(l2)

# l2=[ num**2 if num%2==0 else num**3 for num in l1]
# print(l2)

# l3=['maung maung','aung aung','hla hla','su su','mon mon']
# # g => capialize , upper

# l4=[ name.capitalize() if name.endswith('g')  else name.upper()  for name in l3 ]
# print(l4)

# l5 = ['yangon','mandalay','bago','yangon','pathein','mandalay']
# # set 
# l6 =set(l5)
# l7=list(l6)
# print(l7)
# print(l7)

di={ 
    "stu1":{"name":"aung aung","age":20,"city":'Yangon'},
    "stu2":{"name":"su su","age":19,"city":'Bago'},
    }
for key in di: # keys 
    print(key, " ----- ", di[key])

for key,value in di.items():
    if value['name']=='su su':
        print(key)


d1={ "city":"POL","country":'Myanmar','con':True,2:'Two'}
kv=[ type(i) for i  in d1.values() ]
print(kv)



# for stu in di.values():
#     print(f'Name : {stu["name"]} , Age : {stu["age"]} , City : {stu["city"]}')

# print(di)
# print('------------')
# for k,v in di.items():
#     print(k,v)
# print('------------')
# for k in di.keys():
#     print(k)
# print('------------')
# for v in di.values():
#     print(v)

