# TODO 개념 정리 후 코드 작성

# TODO 조건식에 맞는 stack 구조로 변경
# 입력값 조건
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 입력					출력
# 7
# pop					-1
# top					-1
# push 123				123
# top					123
# pop					remove(123)
# top					-1
# pop					-1

class Stack(list) :

	# 정수 X를 스택에 넣는 연산이다.
	def push(self, x) :
		self.append(x)

	# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
	# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	# x -> pop()을 재귀호출로 인해서 실행이 안되는 것임
	def pop(self) :
		if len(self) == 0 :
			return -1
		else :
			del self[len(self) - 1]

	# 스택의 가장 위에 있는 정수를 출력한다.
	# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	def top(self) :
		if len(self) == 0 :
			return -1
		else :
			return self[-1]

	# 스택이 비어있으면 1, 아니면 0을 출력한다.
	def empty(self) :
		if len(self) == 0 :
			return 1
		else :
			return 0

	# 스택에 들어있는 정수의 개수를 출력한다.
	def size(self) :
		return len(self)

# test code
if __name__ == '__main__' :
	test_stack = Stack()
	print('Test bed')
	print(test_stack.empty())
	# print(test_stack.top())
	# test_stack.push(1)
	print(test_stack.pop())
	print(test_stack.top())
	test_stack.push(10)
	print(test_stack)
	test_stack.push(100)
	print(test_stack)
	print(test_stack.size())
	print(test_stack.top())
	test_stack.pop()
	print(test_stack.size())
	print(test_stack)
	print('empty = ', test_stack.empty())
	# print(test_stack.top())
	print(test_stack)