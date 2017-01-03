# substring with concatenation of all words

s = "barfoothefoobarman"
words = ["foo", "bar"]

result = [0, 9]

def find_substring(s, words):
    result = []
    if s is None or len(s) ==0 or words is None or len(words) == 0:
        return result
    
    # Frequency of words in the "words" list
    map = {}
    for w in words: 
        if w in map:
            map[w] = map[w] + 1
        else:
            map[w] = 1
    
    length = len(words[0])
    for j in xrange(0, length, 1):
        current_map = {}
        start = j
        count = 0
        for i in xrange(j, len(s)-length+1, length):
            sub = s[i:i+length]
            print "First: : {}, {} ,{},{}".format(j, i, i+length , s[i:i+length])

            # Frequency of words in the string "s"
            if sub in map:
                if sub in current_map:
                    current_map[sub] = current_map[sub] + 1
                else:
                    current_map[sub] =  1
                count +=1
                print "map : {}; current_map : {}".format(map, current_map)
                while(current_map[sub] > map[sub]):
                    left = s[start: start + length]
                    current_map[left] = current_map[left] -1
                    print "SECOND: {}".format(left)
                    count -=1
                    start +=length
                
                if count == len(words):
                    result.append(start)
                    print "Result: {}".format(result)
                    # shift right and reset current_map count and start
                    left = s[start:start+ length]
                    count -=1
                    start += length
            else:
                current_map.clear()
                start = i + length
                count = 0
                
    return result        



print "\n# Final Result:>>> \n"
print find_substring(s, words)