# merge 2 sorted arrays

a = [10, 15, 41, 43, 44, 59, 74, 79, 92] + [0] * 8
b = [2, 11, 37, 58, 62, 73, 78, 79]
m = 9
n = 8
res = [2, 10, 11, 15, 37, 41, 43, 44, 58, 59, 62, 73, 74, 78, 79, 79, 92]

def merge(a, m, b, n):
	i = m-1
	j = n-1
	k = m + n - 1
	while(k >=0):
		if (j < 0 or i >=0 and a[i] > b[j]):
			a[k] = a[i];  k -=1; i-=1
		else:
			a[k] = b[j]; k -=1; j-=1

merge(a, m, b, n)

print a

assert a == res	