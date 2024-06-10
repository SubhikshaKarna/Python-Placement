#Sort based on how close the number is to 50
#Customized sort
def fun(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key=fun)
print(thislist)


