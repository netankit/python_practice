# startString = "hit"

# endString = "cog"

# word_dict = ["hot","dot","dog","lot","log"]

# shortest transformation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" [len: 5]

class WordNode(object):
    def __init__(self, word, numSteps, pre):
        self.word = word
        self.numSteps = numSteps
        self.pre = pre


class Solution(object):
    def findLadders(self, startString, endString, word_dict):
        result = []
        queue = []
        queue.append(WordNode(startString, 1, None))

        word_dict.add(endString)

        minStep = 0
        visited = set()
        unvisited = set()

        unvisited = word_dict.copy()

        preNumSteps = 0

        while (not len(queue) == 0):
            # print queue
            top = queue.pop(0)
            word = top.word

            currNumSteps = top.numSteps

            if word == endString:
                if (minStep == 0):
                    minStep = top.numSteps

            if (top.numSteps == minStep and not minStep == 0):
                # nothing
                t = []
                t.insert(0, top.word)

                while (not top.pre == None):
                    t.append(top.pre.word)
                    top = top.pre

                result.append(t)
                continue

            if (preNumSteps < currNumSteps):
                unvisited.difference_update(visited)

            preNumSteps = currNumSteps

            arr = list(word)

            for i in range(len(arr)):
                for j in range(ord('a'), ord('z') + 1):
                    temp = arr[i]

                    if not arr[i] == chr(j):
                        arr[i] = chr(j)

                    new_word = "".join(arr)

                    if new_word in word_dict:
                        queue.append(WordNode(new_word, top.numSteps + 1, top))
                        word_dict.remove(new_word)

                    arr[i] = temp

        return result

if __name__ == "__main__":
    startString = "hit"

    endString = "cog"

    word_dict = {"hot", "dot", "dog", "lot", "log"}

    ss = Solution()
    print ss.findLadders(startString, endString, word_dict)
