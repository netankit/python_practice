# startString = "hit"

# endString = "cog"

# word_dict = ["hot","dot","dog","lot","log"]

# shortest transformation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" [len: 5]

class WordNode(object):
	def __init__(self, word, numSteps):
		self.word = word
		self.numSteps = numSteps



class Solution(object):
	def ladderLength(self, startString, endString, word_dict):
		queue = []
		queue.append(WordNode(startString, 1)) 
		
		word_dict.add(endString)

		while(not len(queue)==0):
			#print queue
			top = queue.pop(0)
			word = top.word

			if word == endString:
				return top.numSteps

			arr = list(word)

			for i in range(len(arr)):
				for j in range(ord('a'), ord('z')+1):
					temp = arr[i]

					if not arr[i] == chr(j):
						arr[i] = chr(j)

					new_word = "".join(arr)

					if new_word in word_dict:
						queue.append(WordNode(new_word, top.numSteps + 1))
						word_dict.remove(new_word)


					arr[i] = temp

		return 0


if __name__=="__main__":

	startString = "hit"

	endString = "cog"

	word_dict = {"hot","dot","dog","lot","log"}

	ss = Solution()
	print ss.ladderLength(startString, endString, word_dict)
