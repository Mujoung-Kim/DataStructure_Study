# TODO : 맵을 그리는걸 노가다로 [i][j]로 그려야됨
# 공원 산책
# 규칙
# 1. 주어진 routes로 이동할 때 공원을 벗어나는지 확인
# 2. 주어진 routes로 이동할 때 장애물을 만나는지 확인
# 위의 2가지 조건에 해당되면 해당 명령을 무시하고 다음 명령을 수행
# 공원의 가로 길이 : W, 세로 길이 : H
# 공원의 좌측 상단 (0, 0), 우측 하단 (H - 1, W - 1)
# 모든 명령을 수행하고 난 후 강아지의 최종 위치를 반환

# 조건
# 3 <= len(park) <= 50
# 3 <= len(park[i]) <= 50
# park[i] = 'S' : start_point, 'O' : move, 'X' : error
# park는 직사각형
# 1 <= len(routes) <= 50
# routes의 처음부터 순서대로 진행
# op : 방향 = 'N' : 북, 'S' : 남, 'W' : 서, 'E' : 동
# n : 이동할 칸
# 1 <= n <= 9

# input / output
# park						routes				result
# ["SOO","OOO","OOO"]		["E 2","S 2","W 1"]	[2,1]
# ["SOO","OXX","OOO"]		["E 2","S 2","W 1"]	[0,1]
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]

def find_start_point(list) :
	for i in range(len(list)) :
		for j in range(len(list[i])) :
			if list[i][j] == 'S' :
				return i, j

def solution(park, routes) :
	prt_park = [[char for char in string] for string in park]
	x, y = find_start_point(prt_park)
	result = list()

	# routes 추출
	order = [list(map(str, val.split())) for val in routes]

	# moving
	for ord in order :
		# start_point
		prt_park[x][y]

		if ord[0] == 'N' :
			x -= int(ord[1])
		elif ord[0] == 'S' :
			x += int(ord[1])
		elif ord[0] == 'W' :
			y -= int(ord[1])
		elif ord[0] == 'E' :
			y += int(ord[1])
		# print(f'({x}, {y})')

	result.append(x)
	result.append(y)
	# return order
	return prt_park
	return result

if __name__ == '__main__' :
	print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
	print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
	# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))