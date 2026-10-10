'''
9. Check if an element exists in a tuple.
'''

tup=(1,2,3,4,5,4,5)
number=6;
exists=False
for num in tup:
    if num==number:
        exists=True
        break;
        
if exists==True: 
    print("number exists")
else:
    print("does not exists")
    
    