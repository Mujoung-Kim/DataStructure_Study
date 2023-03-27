# 문자열 나누기
# 규칙
# 1. 가장 첫 글자를 읽는다. 이 글자를 x라 한다.
# 2. x와 x가 아닌 다른 글자들이 나온 횟수를 센다.
# 3. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
# 4. string에서 분리한 문자열을 뺴고 남은 부분에 대해서 1 ~ 3을 반복
# 5-1. 남은 부분이 없다면 종료
# 5-2. 두 횟수가 다른 상태에서 더 이상 글자가 없다면,
# 		지금까지 읽은 문자열을 분리하고 종료.

# 조건
# 1 <= len(string) <= 10000
# s -> lower

# input / output
# s					result
# "banana"			3
# "abracadabra"		6
# "aaabbaccccabba"	3

# TODO : step 1까지는 됨.
def solution(string) :
	# result = [string[i:i+2] for i in range(0, len(string), 2)]
	x, y = '', ''
	count_x, count_y = 1, 0
	result = list()

	# 첫 글자와 같은 글자가 반복되는 횟수
	for idx in range(len(string)) :
		if string[0] == string[idx] :
			count_x += 1
		else :
			break

	print(count_x)
	
	# count_x와 count_y 가 같아지면 result.append
	for idx, val in enumerate(string) :
		if string[0] != string[idx] :
			y += val
			count_y += 1
		if count_x == count_y :
			result.append(y)
			count_y = 0

	return result
	# 나눌 때 기준 맞추면 됨, 2 자리에 들어갈 기준을 찾아서 적용시키면 끝
	# for idx in range(0, len(string), 2) :
	# 	result.append(string[idx : idx + 2])
	# result = [string[idx : idx + 2] for idx in range(0, len(string), count_x)]

	# return string, len(string), count_x, result
	# return len([string[idx : idx + 2] for idx in range(0, len(string), count_x)])


if __name__ == '__main__' :
	print(solution("banana"))
	print(solution("abracadabra"))
	print(solution("aaabbaccccabba"))