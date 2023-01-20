# 입력 조건
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100000보다 작거나 같다.
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 입력			출력
# 15			
# push 1		
# push 2		
# front			1
# back			2
# size			2
# empty			0
# pop			1
# pop			2
# pop			-1
# size			0
# empty			1
# pop			-1
# push 3		
# empty			0
# front			3

# TODO queue 기본 뼈대 코드 작성
class Queue(list) :
	
	# 정수 X를 큐에 넣는 연산이다.
	def push(self, x) :
		self.append(x)

	# 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
	# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	def pop(self) :
		if len(self) == 0 :
			return -1
		else :
			tmp = self[0]
			del self[0]
			
			return tmp

	# 큐에 들어있는 정수의 개수를 출력한다.
	def size(self) :
		return len(self)

	# 큐가 비어있으면 1, 아니면 0을 출력한다.
	def empty(self) :
		if len(self) == 0 :
			return 1
		else :
			return 0

	# 큐의 가장 앞에 있는 정수를 출력한다.
	# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	def front(self) :
		if len(self) == 0 :
			return -1
		else :
			return self[0]

	# 큐의 가장 뒤에 있는 정수를 출력한다.
	# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	def back(self) :
		if len(self) == 0 :
			return -1
		else : 
			return self[len(self) - 1]

# test bed
if __name__ == '__main__' :
	print(__name__)