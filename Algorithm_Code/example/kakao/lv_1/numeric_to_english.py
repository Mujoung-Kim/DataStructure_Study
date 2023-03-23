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

if __name__ == '__main__' :
    print(solution("one4seveneight"))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("1234"))