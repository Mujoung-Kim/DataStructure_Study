# TODO : 시간복잡도 + 예외사항이 있음
# 신고 결과 받기
# 규칙
# 각 유저는 한 번에 한 명의 유저만 신고
# 동일한 대상에서 신고한 횟수는 1회로 처리
# k만큼 신고받으면 정지하고 신고한 유저들에게 알림

# 조건
# 2 <= len(id_list) <= 1000
# 1 <= len(id_list.elements) <= 10
# id_list.elements = ascii_lowercase
# set(id_list)
# 1 <= len(report) <= 200000
# 3 <= len(report.element) <= 21
# report.element = "userid reportid"
# id => ascii_lowercase
# 자기 자신은 신고하지 않는다.
# 1 <= k <= 200, k => int
# return sorted(id_list)순으로 정지된 유저 수를 반환
# 10초안에 결과 반환

# input / output
# ["muzi", "frodo", "apeach", "neo"]	->  id_list
# ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	->  report
# 2                                     ->  k
# [2,1,1,0]                             ->  result
# ["con", "ryan"]                                   ->  id_list
# ["ryan con", "ryan con", "ryan con", "ryan con"]  ->  report
# 3	                                                ->  k
# [0,0]                                             ->  result

# import time
# import sys, collections
# from time import strftime

def solution(id_list, report, k) :
    id_set, set_repo = list(dict.fromkeys(id_list)), set(report)
    tmp_res = {}
    result, tmp = [], []

    # O(1)
    for id in id_set :
        tmp_res[id] = { 'report_id': [], 'count': 0}

    # O(1)
    for val in set_repo :
        sender, reporter = map(str, val.split())
        if sender in tmp_res.keys() :
            tmp_res[sender]['report_id'].append(reporter)
            tmp.append(reporter)

    # O(N)
    for val in tmp :
        if tmp.count(val) < k :
            tmp.pop(tmp.index(val))

    # O(N)
    for value in set(tmp) :
        for _, val in tmp_res.items() :
            if value in val['report_id'] :
                val['count'] += 1

    # O(1)
    for _, val in tmp_res.items() :
        result.append(val['count'])

    return result

def solution(id_list, report, k) :
    set_id, set_req = list(dict.fromkeys(id_list)), set(report)
    report_dict = {}
    result = []

    if (len(set_id) - 1) <= k :
        for _ in range(len(set_id)) :
            result.append(0)

    for id in set_id :
        if id not in report_dict :
            report_dict['user'] = id
        else :
            report_dict['user'] += id
        report_dict['count'] = 0

    return report_dict

    # return result

if __name__ == '__main__' :
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))