# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-16 08:41
# @Author  : yanlei
# @FileName: one_hundred_thirteen_eight.py
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None

        # If we have already processed the current node,then we simply return the clone vision of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # Create a new node
        # with the value same as old node
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be loops during
        # traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)  # 先将所有的node都创建好，然后从最后一个node，给random赋值，一直回溯到第一个node
        node.random = self.copyRandomList(head.random)

        return node


numlist = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]


# 创建带随机指针的链表
def createRandomLinkedList(list):
    endcursor = Node(None, None, None)
    end = endcursor
    head = end

    for item in numlist[:][::-1]:
        # print(item)
        head = Node(item[0], endcursor, None)
        endcursor = head

    cursor_node = head
    i = 0
    while cursor_node.next is not None:
        # 当前结点的随机指针指向的位置
        cursor_random = numlist[i][1]
        if cursor_random is None:
            cursor_node.random = end
            cursor_node = cursor_node.next
            i += 1
            continue
        # 用临时指针找到该位置
        tmp = head
        while cursor_random > 0:
            tmp = tmp.next
            cursor_random -= 1

        cursor_node.random = tmp
        cursor_node = cursor_node.next
        i += 1

    return head


# 读取带随机指针的链表
def getRandomLinkedList(head):
    # 线性读取每一个node，将值放到list中
    cursor_head = head
    ret_list = []
    while cursor_head.next is not None:
        tmp = []
        tmp.append(cursor_head.val)
        # 获取随机指针指向结点的索引
        random_node = cursor_head.random
        if random_node.val is None:
            tmp.append(None)
        else:
            random_node_index = 0
            tmp_node = head
            while random_node != tmp_node:
                tmp_node = tmp_node.next
                random_node_index += 1

            tmp.append(random_node_index)

        ret_list.append(tmp)
        cursor_head = cursor_head.next

    return ret_list


head = createRandomLinkedList(numlist)
new_head = Solution().copyRandomList(head)
# print(getRandomLinkedList(new_head))
getRandomLinkedList(new_head)


