# Wild Card Matching support for ? and *
def isMatch(string, pattern):
	i = 0
	j = 0
	starIndex = -1
	iIndex = -1

	while (i < len(string)):
		if (j < len(pattern) and (pattern[j] == "?" or pattern[j] == string[i])):
			i += 1
			j += 1
		elif(j < len(pattern) and pattern[j] == "*"):
			starIndex = j
			iIndex = i
			j+=1
		elif not (starIndex == -1):
			j = starIndex +1
			i = iIndex +1
			iIndex+=1
		else:
			return False

	while(j< len(pattern) and pattern[j] == '*'):
		j +=1

	return j == len(pattern)

print isMatch("aab", "*ab") # True
print isMatch("aab", "?ab") # True
print isMatch("bab", "*ab") # True
print isMatch("bab", "b?b") # True
print isMatch("babi", "*bi") # True
print isMatch("bab", "b?e") # False
