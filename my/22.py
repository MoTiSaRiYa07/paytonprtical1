
"""
Write a program to input marks of 5 subjects of a student and display the total
marks scored, percentage scored and the class of result.
Result criteria:
Percentage >= 70% : Distinction
Percentage >= 60% and < 70% : First Class
Percentage >= 50% and < 60% : Second Class
Percentage >= 40% and < 50% : Pass Class
Percentage < 40% : Fail
"""

nam=int(input("Enter your id :"))
print('Enter your name:')
x = input()
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")



"""
output ::
Enter your id :152          
Enter your name :ankush
Enter marks of the first subject: 98
Enter marks of the second subject: 98 
Enter marks of the third subject: 98
Enter marks of the fourth subject: 98 
Enter marks of the fifth subject: 98
Grade: A
    """