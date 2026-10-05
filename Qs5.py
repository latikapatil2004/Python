'''Question 5: Write a Java program to count even & odd values from an array.
Asked In Practice assignment
Input:
Array Size = 7
Array Elements = 12 17 24 39 40 55 70
Output:
Count of Even Values = 4
Count of Odd Values = 3
Explanation:
? Initialize counters: evenCount = 0, oddCount = 0.
? For each element in the array:

? If divisible by 2 ? increase evenCount.
? Otherwise ? increase oddCount.
'''


list=[12,17,24,39,40,55,70]
l=len(list)
ecount=0
ocount=0

for i in range(0,l):
    if list[i]%2==0:
        ecount+=1

for i in range(0,l):
    if list[i]%2!=0:
        ocount+=1
        
print("Even count",ecount)
print("Odd count",ocount)
      