# 부족한 금액 계산하기
# 규칙
# 1. 원래 이용료는 price원이다.
# 2. N 번 이용한다면 원래 이용료의 N 배를 받는다.
# 3. 해당 놀이기구를 count번 타게 되면 자신이 가지고 있는 금액에서 얼마가 모자란지 반환하라.

# 조건
# 1 <= price <= 2500
# 1 <= money <= 1000000000
# 1 <= count <= 2500

# input / output
# price	money	count	result
# 3		20		4		10

def solution(price, money, count) :
	result = 0

	for i in range(1, count + 1) :
		result += price * i

	if result > money :
		return result - money
	else :
		return 0

# comprehension
def solution(price, money, count) :
	return sum([price * i for i in range(1, count + 1)]) - money if sum([price * i for i in range(1, count + 1)]) > money else 0

# 다른 풀이
# 산술 평균을 이용
def solution(price, money, count) :
	return max(0, price * (count + 1) * count // 2 - money)

# lambda
solution = lambda price, money, count : max(0, count * (count + 1) // 2 * price - money)

if __name__ == '__main__' :
	print(solution(3, 20, 4))