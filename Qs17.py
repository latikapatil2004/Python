'''
8. Find the index of a given element in a tuple.
'''


tup=(1,2,3,4,5)
number=3;
index=-1
for i in range(len(tup)):
    if tup[i]==number:
        index=i;
        break;
print("Index of array ",index)