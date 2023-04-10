# 주차 요금 계산
# 규칙
# fees => [기본시간, 기본요금, 단위시간, 단위요금]
# records => ["시각 차량번호 내역", "시각 차량번호 내역", ...]
# 요금 계산 example
# 차량번호	누적 주차 시간	주차요금
# 0000		34 + 300 = 334	5000(기본요금) + [(334-180(기본시간)) / 10] * 600 = 14600

# 조건
# len(fees) = 4
# 1 <= fees[0] <= 1439 -> fees[0] : 기본 시간(분)
# 0 <= fees[1] <= 100000 -> fees[1] : 기본 요금(원)
# 1 <= fees[2] <= 1439 -> fees[2] : 단위 시간(분)
# 1 <= fees[3] <= 10000 -> fees[3] : 단위 요금(원)
# 1 <= len(records) <= 1000
# records.elements	->	"시각 차량번호 내역"으로 구분
# 					->	시각 = HH:MM, len(시각) == 5, 00:00 <= 시각 <= 23:59
# 					->	차량번호 = 0 ~ 9 사이의 값으로 구성된 길이4인 문자열
# 					->	내역 = "IN" : 입 or "OUT" : 출
# 					->	시각을 기준으로 오름차순되어 있다.
# 					->	들어온 차량이 다음날 나가는 경우는 없다.
# 					->	같은 시각, 같은 차량번호의 내역은 중복되지 않음

# input / output
# [180, 5000, 10, 600]	->	fees
# ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]		->	records
# [14600, 34400, 5000]	->	result
# [120, 0, 60, 591]		->	fees
# ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]		->	records
# [0, 591]				->	result
# [1, 461, 1, 10]		->	fees	
# ["00:00 1234 IN"]		->	records
# [14841]				->	result

def change_min(time) :
	return int(time.split(':')[0]) * 60 + int(time.split(':')[-1])

def solution(fees, records) :
	parking_dict = {}
	parking_time = 0
	result = []

	# parking_dict
	for sen in records :
		time, number, park = map(str, sen.split(' '))
		
		if number not in parking_dict :
			parking_dict[number] = {}
		if park not in parking_dict[number] :
			parking_dict[number][park] = []
		parking_dict[number][park].append(change_min(time))

	# return parking_dict

	# parking_time
	# XXX : 0, 591이 안나옴 -> 'IN'을 한 번만 돌리니까 그럼
	# 서순 정리랑 parking_time을 이전값이랑 누적해서 계산하도록 바꿔야됨.
	for key in parking_dict :
		print(parking_time)
		if 'OUT' in parking_dict[key] :
			parking_time += parking_dict[key]['OUT'].pop(0) - parking_dict[key]['IN'].pop(0)
		else :
			parking_time += change_min('23:59') - parking_dict[key]['IN'].pop(0)
		print(parking_time)
		if parking_time <= fees[0] :
			fee = fees[1]
			result.append(fee)
		else :
			fee = int(fees[1] + (parking_time - fees[0]) / fees[2] * fees[3])
			result.append(fee)
	
	return result

def solution(fees, records) :
	parking_dict = {}
	result = []

	# 이건 아무리 생각해도 dict
	for sen in records :
		time, number, park = map(str, sen.split(' '))

		if number not in parking_dict :
			parking_dict[number] = {}
		if park not in parking_dict[number] :
			parking_dict[number][park] = []
		parking_dict[number][park].append(change_min(time))

	return parking_dict
	return result

if __name__ == '__main__' :
	print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
	print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
	print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))