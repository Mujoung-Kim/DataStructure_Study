# 나머지가 1이 되는 수 찾기
# 규칙
# num을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 반환

# 조건
# 3 <= num <= 1000000

# input / output
# n		result
# 10	3
# 12	11

def solution(num) :
	for i in range(1, num + 1) :
		if num % i == 1 :
			return i

# comprehension
def solution(num) :
	return [i for i in range(1, num + 1) if num % i == 1][0]

if __name__ == '__main__' :
	print(solution(10))
	print(solution(12))