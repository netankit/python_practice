'''
# String (number) to integer
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do
not see below and ask yourself what are the possible input cases.
'''

'''
null string
white spaces
+ or -
max or min
real value calculation
'''
import sys


def atoi(string):

	if string == None or len(string) < 1:
		return 0
	
	string = string.strip()

	flag = '+'

	i = 0
	if string[0] == '-':
		flag = '-'
		i+=1
	elif string[0] == '+':
		i+=1


	result = 0

	while (len(string) > i  and string[i] >= '0' and string[i] <= '9'):
		result = result * 10 + ord(string[i]) - ord('0')
		i+=1	

	if flag=='-':
		result = -result

	if result > sys.maxint:
		return sys.maxint

	if result < -sys.maxint-1:
		return -sys.maxint-1

	return int(result)

print atoi("991")



