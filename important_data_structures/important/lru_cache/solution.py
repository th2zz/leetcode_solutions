class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key, self.value, self.next = key, value, next


class LRUCache:
    """
    https://www.lintcode.com/problem/134/?_from=collection&fromId=161
    Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example
Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
Hash Table
Doubly Linked List
Linked List
Related Problems
538
Memcache
Medium
24
LFU Cache
Hard

    """

    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.key_to_prev_node = {}

    def push_back(self, node):  # append
        self.key_to_prev_node[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.key_to_prev_node:  # key 不存在于cache
            return -1
        self.kick(key)  # 刚被访问过 应该移到链表末尾
        return self.tail.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if key in self.key_to_prev_node:
            self.kick(key)
            self.tail.value = value
            return
        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev_node) > self.capacity:
            self.pop_front()

    def pop_front(self):
        head = self.dummy.next  # 需要删除的头
        del self.key_to_prev_node[head.key]
        self.dummy.next = head.next  # dummy next后移
        self.key_to_prev_node[head.next.key] = self.dummy  # 更新新的头的key_to_prev映射关系

    def kick(self, key):  # 将key节点移动到尾部
        prev_node = self.key_to_prev_node[key]
        key_node = prev_node.next
        if key_node == self.tail:
            return
        # 删掉key节点, push_back key node
        prev_node.next = key_node.next  # prev_node next指向key_node next
        self.key_to_prev_node[key_node.next.key] = prev_node  # 记录key_node next key对应的前一个节点 即prev_node
        key_node.next = None
        self.push_back(key_node)
