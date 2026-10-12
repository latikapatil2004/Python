'''1. Take a string input and convert it to uppercase.
'''


str=input("Enter String")
result=""
for ch in str:
    if 'a'<=ch<='z':
        result=result+chr(ord(ch)-32)    
    else: 
        result=result+ch;
        
print(result);
        
     