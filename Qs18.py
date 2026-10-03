'''Question 18: Write a Java program to convert days into years, months, and weeks.
Asked In Basic program
Input:
Days = 400

Output:
Years = 1
Months = 1
Weeks = 1

Explanation:
1 year = 365 days.
After subtracting 365 days, the remaining days are divided into months (30 days each) and weeks (7 days each).

lightbulb Take a Help'''


days=int(input("enterr days : \n"))
years =days//365
Update_days = days-(years * 365)
months = days//30
days = days - (months * 30)
weeks = days//7
print(years)

print(months)
print(days)
print(weeks)