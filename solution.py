# A = 6, B = 1, C = 1, return 'aacaabaa', diverse string
def solution(A, B, C):
    def recur(a, b, c, A, B, C, string, result):
        result.append(string)
        if (len(string) < 2 and a<A) or (a<A and ((string[-1] == 'a' and string[-2] != 'a') or (string[-1] != 'a'))) :
            recur(a+1, b, c, A, B, C, string+'a', result)
        if (len(string) < 2 and b<B) or (b<B and ((string[-1] == 'b' and string[-2] != 'b') or (string[-1] != 'b'))) :
            recur(a, b+1, c, A, B, C, string+'b', result)
        if (len(string) < 2 and c<C) or (c<C and ((string[-1] == 'c' and string[-2] != 'c') or (string[-1] != 'c'))) :
            recur(a, b, c+1, A, B, C, string+'c', result)
    result = []
    string = ''
    recur(0, 0, 0, A, B, C, string, result)
    max_ = 0
    res = []
    for r in result: # filter short element
        if len(r) > max_:
            max_ = len(r)
            res.append(r)
    res.sort(key=len, reverse=True)
    return res[0]

# aabaacaa
# abbcb
# ccbcc
