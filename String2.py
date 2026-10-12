'''2. Take a string input and convert it to lowercase.
'''

str=input("Enter String")
result=""
for ch in str:
    if 'A'<=ch<='Z':
        result=result+chr(ord(ch)+32)    
    else: 
        result=result+ch;
        
print(result);
        
