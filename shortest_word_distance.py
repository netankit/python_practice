# shortest_word_distance
import sys
import ipdb
def  shortest_word_distance(words, word1, word2):
	ipdb.set_trace()

	if words == None or word1 == None or word2 == None or len(words) < 1:
		return 0
	m = -1
	n = -1

	minimum =  sys.maxint

	turn = 0
	if word1 == word2:
		turn  = 1

	for i in xrange(0, len(words), 1):
		ss = words[i]
		if word1 == ss and (turn ==1 or turn == 0):
			m = i 
			if turn == 1:
				turn = 2
			if not n == -1:
				minimum = min(minimum, m - n)
		elif word2 == ss and (turn ==2 or turn == 0):
			n = i
			if turn == 2:
				turn = 1
			if not m == -1:
				minimum = min(minimum, n - m)
	print minimum
	return minimum

words = ["practice", "makes", "perfect", "coding", "makes"]
print "First: "
word1 = "makes" 
word2 = "coding" 
ouput1 = 1 
assert shortest_word_distance(words, word1, word2) == ouput1
print "Second: "
word1 = "makes" 
word2 = "makes" 
output2 = 3.
assert shortest_word_distance(words, word1, word2) == output2

