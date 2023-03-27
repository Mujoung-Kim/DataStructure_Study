# 약수의 개수와 덧셈
# 규칙
# 두 정수 left ~ right 까지의 모든 수들 중 약수의 개수가 짝수면 +
# 약수의 개수가 홀수면 - 한 result를 반환.

# 조건
# 1 <= left <= right <= 1000

# input / output
# left	right	result
# 13	17		43
# 24	27		52

# 약수 구하는 함수 구현해서 호출
def solution(left, right) :
	tmp = []
	result = 0

	for num in range(left, right + 1) :
		tmp = get_my_divisor(num)

		if len(tmp) % 2 == 0 :
			result += num
		else :
			result -= num

	return result

def get_my_divisor(num) :
	divsor_list = []

	for i in range(1, num + 1) :
		if num % i == 0 :
			divsor_list.append(i)

	return divsor_list

# 다른 풀이 -> sqrt해서 나눠지면 소수이므로 홀수 아니면 짝수
def solution(left, right) :
	result = 0

	for num in range(left, right + 1) :
		if int(num ** 0.5) == num ** 0.5 :
			result -= num
		else :
			result += num
	
	return result

if __name__ == '__main__' :
	print(solution(13, 17))
	print(solution(24, 27))