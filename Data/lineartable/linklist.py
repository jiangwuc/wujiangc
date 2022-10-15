"""
单链表学习程序
"""

#创建节点类
class Node:
    def __init__(self,value,next = None):
        self.value = value  #有用数据[可以定义多个]
        self.next = next   #记录下一个节点的数据

#链表的操作
class LinkList:
    #初始化列表
    def __init__(self):
        # 创建一个无用节点，当做列表的开头。
        self.head = Node(None)

    #插入链表
    def init_list(self,l):
        # 保持head不动，一动就会丢失下一个节点的数据，让P进行移动
        p = self.head
        for item in l:
            #让新的节点等于P.next，使新节点与原来的节点相连接
            p.next = Node(item)
            # p要移动到下一个节点，需要将p等于新节点，
            # 因新节点已经赋给了p.next，所以，p = p.next
            # 不能让P直接等于Node（item）
            p = p.next

    #展示链表数据
    def show(self):
        # 将p指向第一个元素
        p = self.head.next

        #只要p不等于None，while循环不会结束
        while p:
            print(p.value,end=' ')
            p = p.next
        print()

    #尾部插入新的节点
    def append(self,item):
        #将P指向无用节点
        p = self.head
        #循环判断p的next是不是为空
        #为空，表示p已经到了最后一个节点
        # while p.next is not None 另一种写法
        #
        while p.next:
            p = p.next
        p.next = Node(item)

    #获取链表长度
    def get_length(self):
        n = 0
        #链表头不能算在长度里，他是一个无用的节点。
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
        return n

    #判断链表是否为空
    def is_empty(self):
        #直接判断链表的长度，如果为0，链表肯定是空
        if self.get_length() == 0:
            return True
        else:
            return False

    #清空链表
    def clear(self):
        #让链表的Next与后面的元素断开，将后面的元素抛弃
        #python有垃圾回收机制，不用去管
        self.head.next = None




if __name__ == '__main__':
    link = LinkList()
    #初始数据
    l = [1,2,3,4,5,6]
    #将初始数据插入链表
    link.init_list(l)
    #遍历链表
    link.show()
    #链表后插入数据
    link.append(7)
    link.show()
    #获取链表长度
    print(link.get_length())
    # 判断是否为空
    # print(link.is_empty())
    #清空链表
    # link.clear()
    # print(link.is_empty())






