# 문자열 뒤집기
# 규칙
# 거꾸로 뒤집은 문자열을 반환

# 조건
# 1 <= len(my_string) <= 1000

# input / output
# my_string	return
# "jaron"	"noraj"
# "bread"	"daerb"

def solution(my_string) :
	result = ''
	
	for idx in range(len(my_string) - 1, -1, -1) : 
		result += my_string[idx]

	return result

def solution(my_string) :
	return ''.join([my_string[idx] for idx in range(len(my_string) - 1, -1, -1)])

# slicing
def solution(my_string) :
	return my_string[::-1]

# reversed 사용
def solution(my_string) :
	return ''.join(list(reversed(my_string)))

if __name__ == '__main__' :
	print(solution("jaron"))
	print(solution("bread"))