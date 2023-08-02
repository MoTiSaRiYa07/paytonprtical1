
#Write a python program to print sum of digit in a number. N = 1234 then 1 + 2 + 3 + 4 = 10.
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

#output ::
#Enter Number: 1234      
#10