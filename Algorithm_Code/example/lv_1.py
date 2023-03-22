# 카드뭉치

# 조건
# 1 <= card1, card2 <= 10
# 2 <= goal <= len(card1) + len(card2)
# card1, card2, goal -> alphabet 소문자만

# input / output
# cards1	cards2	goal	result
# ["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"
# ["i", "water", "drink"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"No"

def solution(card1, card2, goal) :
    result, answer = '', ''

    for val in goal :
        result += val

    for index in range(len(goal)) :
        if len(card1) != 0 and goal[index] == card1[0]:
            answer += card1.pop(0)
        elif len(card2) != 0 and goal[index] == card2[0]:
            answer += card2.pop(0)

    if result == answer :
        return 'Yes'
    else :
        return 'No'

# code 개선
def solution(card1, card2, goal) :
    for val in goal :
        if len(card1) > 0 and val == card1[0] :
            card1.pop(0)
        elif len(card2) > 0 and val == card2[0] :
            card2.pop(0)
        else :
            return 'No'
        
    return 'Yes'

# 둘만의 암호
# 규칙
# s의 값에서 index만큼 뒤에 있는값 대신skip이면 다음

# 조건
# 5 <= s <= 50
# 1 <= skip <= 10
# 1 <= index <= 20
# s, skip은 alphabet 소문자
# skip에 포함되는 문자는 s에 포함되지 않음

# input / output
# s	skip	index	result
# "aukks"	"wbqd"	5	"happy"

# list
def solution(s, skip, index) :
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''

    for val in skip :
        if val in alpha :
            alpha.pop(alpha.index(val))
    for val in s :
        if val in alpha :
            result += alpha[(alpha.index(val) + index) % len(alpha)]

    return result

# string
def solution(s, skip, index) :
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for val in skip :
        if val in alpha :
            alpha = alpha.replace(val, '')
    for val in s :
        if val in alpha :
            result += alpha[(alpha.index(val) + index) % len(alpha)]

    return result

# string type gpt refactoring
def solution(s, skip, index):
    # create a set of characters to skip for faster lookup
    skip_set = set(skip)
    
    # create a list of valid characters
    alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip_set]
    
    # initialize the result string
    result = ''
    
    # loop through each character in the input string
    for char in s:
        # skip characters in the skip set
        if char in skip_set:
            result += char
        else:
            # get the index of the character in the valid character list
            char_index = alpha.index(char)
            # apply the given index shift and wrap around if necessary
            shifted_index = (char_index + index) % len(alpha)
            # append the shifted character to the result string
            result += alpha[shifted_index]
    
    return result

# code 개선
from string import ascii_lowercase

def solution(s, skip, index) :
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)

    dic_alpha = {alpha : idx for idx, alpha in enumerate(a_to_z)}

    for val in s :
        result += a_to_z[(dic_alpha[val] + index) % len(a_to_z)]

    return result

# 개인정보 수집 유효기간
# TODO : pri_date 값이 주어진 값과 다름 이것만 해결하면 됨

# 조건
# date_format = YYYY.MM.DD
# 2000 <= YYYY <= 2022
# 1 <= MM <= 12
# 1 <= DD <= 28
# 1 <= term <= 20
# 1 <= privacies <= 100

# input / output	
# "2022.05.19" -> today
# ["A 6", "B 12", "C 3"] -> terms	
# ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] -> privacies
# [1, 3] -> result

# "2020.01.01" -> today
# ["Z 3", "D 5"] -> terms
# ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	
# [1, 4, 5] -> result
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies) :
    now = datetime.strptime(today, '%Y.%m.%d').date()
    pri_res = []
    result = []

    for val in privacies :
        for idx in range(len(terms)) :
            if terms[idx].split()[0] in val :
                # 이 부분이 문제인거 같은데 뭘까?
                pri_res.append(
                    datetime.strptime(val.split()[0], '%Y.%m.%d').date() + 
                    relativedelta(months=int(terms[idx].split()[1]))
                )
    for val in pri_res :
        if now > val :
            result.append(pri_res.index(val) + 1)

    return result

def string_to_date(date) :
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies) :
    pri_res = []
    result = []

    now = string_to_date(today)

    for val in privacies :
        for idx in range(len(terms)) :
            if terms[idx].split()[0] in val :
                pri_res.append(string_to_date(val.split()[0]) +
                                (int(terms[idx].split()[1]) * 28))
    for val in pri_res :
        if now >= val :
            result.append(pri_res.index(val) + 1)

    return result

