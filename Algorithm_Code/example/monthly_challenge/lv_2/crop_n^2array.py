# N^2 배열 자르기
# 규칙
# 1. N 행 N 열 크기의 비어있는 2차원 배열을 만든다.
# 2. i = 1, 2, 3, ..., N 에 대해 i 행 i 열까지 모든 빈 칸을 i 로 채운다.
# 3. 1행, 2행, ..., N행을 잘라내어 이어 붙인 새로운 1차원 배열을 만든다.
# 4. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[right], ..., arr[right]만 남기고 나머지는 제거한다.
# 5. 주어진 과정대로 만들어진 arr를 반환한다.

# 조건
# 1 <= N <= 10^7
# 0 <= left <= right < N^2
# right - left < 10^5

# input / output
# n		left	right	result
# 3		2		5		[3,2,2,3]
# 4		7		14		[4,3,3,3,4,4,4,4]

# 시간복잡도 : O(N^2)
def solution(n, left, right) :
	result = []

	# 2차원 배열에 값 채워넣기
	for i in range(1, n + 1) :
		line = []
		for j in range(1, n + 1) :
			if i >= j :
				line.append(i)
			else :
				line.append(j)
		result.append(line)

	return sum(result, [])[left : right + 1]

# comprehension
def solution(n, left, right):
    result = [[i if i >= j else j for j in range(1, n + 1)] for i in range(1, n + 1)]
    return sum(result, [])[left:right + 1]

# 시간복잡도 개선 코드 O(N)
def solution(n, left, right):
    result = []

    for i in range(left, right + 1):
        row = i // n
        col = i % n

        if col >= row:
            result.append(col + 1)
        else:
            result.append(row + 1)

    return result

# 다른 풀이
def solution(n, left, right) :
	result = []

	for i in range(left, right + 1) :
		result.append(max(i // n, i % n) + 1)

	return result

# lambda
solution = lambda n, left, right : list((max(i // n, i % n) + 1 for i in range(left, right + 1)))

if __name__ == '__main__' :
	print(solution(3, 2, 5))
	print(solution(4, 7, 14))