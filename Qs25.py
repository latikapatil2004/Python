'''Question 25: Write a Java program to check whether a number is palindrome or not.
Asked In Basic program
Input:
121

Output:
Palindrome

Explanation:
A palindrome number remains the same when reversed.
Since 121 reversed is also 121, it is a palindrome.
'''


num=int(input("Enter num"))
temp=num
rev=(temp%10)*100+((temp//10)%10)*10+temp//100
if num==rev:
    print("Palindrome")
else:
    print("not palindrome")
    
    
    
    

