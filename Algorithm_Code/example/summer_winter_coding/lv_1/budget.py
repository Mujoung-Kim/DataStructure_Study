# 예산
# 규칙
# 지원을 할 때는 해당 부서에서 신청한 금액을 전부 지원
# budget에서 최대한 많이 지원하는 경우의 수

# 조건
# 1 <= len(d) <= 100
# 1 <= d.elements <= 100000
# 1 <= budget <= 10000000

# input / output
# d				budget	result
# [1,3,2,5,4]	9		3
# [2,2,3,3]		10		4

import itertools

# O(2^N)
def solution(d, budget) :
	d.sort()
	result = list()

	for x in range(len(d) + 1) :
		for items in itertools.combinations(d, x) :
			if sum(items) == budget :
				result.append(len(items))

	return max(result)

# O(NlogN)
def solution(d, budget):
	d.sort()
	total = 0

	for idx in range(len(d)):
		total += d[idx]
		
		if total > budget:
			return idx
	
	return len(d)

# O(NlogN) while 사용
def solution(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
	
    return len(d)

if __name__ == '__main__' :
	print(solution([1,3,2,5,4], 9))
	print(solution([2,2,3,3], 10))