#Write a python program to find the sum of the first N natural numbers. [Hint:
#1+2+3+4+….+N]




num = int(input("enter num 1 :"))
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  


"""

     output ::

BMIIT202106100110152@bmiit-lab1:~/Desktop$ python3 27.py
enter num 1 :500
The sum is 125250

"""