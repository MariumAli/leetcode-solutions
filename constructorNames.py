def constructorNames(a, b):
    m1 = dict()
    m2 = dict()
    
    for i in a:
        m1[i] = m1.get(i, 0) + 1
    for i in b:
        m2[i] = m2.get(i, 0) + 1
    print(m1)

    print('-----------')
    print(m2)
    if (m1.keys() != m2.keys()):
        return False
    
    r1 = dict()
    r2 = dict()
    for i in m1.values():
        r1[i] = r1.get(i, 0) + 1
    
    for i in m2.values():
        r2[i] = r2.get(i, 0) + 1

    print(r1)
    print('-----------')
    print(r2)
    
    return  r1 == r2
print(constructorNames('babczzz', 'abbzccc'))

# def find_2_largest(nums):
#     len_nums = len(nums)
#     if len_nums < 2:
#         raise ValueError('Invalid Input')
#     first = second = - (sys.maxint-1)

#     for num in nums:
#         if compare(num, first):
#             second = first
#             first = num
#         if compare(num, second) and num != first:
#             second = num
#     return second
