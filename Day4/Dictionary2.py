myFamily={
    "child1":{
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Tobias",
        "year":2007
    },
    "child3":{
        "name":"Linus",
        "year":2011
    }
}

print(myFamily)
print(myFamily["child1"]["name"])

for x,obj in myFamily.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])