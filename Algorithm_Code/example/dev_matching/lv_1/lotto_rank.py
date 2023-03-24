# 로또의 최고 순위와 최저 순위
# 규칙
# 맞춘 갯수에 따라 등급나눔
# 1 : len(lottos) - n -> n = range(len(lottos), 0, -1)
# 낙서된 번호는 0으로 표기
# 낙서된 lottos를 보고 최저와 최고 순위를 예측
# 최고순위는 0은 전부 맞춤, 최저순위는 0은 전부 틀림

# 조건
# len(lottos), len(win_nums) == 6
# 0 <= lottos.elements <= 45
# lottos.elements -> 0만 중복허용
# 1 <= win_nums.elements <= 45
# win_nums.elements -> 중복x

# input / output
# lottos				win_nums					result
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]		[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]		[1, 1]

def solution(lottos, win_nums) :
	rank = { 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : [1, 0] } 
	min = len(list(set(win_nums).intersection(lottos)))
	max = min + lottos.count(0)
	result = list()

	for key, value in rank.items() :
		if max == value :
			result.append(key)
		elif len(str(value)) > 1 :
			if max in value :
				result.append(key)
		if min == value :
			result.append(key)
		elif len(str(value)) > 1 :
			if min in value :
				result.append(key)

	return result

# dict one_line
def solution(lottos, win_nums) :
	rank = { 0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}

	return [
		rank[len(set(win_nums).intersection(lottos)) + lottos.count(0)], 
		rank[len(set(win_nums).intersection(lottos))] 
		]

# 다른 풀이 only list
def solution(lottos, win_nums) :
	rank = [6, 6, 5, 4, 3, 2, 1]
	cnt_0 = lottos.count(0)
	count = 0

	for val in win_nums :
		if val in lottos :
			count += 1

	return rank[cnt_0 + count], rank[count]

if __name__ == '__main__' :
	print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
	print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
	print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))