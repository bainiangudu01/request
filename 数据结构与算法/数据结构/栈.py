class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):  # 进栈
        self.stack.append(element)

    def pop(self):  # 出栈
        return self.stack.pop()

    def get_top(self):  # 取栈顶，如果栈是空，返回不了，需要判断一下
        if len(self.stack) > 0:  # 如果栈的长度大于0，返回栈顶，否则返回None
            return self.stack[-1]
        else:
            return False

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):  # 括号匹配函数，参数是一个字符串
    match = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:  # 循环读这个字符串
        if ch in {'(', '[', '{'}:  # 如果字符是这三个括号中的一个，就进栈
            stack.push(ch)
        else:  # ch in {'}',']',')'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:  # 如果和栈顶是匹配的，就将栈顶pop出来
                stack.pop()
            else:  # stack.get_top() != match[ch]
                return False
    if stack.is_empty():  # 循环完之后如果栈是空的，就匹配了
        return True
    else:
        return False

print(brace_match('{}[](){()}{[()]}'))
