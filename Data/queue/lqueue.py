"""
队列:链式存储的实现
链表的头做为队头，链表的尾做为队尾。
"""
class QueueError(Exception):
    pass

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LQueue:
    def __init__(self):
        #初始化两个节点
        self.front = self.rear=Node(None)

    #对象的相等，一般用is，不用==
    def is_empty(self):
        return self.front is self.rear

    #入队
    def enquere(self,item):
        #在尾部添加一个新的节点
        #再讲rear移动到新的节点
        #保持rear一直在队尾，这样可以不必每次都循环到队尾进行插入操作
        self.rear.next = Node(item)
        self.rear = self.rear.next

    #出队
    def dequeue(self):
        if self.front is self.rear:
            raise QueueError("Queue is Empty")
        #讲front 移动到下一个节点
        self.front = self.front.next
        #返回front移动到节点的值
        #返回后，相当于该值改为了None
        return self.front.value

    #清空队列
    def clear(self):
        self.front = self.rear


if __name__ == '__main__':
    lq = LQueue()
    print(lq.is_empty())
    lq.enquere(12)
    lq.enquere(13)
    lq.enquere(14)
    while not lq.is_empty():
        print(lq.dequeue())

