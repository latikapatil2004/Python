'''Question 17: Write a Java program to convert seconds into hours, minutes, and seconds.
Asked In Basic program
Input:
Seconds = 3665

Output:
Hours = 1
Minutes = 1
Seconds = 5

Explanation:
1 hour = 3600 seconds.
3665 / 3600 gives 1 hour.
Remaining seconds are converted into minutes and seconds using division and modulus operations.'''

seconds=int(input("enter seconds"))

hours = seconds/3600;
remainingSeconds = seconds % 3600;
minutes = remainingSeconds / 60;
seconds = remainingSeconds % 60;
print("hour : ",hours)
print("Minutes : ",minutes)
print("Seconds : ",seconds)