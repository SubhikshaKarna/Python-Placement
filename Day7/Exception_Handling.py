def  convert_to_integer(string):
    try:
        number=int(string)
        print("Integer value:",number)
    except ValueError:
        print("Error: Invalid Format")
def main():
    string=input("Enter string to Convert into Integer:")
    convert_to_integer(string)

if __name__=="__main__":
    main()
    

#Exception Handling

def get_positive_integer():
    while True:
        try:
            number=int(input("Enter a positive Integer:"))
            if number<=0:
                raise ValueError("Not a positive integer!")
            return number
        except ValueError as e:
            print("Error:",e)
    
positive_integer=get_positive_integer()
print("You Entered:",positive_integer)

#Custom Exception 
class MyCustomError(Exception):
    def __init__(self,message):
        self.message=message  
try:
    raise MyCustomError("This is a custom error message.")
except MyCustomError as e:
    print("Custom Error caught:",e.message)

#Index Error

def access_list_element(lst,index):
    try:
        value=lst[index]
        print("Value at index",index,"is:",value)
    except IndexError:
        print("Error:Index out of range!")

my_list=[1,2,3,4,5]
index=int(input("Enter an index to access:"))
access_list_element(my_list,index)

#File not found Error

try:
    file=open("nonexistentfile.txt","r")
    content=file.read()
    file.close()
except FileNotFoundError:
    print("File not found!")

# Key Error

def access_dictionary_value(dictionary,key):
    try:
        value=dictionary[key]
        print("Value for key",key,"is:",value)
    except KeyError:
        print("Error:Key not found!")

my_dict={'a':1,'b':2,'c':3}
key=input("Enter a key to access:")
access_dictionary_value(my_dict,key)