'''
7. Count how many times a specific value appears in a tuple.
'''


t=(1,4,3,4,4,6,66)
nm=4;
count=0
for num in t:
    if num==nm:
        count+=1;
        
print("No of count ",count)
        