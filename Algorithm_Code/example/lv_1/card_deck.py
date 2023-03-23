# 카드 뭉치
# 규칙

# 조건
# 1 <= card1, card2 <= 10
# 2 <= goal <= len(card1) + len(card2)
# card1, card2, goal -> alphabet 소문자만

# input / output
# ["i", "drink", "water"]				->	cards1
# ["want", "to"]						->	cares2
# ["i", "want", "to", "drink", "water"]	->	goal
# "Yes"									->	result
# ["i", "water", "drink"]				->	cards1
# ["want", "to"]						->	cards2
# ["i", "want", "to", "drink", "water"]	->	goal
# "No"									-> result

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

if __name__ == '__main__' :
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))