
"""
Write a Python program that takes any character as an input and check
whether it is alphabet, digit or special character.
"""




ch = input("Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character")


    """
        output ::
                 
BMIIT202106100110152@bmiit-lab1:~/Desktop$ python3 24.py
Enter Your Own Character : ankush
The Given Character  ankush is an Alphabet
-------------------------------------------------------------------
BMIIT202106100110152@bmiit-lab1:~/Desktop$ python3 24.py
Enter Your Own Character : 152
The Given Character  152 is a Digit
-----------------------------------------------------------------------
.BMIIT202106100110152@bmiit-lab1:~/Desktop$ python3 24.py
Enter Your Own Character : -152
The Given Character  -152 is a Special Character
.BMIIT202106100110152@bmiit-lab1:~/Desktop$ .

 """