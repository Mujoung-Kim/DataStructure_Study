# 가장 가까운 같은 글자
# 규칙
# string = "banana" 라고 가정했을 때
# string[0]은 자신의 앞에 같은 글자가 없으므로 -1
# string[1]은 자신의 앞에 같은 글자가 없으므로 -1
# string[2]은 자신의 앞에 같은 글자가 없으므로 -1
# string[3]은 자신의 두 칸 앞에 같은 글자가 존재하므로 2
# string[4]은 자신의 두 칸 앞에 같은 글자가 존재하므로 2
# string[5]은 자신의 두 칸, 네 칸 앞에 같은 글자가 존재하며
#  			  가장 가까운 것은 두 칸이므로 2
# result = [-1, -1, -1, 2, 2, 2]를 반환

# 조건
# 1 <= len(string) <= 10000
# string -> lower

# input / output
# string	result
# "banana"	[-1, -1, -1, 2, 2, 2]
# "bannana"	[-1, -1, -1, 1, 3, 2, 2]
# "foobar"	[-1, -1, 1, -1, -1, -1]

def solution(string) :
	result = list()
	dic = dict()

	for idx in range(len(string)) :
		if string[idx] in dic :
			result.append(idx - dic[string[idx]])
		else : 
			result.append(-1)
		
		dic[string[idx]] = idx

	return result

if __name__ == '__main__' :
	print(solution("banana"))
	print(solution("bannana"))
	print(solution("foobar"))