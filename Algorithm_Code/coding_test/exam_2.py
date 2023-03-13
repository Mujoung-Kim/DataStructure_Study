# 입력 조건
# n, m, k (n,m <= k, 1 <= n, m, k <= 10000000)
# 입력 시 space, enter, tab

# input / output example
# 3 3 3
# 1 2 5	-> 귀족
# 1 2 3	-> 상인
# 1 2 4	-> 시민
# 1 -> result

# 1 3 5
# 3
# 2 1 4234
# 4231 4200 4201 1000 4000
# 1 -> result

def solution(t, n, m, k) :
    vote = []
    tmp = {}

    for _ in range(int(t[0]) * 2) :
        for val in n :
            vote.append(val)
    for _ in range(int(t[1]) * 3) :
        for val in m :
            vote.append(val)
    for _ in range(int(t[2])) :
        for val in k :
            vote.append(val)

    for _ in range(len(vote)) :
        for val in list(set(n + m + k)) :
            tmp[val] = vote.count(val)

    tmp = dict(sorted(tmp.items()))
    return max(tmp, key=tmp.get)

t, n, m, k = map(str, [input(), input(), input(), input()])

print(solution(t.split(), n.split(), m.split(), k.split()))