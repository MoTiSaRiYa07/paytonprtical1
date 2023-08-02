
"""

 To find total number of odd digit, even digit, sum of odd digit and sum of even
digit from the given number.
"""




# initializing list
test_list = [345, 893, 1948, 34, 2346]

# printing original list
print("The original list is : " + str(test_list))

odd_sum = 0
even_sum = 0

for sub in test_list:
	for ele in str(sub):
		
		# adding in particular summation according to value
		if int(ele) % 2 == 0:
			even_sum += int(ele)
		else:
			odd_sum += int(ele)

# printing result
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))



"""
           output ::
		   The original list is : [345, 893, 1948, 34, 2346]
Odd digit sum : 36
Even digit sum : 40
BMIIT202106100110152@bmiit-lab1:~/Desktop$ 
"""