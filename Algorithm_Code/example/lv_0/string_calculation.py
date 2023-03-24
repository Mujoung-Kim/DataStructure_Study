# 문자열 계산하기
# 규칙
# 문자열로 된 수식을 계산해서 반환

# 조건
# 연산자는 +, -만 존재
# 문자열의 시작과 끝에는 공백이 없다.
# 잘못된 수식은 들어오지 않는다.
# 5 <= len(my_string) <- 100
# 1 <= result <= 100000
# type(result) = int

# input / output
# my_string	result
# "3 + 4"	7

def solution(my_string) :
	a, b, c = map(str, my_string.split())

	if b == '+' :
		return int(a) + int(c)
	elif b == '-' :
		return int(a) - int(c)

# def solution(my_string) :
# 	tmp = my_string.split()

# 	if tmp[1] == '+' :
# 		if not tmp[-1].isdigit() :
# 			return tmp[0]
# 		elif len(tmp) == 1 :
# 			return tmp[0]
# 		else :
# 			return int(tmp[0]) + int(tmp[-1])
# 	if tmp[1] == '-' :
# 		if not tmp[-1].isdigit() :
# 			return tmp[0]
# 		else :
# 			return int(tmp[0]) - int(tmp[-1])

if __name__ == '__main__' :
	print(solution("3 + 4"))
	# print(solution("300 +"))
	print(solution("1 - 20000"))