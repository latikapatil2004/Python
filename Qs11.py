'''Input:
Marks = 70, 75, 80, 65, 60

Output:
Total = 350
Percentage = 70%

Explanation:
Total marks are calculated by adding all five subject marks.
Percentage = Total / 5.

'''

sub1=int(input("Ennter marks of subject1 \n"))
sub2=int(input("Ennter marks of subject2 \n"))
sub3=int(input("Ennter marks of subject3 \n"))
sub4=int(input("Ennter marks of subject4 \n"))
sub5=int(input("Ennter marks of subject5 \n"))
total=(sub1+sub2+sub3+sub4+sub5)
print("Total   : ", total)
percentage=total/5
print("Percentage   : ", percentage)