#print("Hello Python")

#print("Hello Automation Testing")

name = "Tun Tun"
# print("My name " + name)
# print("My name " + name)
# print("My name " + name)
# print("My name " + name)
# print("My name", name)
# print("My name", name)

a = 10
b = 20
result = a + b

#print(f"{a} + {b} = {result}")

#Python Data Type
a = 10
b = "Hi July"
c = 10.5

# print(type(a))
# print(type(b))
# print(type(c))


"""
    Standard Data Type
1, Numbers      (Interger, Float, Complex Number)
2, Squence Type  (String, List, Tuple)
3, Boolean
4, Set
5, Dictionary
"""

c = 1+2j
#print(type(c))

str = "string 'value'"
#print(type(str))
str1 = 'string value 1'
#print(str1)
str2 = ''' <html>
                <head>
                    <title></title>
                </head>
                <body>
                </body>
            </html>
'''

#print(str2)
str1 = 'hello Testing QA Automation '
str2 = 'hello Selenium Python Testing'

print(str1[6:16])
print("="*35)
#print(str1 + str2)
#print(str1[-1:-10:-2])

name = "Maung Maung", "Aung Aung"
#print(name)
#print(type(name))

list1 = []
tuple1 = ()
set1 = {}
dic = {name:"Maung Maung"}
# print(type(list1))
# print(type(tuple1))
# print(type(set1))
# print(type(dic))

list2= ["String", True, 10, 34.4, 1+2j]
list2[1] = "Testing"

for i in list2:
    print(i)
print("=" * 30)
tuple2 = ("String", True, 10, 34.4, 1+2j)

#tuple2[1] = "Testing"

for i in tuple2:
    print(i)
print("="*30)

set2 = {"Apple", "Orange", "Banana", "Lemo", "Apple", "Banana"}

for i in set2:
    print(i)
