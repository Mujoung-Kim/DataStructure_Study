# 소수 만들기
# 규칙
# 주어진 숫자 중 3개의 수를 더 했을 때 소수가 되는 경우의 수
# 서로 다른 3개의 수를 골라 소수가 되는 갯수를 반환

# 조건
# 3 <= len(nums) <= 50
# 1 <= nums.elements <= 1000

# input / output
# nums			result
# [1,2,3,4]		1
# [1,2,7,6,4]	4

import itertools

# O(N^3)
def primenumber(num) :
	for i in range(2, num) :
		if num % i == 0 :
			return False
		
	return True

def solution(nums) :
	return len([items for items in itertools.combinations(nums, 3) if primenumber(sum(items))])

# 시간 복잡도  개선코드
# O(N^3 * sqrt(num))
def primenumber(num) :
	for i in range(2, int(num ** 0.5) + 1) :
		if num % i == 0 :
			return False
	
	return True

def solution(nums) :
	return len([items for items in itertools.combinations(nums, 3) if primenumber(sum(items))])

# 도른자의 채점기계 해킹방법
# class ALWAYS_CORRECT(object) :
#     def __eq__(self, other) :
#         return True

# def solution(a):
#     answer = ALWAYS_CORRECT()
#     return answer

# 에라토스테네스의 체 알고리즘
# O(N^3log(log(N)))
def eratos(num) :
	if num < 2 :
		return []
	
	s = [0, 0] + [1] * (num - 1)

	for i in range(2, int(num ** 0.5) + 1) :
		if s[i] :
			s[i * 2 :: i] = [0] * ((num - i) // i)
	
	return [i for i, v in enumerate(s) if v]

def solution(nums) :
	primes = eratos(3000)
	count = 0

	for i in range(len(nums)) :
		for j in range(i + 1, len(nums)) :
			for k in range(j + 1, len(nums)) :
				if (nums[i] + nums[j] + nums[k]) in primes :
					count += 1

	return count

if __name__ == '__main__' :
	print(solution([1,2,3,4]))
	print(solution([1,2,7,6,4]))