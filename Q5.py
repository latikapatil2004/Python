'''. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements.
'''



numbers={10,20,30,40,50}
sum=0
for num in numbers:
    sum=sum+num
    
    
avg=sum/len(numbers)
print("Average",avg)