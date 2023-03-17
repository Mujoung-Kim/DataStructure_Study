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

if __name__  == '__main__' :
    # print(solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    # print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))
    pass