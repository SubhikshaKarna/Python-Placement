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
    