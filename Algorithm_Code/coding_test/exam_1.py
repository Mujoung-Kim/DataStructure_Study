# 변수들의 조건
# 1 <= serial_number <= 200,000,000 
# k : serial_number(total_sum) / k == 144 < k <= 10,000
# n -> 1 <= n <= 10,000
# 사과 패드를 산다면 Y, 살 수 없다면 N 입출력은 space, enter, tab
# -> input map(str)로 조건줘서 입력값을 받도록 설정하면됨

# input / output example
# 4 145	-> n, k
# 100 100 100 101 -> serial_number
# YES -> result
# 4 145
# 100 45 142 199
# YES
def solution(n, k, serial_number) :
    result = 0

    for index in range(0, n) :
        result = int(serial_number[index])

        if int(serial_number[index]) % k == 144 :
            print(int(serial_number[index]) % 144)
            return 'YES'

        # if result % k == 144:
        #     return 'YES'
        # else :
        #     return 'NO'

n_k, s = map(str, [input(), input()])
n = int(n_k.split()[0])
k = int(n_k.split()[1])

print(solution(n, k, s.split()))