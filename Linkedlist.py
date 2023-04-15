from collections import deque

# create linkedlit
linkedlist = deque()  # 因为双端队列deque可以在队列两端添加或删除数据，所以可以用作表示链表的一种方式。

# 定义节点类链表


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# add element 时间复杂度 O(1)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
# [1,2,3]
print(linkedlist)

# Insert element 时间复杂度 O(n)
linkedlist.insert(2, 99)
# [1,2,99,3]
print(linkedlist)

# Access element 时间复杂度 O(n)
element = linkedlist[2]
# 99
print(element)

# search element 时间复杂度 O(n)
index = linkedlist.index(99)
# 2
print(index)

# update element 时间复杂度 O(n)
linkedlist[2] = 88
# [1,2,88,3]
print(linkedlist)

# remove element 时间复杂度 O(n)
linkedlist.remove(88)
# [1,2,3]
print(linkedlist)

# length 时间复杂度 O(n)
length = len(linkedlist)
# 3
print(length)
