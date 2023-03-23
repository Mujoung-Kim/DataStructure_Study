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

if __name__ == '__main__' :
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
    print(solution(" .. .... "))
    print(solution("\t"))
    print(solution(" "))
    print(solution("ABE"))