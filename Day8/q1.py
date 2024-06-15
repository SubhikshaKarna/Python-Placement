#Take a Sentence as a input and count number of words character and uppercase and lowercase  letter init

import string
sentence=input("Enter a  sentence:")
wordList=sentence.strip().split(" ")
print(f'This Sentence has {len(wordList)} words',end='\n\n')
digit_count=uppercase_count=lowercase_count=0
for character in sentence:
    if character in string.digits:
        digit_count+=1
    elif character in string.ascii_uppercase:
        uppercase_count+=1
    elif character in string.ascii_lowercase:
        lowercase_count+=1
print(f'This Sentence has {digit_count} digits',f'{uppercase_count} upper case letters',f'{lowercase_count} lower case letters', sep="\n")