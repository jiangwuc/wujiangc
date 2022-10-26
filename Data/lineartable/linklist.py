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

    #获取某个索引的值
    def get_item(self, item):
        #让P指向第一个节点，这样才会第一个数据为0
        p = self.head.next
        n = 0
        #没有到对应的索引且遍历索引没有到最后就循环
        #and：一个为假，全部为假.or :一个为真，全为真
        while n < item and p is not None:
            p = p.next
            n += 1
        #如果因为P到了最后，则说明越界
        if p is None:
            #主动报错
            raise IndexError("list index out of range")
        #不小于索引，说明找到了索引节点。
        return p.value

    #在某个索引位置插入数据
    def insert(self,index,val):
        #self.get_length() ,可以在后面插入
        if index< 0 or index > self.get_length():
            raise IndexError("list index out of range")
        p = self.head
        i = 0
        #让p移动到待插入位置的前一个
        while i < index:
            p = p.next
            i += 1
        #创建新的节点
        p_new = Node(val)
        # 将新节点的next 等于下一个节点
        p_new.next = p.next
        # 将新节点赋给前一个节点的next
        p.next = p_new

    #根据值删除链表中的某一个节点
    def delete(self,item):
        p = self.head
        while p.next is not None:
            #如果值相等，则越过中间的节点
            if p.next.value == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("%d not in list"%item)



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
    #获取某个节点值
    print(link.get_item(3))

    #在某个索引位置插入数据
    link.insert(5,10)
    link.show()
    # link.delete(30)
    link.show()




