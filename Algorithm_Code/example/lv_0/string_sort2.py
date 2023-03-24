# 문자열 정렬하기2
# 규칙
# 모두 소문자로 바꾸고 알파벳 순서대로 정렬 후 반환

# 조건
# 0 < len(my_string) < 100

# input / output
# my_string	result
# "Bcad"	"abcd"
# "heLLo"	"ehllo"
# "Python"	"hnopty"

def solution(my_string) :
	result = ''

	for val in sorted(my_string.lower()) :
		result += val

	return result

# join 사용
def solution(my_string) :
	return ''.join(sorted(my_string.lower()))

if __name__ == '__main__' :
	print(solution("Bcad"))
	print(solution("heLLo"))
	print(solution("Python"))