
# Longest Substring without repetition
def length_of_longest_substring(s):
    if s is None:
        return 0
    flag = [False] * 256
    result = 0
    start = 0
    arr = list(s)
    for i in xrange(0, len(arr), 1):
        current = arr[i]
        if flag[current]:
            result = max(result, i-start)
            for k in xrange(start, i, 1):
                if arr[k] == current:
                    start = k + 1
                    break
                flag[arr[k]] = False
        else:
            flag[current] = True
    result = max(len(arr) - start, result)
    return result

print length_of_longest_substring("bbbbb")
print length_of_longest_substring("abcabcbb")

