# 크기가 작은 부분문자열
# 규칙
# len(p)만큼 t의 자릿수를 나눈다.
# 나눠진 t의 값이 p보다 작거나 같은 값의 갯수를 반환

# 조건
# 1 <= len(p) <= 18
# len(p) <= len(t) <= 10000
# t, p -> only int and not in 0

# input / output
# t					p		result
# "3141592"			"271"	2
# "500220839878"	"7"		8
# "10203"			"15"	3

def solution(t, p) :
	result = []

	for idx in range(len(t)) :
		if len(t[idx : idx + len(p)]) >= len(p) :
			if t[idx : idx + len(p)] <= p :
				result.append(t[idx : idx + len(p)])

	return len(result)

# comprehension
def solution(t, p):
    return len([t[idx : idx + len(p)] for idx in range(len(t)) if len(t[idx : idx + len(p)]) >= len(p) and t[idx : idx + len(p)] <= p])

# 다른 풀이
def solution(t, p) :
	result = 0

	for i in range(len(t) - len(p) + 1) :
		if p >= t[i : i + len(p)] :
			result += 1

	return result

if __name__ == '__main__' :
	print(solution("3141592", "271"))
	print(solution("500220839878", "7"))
	print(solution("10203", "15"))