#case sensitive
thislist=["banana","Orange","Kiwi","Cherry"]
thislist.sort()
print(thislist)

#case insensitive
thislist=["banana","Orange","Kiwi","Cherry"]
thislist.sort(key=str.lower)
print(thislist)


