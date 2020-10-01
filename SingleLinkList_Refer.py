class Node(object):
    """定义一个节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
 
 """定义一个单链表""" 
class SingleLinkList(object):
   
    def __init__(self, node=None):
        self.__head = node
"""链表是否为空"""
    def is_empty(self):
        
        return self.__head is None
"""链表的长度"""
    def length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
 """遍历整个链表"""
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")
 """链表头部添加元素"""
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
  """链表尾部添加元素"""
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
 """指定位置添加元素:param pos 从0开始(即将链表的第一个节点记为0节点)"""
    # pos/position:位置，方位 param:参数
    def insert(self, pos, item):
        # pre/previous以前的，在什么之前
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
  """删除节点"""
    def remove(self, item):
        pre = self.__head
        # 判断是不是空链表
        if pre == None:
            return False
        # 判断是不是头结点，包含了只有一个节点情况
        elif pre.elem == item:
            self.__head = pre.next
            # pre = None
            return True
        else:
            while pre.next != None:
                if pre.next.elem == item:
                    pre.next = pre.next.next
                    return True
                else:
                    pre = pre.next
            return False
  """查找节点是否存在"""
    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == '__main__':
    sll = SingleLinkList()
 
    print(sll.remove(4))
    sll.travel()
    print("----------")
    sll.append(2)
    print(sll.search(2))
    print(sll.remove(2))
    print("----------")
    sll.append(2)
    sll.append(3)
    sll.append(5)
    sll.append(6)
    sll.append(7)
    sll.travel()
    sll.add(1)
    sll.travel()
    sll.insert(3, 4)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.remove(7)
    sll.travel()
    sll.remove(4)
    sll.travel()
    print(sll.remove(100))
    sll.travel()
    print(sll.search(6))