
import random
import string 

ASCII_lowercase = string.ascii_lowercase
ASCII_uppercase = string.ascii_uppercase
Digits= string.digits
Punctuations=string.punctuation

Password_Length=int(input("Enter Password Length :"))
s=[]
s.extend(list(ASCII_lowercase))
s.extend(list(ASCII_uppercase))
s.extend(list(Digits))
s.extend(list(Punctuations)) 
random.shuffle(s)
print("---------------------------------------")
print("Password Generated :","".join(s[:Password_Length]))
print("--------------------------------------")
