# 없는 숫자 더하기
# 규칙
# range(0, 10)의 숫자중 일부가 들어있는 정수 배열에서
# numbers에서 찾을 수 없는 숫자를 모두 더한 값을 반환.

# 조건
# 1 <= len(numbers) <= 9
# 0 <= numbers.elements <= 9
# set(numbers.elements)

# input / output
# numbers			result
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

def solution(numbers) :
	result = 0

	for num in range(10) :
		if num not in numbers :
			result += num

	return result

# 위의 코드 comprehension으로 변형
def solution(numbers) :
	return sum([num for num in range(10) if num not in numbers])

# 다른 풀이
def solution(numbers) :
	return 45 - sum(numbers)

# lambda 사용
solution = lambda x: sum(range(10)) - sum(x)

if __name__ == '__main__' :
	print(solution([1,2,3,4,6,7,8,0]))
	print(solution([5,8,4,0,6,7,9]))