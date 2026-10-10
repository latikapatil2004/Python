'''18. Find the maximum and minimum value in a tuple.
'''


tup=(1,2,3,4,5,67)
max=tup[0];
min=9;
for num in tup:
    if num>max:
        max=num
        
    elif num<min:
        min=num;
        
print("Maximum",max)
print("Manimum",min)
