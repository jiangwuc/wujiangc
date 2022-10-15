"""
栈:链表存储
永远在头节点侧执行入栈，出栈操作
"""

#自定义一个异常，不需要代码实现
class LStackError(Exception):
    pass

#定义一个节点
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LStack:
    def __init__(self):
        #标识栈顶位置
        self._top = None
    #判断栈顶是否空
    def is_empty(self):
        return self._top is None

    #入栈
    def push(self,item):
        #创建一个节点
        node = Node(item)
        #将新节点的Next = top
        node.next = self._top
        #将top移动到新节点
        self._top = node
        #也可以写成:self._top
        #self._top = Node(item,self._top)
    #出栈
    def pop(self):
        #如果顶是空的，则返回错误
        if self._top is None:
            raise LStackError("stack is empty")
        #将p设置为顶,p不做移动
        p = self._top
        #将top移动到下一个节点
        self._top = p.next
        #返回栈顶的值
        return p.value
    #查看栈顶元素
    def top(self):
        if self._top is None:
            raise  LStackError("stack is empty")
        return self._top.value




if __name__ == '__main__':
    st = LStack()
    print(st.is_empty())

    st.push(10)
    st.push(20)
    st.push(30)

    print(st.top())

    while not  st.is_empty():
        print(st.pop())
