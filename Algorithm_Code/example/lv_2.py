# painting 

# input/output
# n	m	section	result
# 8	4	[2, 3, 6]	2
# 5	4	[1, 3]	1
# 4	1	[1, 2, 3, 4]	4
# 6 3   [2, 3, 6]   2
# 6 5   [2, 3, 6]   1
# 6 5   [1, 6]  2

# TODO : section의 elements가 m보다 큰 경우 몫계산법으로 안됨.
# 자 이제 exception만 해결하면 날먹으로 쌉가능
def solution(n, m, section) :
    result = 0

    if m > section[len(section) - 1] - section[0] :
        result = n // m
    else :
        for val in section :
            for v in list(range(1, n)) :
                if val in list(range(v, m)) :
                    result += 1
    
    return result

# 숫자 변환하기
# 규칙
# x -> y
# x + n or x * 2 or x * 3의 연산만으로 y값으로 변환
# 변환 가능하면 최소연산 횟수를 return
# 변환 불가능하면 -1을 return

# 조건
# 1 <= x <= y <= 1000000
# 1 <= n < y

# input / output
# x     y	n	result
# 10	40	5	2
# 10	40	30	1
# 2     5	4	-1

# TODO : 2, 3, n 종합으로 계산해서 결과가 나오는 것은 못잡음
def solution(x, y, n) :
    result = {}

    if y % (x * 2) == 0 :
        res = 0
        while x * (2 ** res) != y and x * (2 ** res) <= y:
            res += 1
        if x * (2 ** res) == y :
            result[2] = res
    if y % (x * 3) == 0 :
        res = 0
        while x * (3 ** res) != y and x * (3 ** res) <= y:
            res += 1
        if x * (3 ** res) == y :
            result[3] = res
    if y % (x + n) == 0 :
        res = 0
        while x + n * res != y  and x + n * res <= y:
            res += 1
        if x + n * res == y :
            result["n"] = res
    if y % (x * 2 * 3) == 0 :
        res = 0
    if y % (x * 2) != 0 and y % (x * 3) != 0 and y % (x + n) != 0 :
        return -1

    return min(result.values())

def gcd(x, y, count=0) :
    # print(count)
    if y == 0 :
        return {"y":y, "count":count}
    else :
        count += 1
        return gcd(y, x % y, count)

def solution(x, y, n) :
    result = 0

    if y % (x * 2) % 3 % n == 0 :
        # 계산식 넣으면 됨
        i, idx, index = 0, 0, 0
        res = 0
        while x * (2 ** i) != y and x * (2 ** i) < y :
            res = x * (2 ** i)
            i += 1
        result += (i - 1)
        if x * (3 ** idx) != y - res and x * (3 ** idx) < y - res :
            while x * (3 ** idx) != y - res and x * (3 ** idx) < y - res :
                res = x * (3 ** idx)
                idx += 1
            result += (idx - 1)
        if x * (n ** index) != y - res and x * (n ** index) < y - res :
            while x * (n ** index) != y - res and x * (n ** index) < y - res :
                res = x * (n ** index)
                index += 1
            result += (index - 1)
        # print((i - 1) + (idx - 1) + (index - 1))
        return result
    else :
        return -1

# 2, 3, n를 가지고 x를 이용해서 y값을 만들어라
# 해당 수가 2, 3의 배수인지 확인

# y  -  x = 
# 60 - 10 = 50
# 이 로직
# 간단하게 보면 n^z, 2^z, 3^z 해서 각 z들을 더하면 되는데
# x + n         = 40 -> 1번
# x * 2 * 3     = 60 -> 2번
# x * 2 * 2     = 40 -> 2번
# x * 2 * 3 + n = 65 -> 3번
# x             = 5  -> false

# i, idx, index를 따로따로 증가시키면서 반복
# while x * (2 ** i) * (3 ** idx) + (n ** index) != y and x * (2 ** i) * (3 ** idx) + (n ** index) < y:
#     i, idx, index = i + 1, idx + 1, index + 1

# test bed
if __name__ == '__main__' :
    # print(solution(6, 5, [1, 6]))
    print(solution(10, 60, 5))
    print(solution(10, 40, 5))
    print(solution(10, 40, 30))
    print(solution(2, 5, 4))
    pass