# TODO : right, left 식 도출해야됨
# 키패드 누르기
# 규칙
# 왼손, 오른손 엄지로만 번호를 누름
# 왼손 시작점 = *
# 오른손 시작점 = #
# 엄지는 상하좌우 1칸만 움직임
# 1, 4, 7은 왼손만 / 3, 6, 9는 오른손만
# 2, 5, 8, 0 양손 중 가까운 것만 대신 둘이 거리가 같을 경우 주손으로
# 주손은 hand 변수로 값을 가져옴

# 조건
# 1 <= len(numbers) <= 1000
# 0 <= numbers.elements <= 9
# hand == 'left' or 'right'
# return == 'L' or 'R'

# input / output
# numbers							hand	result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL" LRLLLRLLLRL
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

def solution(numbers, hand) :
	keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
	keypad_t = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
	left = [1, 4, 7, '*']
	right = [3, 6, 9, '#']
	double = [2, 5, 8, 0]
	result = ''

	# for i in numbers :
	# 	print(i)
	# 	for x, y in enumerate(keypad) :
	# 		print(f'x : {x}, y : {y}')

	for x, y in zip(keypad, numbers) :
		print(f'pad : {x}, num : {y}')

	return result

	# 어떻게 기록해야되지 L, R을
	for i in numbers :
		if i in left :
			result += 'L'
		elif i in right :
			result += 'R'
		elif i in double :
			# TODO : right, left가 한 번도 안나왔을 때 초기값 위치설정
			# left, right 위치 어떻게 저장할 지
			return keypad_t[1][1] - keypad_t[0][1]
			# if keypad.index(i) - left < keypad.index(i) - right :
			if keypad.index(i) - keypad.index(numbers[numbers.index(i)] - 1) \
			< keypad.index(i) - keypad.index(numbers[numbers.index(i)] - 2) :
				result += 'L'
			# elif keypad.index(i) - left > keypad.index(i) - right :
			elif keypad.index(i) - keypad.index(numbers[numbers.index(i)] - 1) \
			> keypad.index(i) - keypad.index(numbers[numbers.index(i)] - 2) :
				result += 'R'
			else :
				if hand == 'left' :
					result += 'L'
				elif hand == 'right' :
					result += 'R'
	
	return result
	return len(numbers), result, len(result)

if __name__ == '__main__' :
	print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
	# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
	# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
	pass