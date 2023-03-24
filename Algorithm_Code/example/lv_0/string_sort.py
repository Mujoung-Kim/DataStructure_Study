# 문자열 정렬하기
# 규칙
# my_string 안의 숫자만 골라 오름차순으로 정렬하고 반환

# 조건
# 1 <= len(my_string) <= 100
# 1 <= my_string.isdecimal()
# my_string.elements -> lowercase, range(9)

# input / output
# my_string		result
# "hi12392"		[1, 2, 2, 3, 9]
# "p2o4i8gj2"	[2, 2, 4, 8]
# "abcde0"		[0]

def solution(my_string) :
	result = list()

	for val in my_string :
		if val.isdecimal() :
			result.append(int(val))

	return sorted(result)

def solution(my_string) :
	return sorted([int(val) for val in my_string if val.isdecimal()])

# map, filter 사용
def solution(my_string) :
	return sorted(map(int, filter(lambda s: s.isdecimal(), my_string)))

if __name__ == '__main__' :
	print(solution("hi12392"))
	print(solution("p2o4i8gj2"))
	print(solution("abcde0"))