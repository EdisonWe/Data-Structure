'''
栈: FILO (先进后出)
'''

# create a stack
stack = []

# add element 时间复杂度 O(1)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
# [1,2,3]

# get the top of stack 时间复杂度 O(1)
print(stack[-1])
# 3

# remove the top of stack 时间复杂度 O(1)
temp = stack.pop()
print(temp)
# 3

# length 时间复杂度 O(1)
len(stack)

# Interate stack 时间复杂度 O(n)
while len(stack) > 0:
    temp1 = stack.pop()
    print(temp1)
# 3
# 2
# 1
