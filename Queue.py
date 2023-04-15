'''
队列: FIFO(先进先出)
单端队列 一个口仅进，一个口仅出
双端队列 两个口都可以进出
'''
from collections import deque

# create queue
queue = deque()

# add element 时间复杂度 O(1)
queue.append(1)
queue.append(2)
queue.append(3)
# [1,2,3]
print(queue)

# get the head of the queue 时间复杂度 O(1)
temp1 = queue[0]
# 1
print(temp1)

# remove the head of the queue 时间复杂度 O(1)
temp2 = queue.popleft()
# 1
print(temp2)

# [2,3]
print(queue)

# queue is empty? 时间复杂度 O(1)
print(len(queue) == 0)
# False

# Interate queue 时间复杂度 O(n)
while len(queue) != 0:
    temp = queue.popleft()
    print(temp)
# 2
# 3
