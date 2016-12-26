# KMP: Knuth-Morris-Pratt PAttern Matching Algorithm: Find the lowest index in Text T which starts to mathes the pattern P. 
# More efficient than Brute Force and Bayer-Moore Algorithm
def compute_kmp_fail(P):
    # import ipdb; ipdb.set_trace()
    m = len(P)
    fail = [0] * m
    j=1
    k=0
    print "Pattern : {}".format([(v,i) for i, v in enumerate(list(P))]) 
    print "Initial - j:{}; k: {}; m: {}; P[j]:{}; P[k]:{}".format(j, k, m, P[j], P[k])
    while j < m:
        print "In loop - k:{}, j:{}; P[j]:{}; P[k]: {}; fail: {}".format(k, j, P[j], P[k], fail)
        if P[j] == P[k]: 
            fail[j] = k + 1 
            j += 1  
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

print compute_kmp_fail("amalgamation")


def find_kmp(T, P):
    n, m = len(T), len(P)
    if m==0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j-m +1
            j+=1
            k+=1
        elif k > 0:
            k = fail[k-1]
        else:
            j+=1
    return -1

print  "\n\n Final Result: "
print find_kmp("atcamalgamalgamation", "amalgamation")