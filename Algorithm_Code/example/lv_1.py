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

def solution(s, skip, index) :
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''

    for val in skip :
        if val in alpha :
            alpha.pop(alpha.index(val))
    for val in s :
        if val in alpha :
            if len(alpha) <= alpha.index(val) + index :
                result += alpha[(alpha.index(val) + index) - len(alpha)]
            else :    
                result += alpha[alpha.index(val) + index]

    return result

if __name__  == '__main__' :
    print(solution('aukks', 'wbqd', 5))
    pass