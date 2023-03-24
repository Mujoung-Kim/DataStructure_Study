# 시저 암호
# 규칙

# 조건
# 공백은 아무리 뒤로 밀어도 공백
# string -> lower, upper, space
# 1 <= len(string) <= 8000
# 1 <= num <= 25

# input / output
# string	num	result
# "AB"		1	"BC"
# "z"		1	"a"
# "a B z"	4	"e F d"

# O(N)
def solution(string, num) :
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	result = ''

	for val in string :
		if val in upper :
			result += upper[(upper.index(val) + num) % 26]
		elif val in lower :
			result += lower[(lower.index(val) + num) % 26]
		elif val == ' ' :
			result += val

	return result

# O(N) comprehension
def solution(string, num):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([
	    upper[(upper.index(val) + num) % 26] if val in upper else 
		lower[(lower.index(val) + num) % 26] if val in lower else 
		val for val in string
		])

# chr, ord 사용
def solution(string, num) :
	string = list(string)

	for i in range(len(string)) :
		if string[i].isupper() :
			string[i] = chr((ord(string[i]) - ord('A') + num) % 26 + ord('A'))
		elif string[i].islower() :
			string[i] = chr((ord(string[i]) - ord('a') + num) % 26 + ord('a'))

	return ''.join(string)

if __name__ == '__main__' :
	print(solution("AB", 1))
	print(solution("z", 1))
	print(solution("a B z", 4))