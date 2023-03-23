# 실패율
# 규칙
# 스테이지에 도달했으나 못깬 플레이어 수 / 스테이지에 도달한 플레이어수
# 전체 스테이지의 수 = N
# 실패율이 높은 스테이지부터 내림차순으로 반환

# 조건
# 1 <= N <= 500
# 1 <= len(stage) <= 200000
# 1 <= stage <= N + 1
# N + 1은 마지막 스테이지까지 클리어한 유저
# 실패율이 같은 경우 작은수가 먼저
# 도달한 유저가 없는 경우 해당 스페이지의 실패율은 0

# input / output
# N	stages	                    result
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	                [4,1,2,3]

# O(NlogN)
def solution(N, stages) :
    tmp_dict = dict.fromkeys(range(1, N + 2), 0)
    tmp = dict.fromkeys(range(1, N + 1), 0)
    set_stage = list(set(stages))

    for val in stages :
        if val in tmp_dict.keys() :
            tmp_dict[val] += 1

    for val in set_stage :
        if val > N :
            set_stage.pop(set_stage.index(val))
            set_stage.append(N)

    for val in set_stage :
        if tmp_dict[val] != 0 :
            tmp[val] = (tmp_dict[val] / len(stages))
        else :
            tmp[val] = 0
        for _ in range(tmp_dict[val]) :
            stages.pop(stages.index(val))

    sorted_dict = sorted(tmp.items(), reverse=True, key=lambda item: item[1])

    return [key for key, _ in sorted_dict]

# 시간복잡도 개선 코드 O(NlogN)
def solution(N, stages) :
    failures = [0] * (N + 2)
    total_players = len(stages)
    failure_rates = {}

    for stage in stages:
        failures[stage] += 1

    for stage in range(1, N + 1):
        if total_players > 0:
            failure_rate = failures[stage] / total_players
            failure_rates[stage] = failure_rate
            total_players -= failures[stage]
        else:
            failure_rates[stage] = 0

    return sorted(failure_rates, key=failure_rates.get, reverse=True)

if __name__ == '__main__' :
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4,4,4,4,4]))