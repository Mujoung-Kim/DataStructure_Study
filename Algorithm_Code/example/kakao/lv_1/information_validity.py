# TODO : pri_date 값이 주어진 값과 다름 이것만 해결하면 됨
# 개인정보 수집 유효기간
# 규칙

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

if __name__ == '__main__' :
    print(solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))