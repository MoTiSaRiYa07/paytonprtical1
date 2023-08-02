29. #Write a python program to find reverse of number.


#Write a python program to find reverse of number.

num = 1234
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

# output :: 4321

