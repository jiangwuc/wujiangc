"""
队列：顺序存储的实现
"""

#队列异常
class QueueError(Exception):
    pass

# 完成队列操作
class SQueue():
    #初始化队列，使用列表存储数据
    def __init__(self):
        self._elems = []

    #判断队列是否为空
    def is_empty(self):
        return self._elems == []

    #入队
    def enqueue(self,item):
        #在列表尾部加入数据
        self._elems.append(item)
    #出队
    def deuqeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        #将列表的第一元素弹出
        return self._elems.pop(0)

    # 清空队列
    def clear(self):
        self._elems = []


if __name__ == '__main__':
    sq = SQueue()
    print(sq.is_empty())
    sq.enqueue(12)
    sq.enqueue(13)
    sq.enqueue(14)

    while not sq.is_empty():
        print(sq.deuqeue())