# 쓰레기 답변
# def solution(today, terms, privacies):
#     now = datetime.strptime(today, '%Y.%m.%d').date()
#     pri_res = []
#     result = []

#     for val in privacies:
#         for idx in range(len(terms)):
#             if terms[idx].split()[0] in val:
#                 target_date = datetime.strptime(val.split()[0], '%Y.%m.%d').date()
#                 # target_date에 대해 months만큼 더하기
#                 year, month, day = target_date.year, target_date.month, target_date.day
#                 month += int(terms[idx].split()[1])
#                 # month를 조정
#                 if month > 12:
#                     year += 1
#                     month -= 12
#                 result_date = datetime(year, month, day).date()
#                 pri_res.append(result_date)

#     for val in pri_res:
#         if now > val:
#             result.append(pri_res.index(val) + 1)

#     return result

def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day
    
def solution(today, terms, privacies):
    answer = []
    
    # today
    today = dateToDay(today)
    
    # terms
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28
    
    # privacies
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToDay(date) + termsInfo[term] <= today:
            answer.append(i+1)
        
    return answer

# 성격유형 검사하기
# 규칙
# 배열로 풀라는 거 같은데?

# 조건
# surver, choice -> array[]
# 1 <= len(survey) <= 1000
# survey = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
# len(choices) = len(survey)
# 1 <= choices.key <= 7
# 0 <= choices.value <= 3

# input / output
# ["AN", "CF", "MJ", "RT", "NA"]    ->  survey
# [5, 3, 2, 7, 5]       	        ->  choices
# "TCMA"                            ->  result
# ["TR", "RT", "TR"]	            ->  survey
# [7, 1, 3]	                        ->  choices
# "RCJA"                            ->  result

def solution(survey, choices) :
    result = ''
    sur_val = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    cho_val = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}

    for idx in range(len(survey)) :
        if choices[idx] < 4 :
            sur_val[survey[idx][0:1]] = sur_val[survey[idx][0:1]] + cho_val[choices[idx]]
        elif choices[idx] > 4 :
            sur_val[survey[idx][1:2]] = sur_val[survey[idx][1:2]] + cho_val[choices[idx]]

    if sur_val['R'] >= sur_val['T'] :
        result += list(sur_val.keys())[0]
    else :
        result += list(sur_val.keys())[1]
    if sur_val['C'] >= sur_val['F'] :
        result += list(sur_val.keys())[2]
    else :
        result += list(sur_val.keys())[3]
    if sur_val['J'] >= sur_val['M'] :
        result += list(sur_val.keys())[4]
    else :
        result += list(sur_val.keys())[5]
    if sur_val['A'] >= sur_val['N'] :
        result += list(sur_val.keys())[6]
    else :
        result += list(sur_val.keys())[7]

    return result

# 이거 조금 다듬으면 될듯?
def solution(survey, choices):
    result = ''
    CATEGORIES = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    sur_val = {category: 0 for category in CATEGORIES}
    cho_val = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

    for idx in range(len(survey)):
        if choices[idx] < 4:
            sur_val[survey[idx][0]] += cho_val[choices[idx]]
        elif choices[idx] > 4:
            sur_val[survey[idx][1]] += cho_val[choices[idx]]

    sorted_categories = sorted(sur_val, key=sur_val.get, reverse=True)
    result += sorted_categories[0] + sorted_categories[2] + sorted_categories[4] + sorted_categories[6]

    return result

# 다른 풀이 zip 활용
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

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

# 숫자 문자열과 영단어
# 규칙
# 숫자의 일부 자릿수를 영단어로 바꾼다.
# 일부 숫자는 바뀌거나 바뀌지 않거나 ㅁ?ㄹ
# 바꾸기 전의 값을 그대로 반환해라.

# 조건
# 1 <= len(s) <= 50
# s는 zero or 0으로 시작하지 않는다.
# 1 <= s <= 2000000000
# s -> int
# 10초안에 결과 도출

# input / output
# s                     result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"    234567
# "123"	                123

# 일단 시간복잡도는 개나 줬음
def solution(s) :
    alpha_list = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 
                  'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 
                  'eight' : 8, 'nine' : 9}
    result, tmp = '', []

    for val in list(s) :
        if val.isalpha() == True :
            result += val
            if result in alpha_list.keys() :
                tmp.append(alpha_list.get(result))
                result = result.replace(result, '')
        elif val.isdecimal() == True :
            tmp.append(val)

    for val in tmp :
        result += str(val)

    return int(result)

