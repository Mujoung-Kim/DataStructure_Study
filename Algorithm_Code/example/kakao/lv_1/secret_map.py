# 비밀지도
# 규칙
# 1. 한 변의 길이는 num, 각 칸은 "" or "#" 둘 중 하나이다.
# 2. 전체 지도는 arr1, arr2 중 하나라도 "#"인 부분은 전체지도도 "#"이다.
# 3. arr1, arr2 모두 ""인 부분은 전체지도에서도 ""이다.
# 4. arr1, arr2는 각각의 int 값은 이진수로 변환한 암호값이다.
# 5. 암호화된 배열에서 "#" : 1, "" : 0으로 형성된다.

# 조건
# 1 <= num <= 16
# arr1, arr2 -> len(num)인 정수
# 각 배열의 값을 이진수로 변환 했을 때 x <= len(num)
# 0 <= x <= 2^n-1

# input / output
# 5																->	n
# [9, 20, 28, 18, 11]											->	arr1
# [30, 1, 21, 17, 28]											->	arr2
# ["#####","# # #", "### #", "# ##", "#####"]					->	result

# 6																->	n
# [46, 33, 33 ,22, 31, 50]										->	arr1
# [27 ,56, 19, 14, 14, 10]										->	arr2
# ["######", "### #", "## ##", " #### ", " #####", "### # "]	->	result

# function 생성
def solution(num, arr1, arr2) :
	arr1_b = [get_binary(val).zfill(num) if len(get_binary(val)) < num else get_binary(val) for val in arr1]
	arr2_b = [get_binary(val).zfill(num) if len(get_binary(val)) < num else get_binary(val) for val in arr2]
	result = []

	for v1, v2 in zip(arr1_b, arr2_b) :
		tmp = ''
		for idx in range(num) :
			if v1[idx] == '1' or v2[idx] == '1' :
				tmp += '1'
			elif v1[idx] == '0' and v2[idx] == '0' :
				tmp += '0'
		result.append(tmp)

	for idx in range(len(result)) :
		result[idx] = result[idx].replace('1', '#')
		result[idx] = result[idx].replace('0', ' ')

	return result

def get_binary(num) :
	tmp = []

	while True :
		remainder = num % 2
		num = num // 2
		
		tmp.append(remainder)

		if num < 2 :
			tmp.append(num)
			break

	tmp.reverse()
	
	return ''.join(map(str, tmp))

# rjust 사용
def solution(num, arr1, arr2) :
	result = []

	for v1, v2 in zip(arr1, arr2) :
		tmp = str(bin(v1|v2)[2:])
		tmp = tmp.rjust(num, '0')
		tmp = tmp.replace('1', '#')
		tmp = tmp.replace('0', ' ')

		result.append(tmp)

	return result

# lambda
solution = lambda num, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(num))) for row in (a|b for a, b in zip(arr1, arr2))])

if __name__ == '__main__' :
	print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
	print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))