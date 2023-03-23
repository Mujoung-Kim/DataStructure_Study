# TODO : 예외사항 하나 찾아서 고쳐야됨.
# 스킬 트리
# 규칙
# 특정 스킬들은 선행조건대로만 배울 수 있다.
# 특정 스킬이 아닌경우 특정스킬 사이에 아무때나 나올 수 있다.

# 조건
# skill, skill_trees = ascii_uppercase
# type(skill) = str
# 1 <= len(skill) <= 26
# 1 <= len(skill_trees) <= 20
# 2 <= len(skill_trees.values) <= 26
# set(skill_trees.values) = True

# input / output
# skill	skill_trees                     	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
# "DBA" ["DEFBCA", "DAB", "CDEF", "AEDSB"]  2

# 예외사항 하나 뭐야
def solution(skill, skill_trees):
    tmp_dict = {}
    result, cnt = 0, 0

    for key in skill_trees:
        tmp = {}
        for val in skill :
            if val in key :
                tmp[val] = key.index(val)
            else:
                tmp[val] = 26 + cnt
                cnt += 1
        tmp_dict[key] = tmp

    sort_list = [sorted(value.values()) for _, value in tmp_dict.items()]
    cnt = 0

    for key, value in tmp_dict.items() :
        tmp_str = ''
        conver = {v:k for k, v in value.items()}
        print(conver)
        for val in sort_list[cnt] :
            if val < 26 :
                tmp_str += conver.get(val)
        print(tmp_str)
        if tmp_str == skill :
            result += 1
        cnt += 1

    return result

if __name__ == '__main__' :
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
    print(solution("DBA", ["DEFBCA", "DAB", "CDEF", "AEDSB"]))
    print(solution("CAD", ["C", "A", "D", "CAE"]))
    print(solution("A", ["DEFBCA", "DAB", "CDEF", "AEDSB"]))