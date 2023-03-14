# 입력 조건
# n (1 <= n <= 2000000)
# n은 실행횟수

# input/output exaple
# 8
# abcdghjk
# 8 -> result
# 11
# f2ddeiffabe
# 7 -> result => 이거 값이 이상한듯? 소문자만이면 10개 중복제거면 7
def solution(n, s) :
    result = 0

    if 'f' in s :
        print('enter f')
        if 'e' in s :
            pass
    elif 'i' in s :
        print('enter i')
        # 다음 index의 문자
        pass
    else :
        return len(s)
    
    return f'n : {n}, e : {s}'

n, s = map(str, [input(), input()])

print(solution(n, s))