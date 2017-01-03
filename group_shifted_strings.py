input_string = ["xyz",  "bcd","abc",  "az","ba", "acef", "a","z"]

output = [
 ["abc","bcd","xyz"],
 ["az","ba"],
 ["acef"],
 ["a","z"]
]

def group_strings(strings):
    #import ipdb; ipdb.set_trace()
    result = []
    mapr = {}

    for s in strings:
        arr = list(s) 
        # print arr
        if len(arr) > 0:
            diff = ord(arr[0]) - ord('a')
            print diff
            for i  in xrange(0, len(arr), 1):
                if ord(arr[i]) - diff < ord('a'):
                    arr[i] = chr(ord(arr[i]) - diff + 26)
                    # print "First: " + str(arr[i])
                else:
                    arr[i] = chr(ord(arr[i]) - diff)
                    # print "Second: " + str(arr[i])
        ns = "".join(arr)
        #print ns
        if ns in mapr:
            #print mapr
            tmp = mapr.get(ns)
            tmp.append(s)
            mapr[ns] = tmp
        else:
            al = []
            al.append(s)
            mapr[ns] = al

    for entry in mapr.keys():
        mapr[entry] = sorted(mapr[entry])

    result = mapr.values()

    return result


print group_strings(input_string)