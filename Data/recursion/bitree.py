"""
二叉树的构建与遍历
"""
#构建二叉树节点
from Data.queue.squeue import *
class TreeNode:
    def __init__(self,data = None,left = None,right =None ):
        self.data = data
        self.left = left
        self.right = right
#二叉树类
class Bitree:
    def __init__(self,root = None):
        self.root = root

    #判断Tree是否为空
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    #先序递归，不管是那种遍历，都是先打印根
    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    #中序遍历
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data,end=" ")
        self.inOrder(node.right)

    #后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=" ")

    #层次遍历，使用队列的思想实现
    def levelOrder(self,node):
        if node is None:
            return
        #导入链式队列的代码
        qu = SQueue()
        #将根节点压入队列
        qu.enqueue(node)
        while not qu.is_empty():
            #在将根节点出列，再将这个根节点下的子节点入列
            node = qu.deuqeue()
            print(node.data,end=" ")
            #需要判断左右子节点是否为None，如果为None，则不入列
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)



"""
            A
          /   \
        B       C
              /   \
            D      E
          /   \   /   \
        F     G  I    H
"""
if __name__ == '__main__':
    #按照后续的方式增加节点
    B = TreeNode("B")
    F = TreeNode("F")
    G = TreeNode("G")
    D = TreeNode("D",F,G)
    I = TreeNode("I")
    H = TreeNode("H")
    E = TreeNode("E",I,H)
    C = TreeNode("C",D,E)
    A = TreeNode("A",B,C)

    bt = Bitree(A)
    bt.preOrder(bt.root)
    print()
    print("inOreder...")
    bt.inOrder(bt.root)
    print()
    print("postOreder...")
    bt.postOrder(bt.root)
    print()
    bt.levelOrder(bt.root)