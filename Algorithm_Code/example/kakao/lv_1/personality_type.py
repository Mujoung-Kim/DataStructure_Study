# 성격 유형 검사하기
# 규칙

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

if __name__ == '__main__' :
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))