"""
基本算法，冒泡排序，选择排序，插入排序
"""
class BubbleSort:
    def __init__(self,list_):
        self.list_ = list_

    #冒泡排序
    def bubble(self):
        #外层循环比较多轮
        for i in range(len(self.list_)-1):
            #内存循环表示每轮比较的次数
            for k in range(len(self.list_) -i -1):
                #前一个数比后一个数大，则交换位置
                if self.list_[k] >= self.list_[k+1]:
                    self.list_[k],self.list_[k+1] = self.list_[k+1],self.list_[k]

    #选择排序
    def select(self):
        #比较多少轮
        for i in range(len(self.list_) -1):
            #假定最小数
            min = i
            for j in range(i + 1,len(self.list_)):
                #碰到比假定数小的数，则将小的数赋值给假定数
                if self.list_[min] > self.list_[j]:
                    min = j
            #完成一轮循环后，再交换，可以减少交换的数量
            if i != min:
                self.list_[i],self.list_[min] = self.list_[min],self.list_[i]

    #插入排序
    def insert(self):
        for i in range(1,len(self.list_)):
            #定义一个变量
            x = self.list_[i]
            #通过将j不断的变成前面一个值，与i进行比较
            j = i
            while j > 0 and self.list_[j-1] > x :
                self.list_[j] = self.list_[j -1]
                j -=1
            #最后将定义的值赋给j
            self.list_[j] = x

    def sub_sort(self, low, high):
        # [4,1,2,6,7,3,9,8]
        # 定义基准数
        key = self.list_[low]
        while low < high:
            # low < high 建立在不断的循环之后，有可能会出现low 》 high
            #后面的数向前甩
            while low < high and self.list_[low] > key:
                high -= 1
            self.list_[low] = self.list_[high]
            # 前面的数向后甩
            while low < high and self.list_[low] < key:
                low += 1
            self.list_[high] = self.list_[low]
        self.list_[low] = key
        return low

    # 快速排序，递归实现
    def quick(self, low, high):
        # low列表开头元素索引
        # high 列表结尾元素索引
        if low < high:
            key = self.sub_sort(low, high)
            self.quick(low,key -1)
            self.quick(key + 1,high)




import random
if __name__ == "__main__":
    list1 = []
    while len(list1) < 50:
        x = random.randint(1,100)
        if x not in list1:
            list1.append(x)
    print(list1)
    l = BubbleSort(list1)
    l.bubble()
    print(l.list_)
    # l.select()
    # print(l.list_)
    # l.insert()
    # print(l.list_)
    l.quick(0,len(list1) -1)
    print(l.list_)


