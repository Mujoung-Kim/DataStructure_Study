# TODO : section의 elements가 m보다 큰 경우 몫계산법으로 안됨.
# 덧칠하기
# 규칙

# 조건

# input / output
# n	m	section	result
# 8	4	[2, 3, 6]	2
# 5	4	[1, 3]	1
# 4	1	[1, 2, 3, 4]	4
# 6 3   [2, 3, 6]   2
# 6 5   [2, 3, 6]   1
# 6 5   [1, 6]  2

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

if __name__ == '__main__' :
    print(solution(8, 4, [2, 3, 6]))
    print(solution(5, 4, [1, 3]))
    print(solution(4, 1, [1, 2, 3, 4]))
    print(solution(6, 3, [2, 3, 6]))
    print(solution(6, 5, [2, 3, 6]))
    print(solution(6, 5, [1, 6]))