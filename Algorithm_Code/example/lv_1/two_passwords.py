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

if __name__ == '__main__' :
    print(solution("aukks", "wbqd", 5))