"""
栈：顺序存储
"""

#自定义一个异常类，栈异常
class StackError(Exception):
    pass


class SStack:
    #初始化一个栈，基于列表进行操作
    #私有变量，双下划线，外面不能调用
    #单下划线，告诉调用者，这是是受保护的变量，实际相当于普通变量，
    #
    def __init__(self):
        self._elems = []

    #栈顶元素，列表的最后一个元素为栈顶元素
    #只能从列表列尾进行操作
    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        #返回列表最后一个元素
        return self._elems[-1]

    #判断列表是否为空
    #如果列表为空，返回True
    def is_empty(self):
        return self._elems == []

    #入栈操作
    def push(self,elem):
        self._elems.append(elem)

    #出栈操作
    def pop(self):
        #如果列表为空，则返回错误
        if not self._elems:
            raise StackError("stack is empty")
        #返回列表最后一个元素
        return self._elems.pop()

if __name__ == '__main__':
    #初始化一个栈
    sstack = SStack()
    print(sstack.is_empty())
    sstack.push(10)
    sstack.push(20)
    sstack.push(30)
    print(sstack.top())

    while not sstack.is_empty():
        print(sstack.pop())
