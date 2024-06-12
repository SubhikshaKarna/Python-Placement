input_string=input("Enter a String:")

#String Length
print("Length of the string:",len(input_string))

#Convert to UpperCase
print("Uppercase:",input_string.upper())
print(input_string.isupper())

#Convert to LowerCase
print("Lowercase:",input_string.lower())
print(input_string.islower())


#Capitalize the string
print("Capitalized:",input_string.capitalize())
print("Capitalize Every Word:",input_string.title())

#Count Occurance of a Substring
substring=input("Enter a Substring to count its Occurance:")
print(input_string.count(substring))

#Check if the string starts with a specific substring
prefix=input("Enter a prefix:")
print(input_string.startswith(prefix))

#Check if the string ends with a specific substring
sufix=input("Enter a suffix:")
print(input_string.endswith(sufix))

#Replace a substring with Another substring
old_substring=input("Enter a delimeter to split the string:")
new_substring=input("Enter a replacement substring:")
print(input_string.replace(old_substring,new_substring))

#Split the string into a list of substring
delimiter=input("Enter a delimiter to split the string:")
print(input_string.split(delimiter))

#Join a list of substring into a single string
substring=input("Enter substring to join(seperated by space):").split()
join_delimiter=input("Enter a delimiter to join the substrings:")
print(join_delimiter.join(substring))

#The strip() method removes any whitespace from the beginning or the end:
print(input_string.strip())
print(input_string.rfind("l"))
print(input_string.rindex("l"))