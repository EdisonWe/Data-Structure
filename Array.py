'''
在连续内存空间中，存储一组相同类型的数据。
区分数组中的元素 索引以及 数组访问(access)和数组搜索(search)。
数组特点：读多写少
'''
# Create an array
array = []

# add element 时间复杂度 O(1)
array.append(1)
array.append(2)
# [1,2]
print(array)

# insert element 时间复杂度 O(n)
array.insert(1, 99)
# [1,99,2]
print(array)

# Access element 时间复杂度 O(1)
print(array[2])
# 2

# update element 时间复杂度 O(1)
array[2] = 88
# [1,99,88]
print(array)

# remove element 时间复杂度 O(n)
array.remove(88)
# [1,99]
print(array)

array.pop(1)  # pop的是索引
# [1]
print(array)

array.pop()  # 删除当前数组中的最后一个元素 时间复杂度 O(1)
# []
print(array)

# get array size
a = [1, 2, 3]
size = len(a)
# 3
print(size)

# Iterate array 遍历数组 时间复杂度 O(n)
for i in a:
    print(i)
# 1
# 2
# 3

for index, element in enumerate(a):
    print("Index at", index, "is", element)
# Index at 0 is 1
# Index at 1 is 2
# Index at 2 is 3

for i in range(0, len(a)):
    print("i:", i, "element:", a[i])
# i: 0 element: 1
# i: 1 element: 2
# i: 2 element: 3

# find element 时间复杂度 O(n)
index = a.index(2)
# 1
print(index)

# sort an array 时间复杂度 O(n)
a = [3, 1, 2]
a.sort()
# [1,2,3]
print(a)

# 反转
a.sort(reverse=True)
# [3,2,1]
print(a)
