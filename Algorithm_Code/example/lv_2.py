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
    result = None

    if m > section[len(section) - 1] - section[0] :
        result = n // m
    else :
        result = 'exception!!'
    
    return result

section = [2, 3, 6]

# test bed
if __name__ == '__main__' :
    print(solution(6, 3, section))
    pass