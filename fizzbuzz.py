'''
This program outputs a list of numbers from 1 to 100
If the number is divisible by 3 print fizz
If the number is divisible by 5 print buzz
If the number is divisible by both 3 and 5 print fizzbuzz
Else print the number
'''

for i in range(1,101):
	if i%3==0 and i%5==0:
		print(i,"fizzbuzz")
	elif i%3==0:
		print(i,"fizz")
	elif i%5==0:
		print(i,"buzz")
	else:
		print(i)
