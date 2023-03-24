# 문자열안에 문자열
# 규칙
# str1안에 str2가 있다면 1 없다면 2를 반환.

# 조건
# 1 <= len(str1) <= 100
# 1 <= len(str2) <= 100
# string -> uppercase, lowercase, int

# input / output
# str1						str2	result
# "ab6CDE443fgh22iJKlmn1o"	"6CD"	1
# "ppprrrogrammers"			"pppp"	2
# "AbcAbcA"					"AAA"	2

def solution(str1, str2) :

	if str2 in str1 :
		return 1
	else :
		return 2

# one_line
def solution(str1, str2) :
	return 1 if str2 in str1 else 2

if __name__ == '__main__' :
	print(solution('ab6CDE443fgh22iJKlmn1o', '6CD'))
	print(solution('ppprrrogrammers', 'pppp'))
	print(solution('AbcAbcA', 'AAA'))