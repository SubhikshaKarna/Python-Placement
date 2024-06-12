thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

thisdict2=dict(name="John",age=36,country="NewYork")
print(thisdict2)

#Creating an Empty Dictionary
my_dict={}

#Adding Key-value pairs to the Dictionary

my_dict['name']='Alice'
my_dict['age']=30
my_dict['city']='New York'

#Accessing 

print("Name:",my_dict['name'])
print("Age:",my_dict['age'])
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)
m=my_dict.get("city")
print(m)


for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])

#Iterating  over keys
print("Keys:")
for key in my_dict.keys():
    print(key)

#Iterating Over Values
print("values:")
for value in my_dict.values():
    print(value)

#iterating over key-value pairs
print("key-value Pairs:")
for key,value in my_dict.items():
    print(key,":",value)

#Checking if a key exists

if 'name' in my_dict:
    print("'name' exists in the Dictionary")
else:
    print("'name' does not exist in the Dictionary")

#Modifying

my_dict['age']=35
print("Modified  Age:",my_dict['age'])

my_dict.update({"age":45})

#Adding to Dictionary
my_dict["color1"]="fair"
print(my_dict)

my_dict.update({"color2":"dark"})

#Removing a key-value pair

removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print("Dictionary after Clearing:",my_dict)

del my_dict
print(my_dict)