'''
集合特点 1. 无序 2. 不重复 所有元素都是独一无二的
主要作用 1. 检查某一个元素是否存在  2. 重复元素

'''

# create set
s = set()

# add element O(1)
s.add(10)
s.add(3)
s.add(4)
s.add(5)
s.add(3)

print(s)
# {10, 3, 4, 5}

# search element O(1)
3 in s

# delete element O(1)
s.remove(3)
print(s)
# {10, 4, 5}

# length O(1)
len(s)
