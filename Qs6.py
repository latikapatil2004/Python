'''5.Find the Sum of Even Numbers
Write a Python program to create a set of integers and calculate the sum of only the even numbers.'''



set={2,4,5,6,7,8,9,11}
esum=0
osum=0
for num in set:
    if num%2==0:
        esum=esum+num
    elif num%2!=0:
        osum=osum+num
    
print("Even ssum",esum)
print("Odd ssum",osum)

    
    
