# def getElementByRank(nums):
#     nums_dict = {}
#     res = []

#     for idx, x in enumerate(sorted(nums)):
#         if x not in nums_dict:
#             nums_dict[x] = idx+1

#     for x in range(len(nums)):
#         res.append(nums_dict[nums[x]])
#     return res

# print(getElementByRank([-4, -2, -3, -7, -7]))

# def compact_matrix_distinct(A):
#   n = len(A[0])
#   m = len(A)
#   elements = sorted((el, col_num, row_num) for row_num, row in enumerate(A) for col_num, el in enumerate(row))

#   print('elements')
#   print(elements)
#   col_max = [0]*n
#   row_max = [0]*m
#   result = [[None]*n for _ in range(m)]

#   for el, col_num, row_num in elements:
#     print('----------------------')
#     print('el')
#     print(el)
#     new_el = max(col_max[col_num], row_max[row_num]) + 1
#     result[row_num][col_num] = new_el
#     col_max[col_num] = new_el
#     row_max[row_num] = new_el
#     print('rowMax')
#     print(row_max)
#     print('colMax')
#     print(col_max)
#     print('----------------------')

#   return result

# print('result:\n')
# print(compact_matrix_distinct([[1, 5, 6], [4, 3, 2], [8, 7, 9]]))
from collections import defaultdict
def compact_matrix(A):
  n = len(A[0])
  m = len(A)
  groups = defaultdict(list)
  result = [[None]*n for _ in range(m)]

  #[[1, 5, 6], [4, 5, 2], [4, 5, 9]]

  for row_num, row in enumerate(A):
    for col_num, el in enumerate(row):
      groups[el].append((col_num, row_num))

  print('groups')
  print(groups)

  col_max = [(0, None)]*n
  row_max = [(0, None)]*m

  def key(el):
    col_num, row_num = el
    x = -max(col_max[col_num][0], row_max[row_num][0])
    print('sorting with key: ' + str(x))
    return x

  for el, positions in sorted(groups.items()):
      print('***************************')
      print('el: ' + str(el))
      for col_num, row_num in sorted(positions, key=key):
        print('col_num: ' + str(col_num))
        print('row_num: ' + str(row_num))
        rel_col_max, val_col_max = col_max[col_num]
        rel_row_max, val_row_max = row_max[row_num]
        rel = max(rel_col_max + (val_col_max != el), rel_row_max + (val_row_max != el))
        result[row_num][col_num] = rel
        col_max[col_num] = (rel, el)
        row_max[row_num] = (rel, el)
        print('col_max: ' + str(col_max))
        print('row_max: ' + str(row_max))
        print('result')
        print(result)
      print('***************************')

  return result

print('result:\n')
print(compact_matrix([[1, 5, 6], [4, 5, 2], [4, 5, 9]]))


