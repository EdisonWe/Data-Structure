'''
哈希表 = 散列表
键值对 key : value
python中可以用字典
'''

# create hashtable by array
hashTable = [''] * 4

# create hashtable by dictionary
mapping = {}

# add element 时间复杂度 O(1)
hashTable[1] = 'edison'
hashTable[2] = 'alexa'
hashTable[3] = 'frank'
mapping[1] = 'edison'
mapping[2] = 'alexa'
mapping[3] = 'frank'
print(mapping)
# {1: 'edison', 2: 'alexa', 3: 'frank'}

# update element 时间复杂度 O(1)
hashTable[1] = 'lee'
mapping[1] = 'lee'
print(mapping)
# {1: 'lee', 2: 'alexa', 3: 'frank'}

# remove element 时间复杂度 O(1)
hashTable[1] = ''
mapping.pop(1)
print(mapping)
# {2: 'alexa', 3: 'frank'}

# get value 时间复杂度 O(1)
hashTable[1]
mapping[1]

# check key 时间复杂度 O(1)
3 in mapping

# length
len(mapping)
