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