# 다른 풀이
def solution(s) :
    alpha_list = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 
                'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 
                'eight' : 8, 'nine' : 9}
    result = s

    for key, value in alpha_list.items() :
        result = result.replace(key, value)

    return int(result)

# list 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
             'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

# 신규 아이디 추천
# 규칙
# id의 길이는 3 <= id <= 15
# id는 ascii_lowercase, 0 ~ 9, -, _, .만 사용가능
# .는 처음과 끝에 쓸 수 없으며 연속해서도 사용할 수 없다.
# 1 단계 : new_id -> lower()
# 2 단계 : new_id -> 이용 가능한 문자를 제외한 모든 문자 제거
# 3 단계 : new_id -> .이 연속해서 나오면 하나의 .으로 변경
# 4 단계 : new_id -> .이 처음과 끝에 존재한다면 제거
# 5 단계 : new_id -> 빈 문자열이라면 a를 대입
# 6 단계 : new_id -> 길이가 16자 이상이라면 제거 
#                    만약 제거후 15번째 글자에 .이 존재한다면 제거
# 7 단계 : new_id -> 2자 이하라면 마지막 문자를 3자가 되도록 반복

# 조건
# 1 <= new_id <= 1000
# id.values in ascii_lowercase, 0 ~ 9, -, _, .
# new_id에 들어오는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/로 한정

# input / output
# no	new_id	                        result
# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	                    "z--"
# 예3	"=.="	                        "aaa"
# 예4	"123_.def"	                    "123_.def"
# 예5	"abcdefghijklmn.p"	            "abcdefghijklmn"

import re

# ?? 어디서 예외가 발생하는 거지?
def solution(new_id) :
    per_str = list(ascii_lowercase + '-' + '_' + '.') + list(str(list(range(10))))
    result = ''

    for val in list(new_id.lower()) :
        if val in per_str :
            result += val

    result = re.sub(r'\.{2,}', ".", result)

    if (result.startswith('.') or result.endswith('.')) and len(result) > 1 :
        result = result.replace('.', '', 1)
    elif len(result) > 0 and len(result) <= 1 :
        result = result.replace('.', '')
    
    if result == '' :
        result += 'a'
    
    if len(result) >= 16 :
        result = result[0:15]

    if result.endswith('.') :
        result = result.replace('.', '', 1)
    
    while len(result) < 3 :
        result += result[-1]

    return result

def solution(new_id) :
    result = ''
    new_id = new_id.lower()

    for val in new_id :
        if val in ['-', '_', '.'] or val.isalpha() or val.isdecimal() :
            result += val

    result = re.sub(r'\.{2,}', '.', result)

    if len(result) > 0 :
        if len(result) > 1 and result[0] == '.' :
            result = result[1:]
        elif result[0] == '.' :
            result = result.replace('.', '')
        if len(result) > 1 and result[-1] == '.' :
            result = result[:-1]

    if result == '' :
        result += 'a'

    if len(result) >= 16 :
        result = result[0:15]
        if result.endswith('.') :
            result = result[:-1]

    while len(result) < 3 :
        result += result[-1]

    return result

# 정규식 풀이
def solution(new_id) :
    result = new_id.lower()
    result = re.sub('[^a-z0-9\-_.]', '', result)
    result = re.sub('\.+', '.', result)
    result = re.sub('^[.]|[.]$', '', result)
    result = 'a' if len(result) == 0 else result[:15]
    result = re.sub('^[.]|[.]$', '', result)
    result = result if len(result) > 2 else result + ''.join([result[-1] for i in range(3 - len(result))])

    return result

if __name__  == '__main__' :
    # print(solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    # print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
    # print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    # print(solution(["TR", "RT", "TR"], [7, 1, 3]))
    # print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
    # print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
    # print(solution("one4seveneight"))
    # print(solution("1234"))
    # print(solution("...!@BaT#*..y.abcdefghijklm"))
    # print(solution("z-+.^."))
    # print(solution("=.="))
    # print(solution("123_.def"))
    # print(solution("abcdefghijklmn.p"))
    # print(solution(" .. .... "))
    # print(solution("\t"))
    # print(solution(" "))
    # print(solution("ABE"))
    # print(solution())
    pass