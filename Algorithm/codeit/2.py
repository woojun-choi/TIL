def linear_search(element, some_list):
  idx = -1
  for i in list(range(len(some_list))):
    if element == some_list[i]:
      idx = i
  if idx != -1:
    return idx
  else:
    return None


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

#뭐가 다를까.. 
# def linear_search(element, some_list):
#     for i in range(len(some_list)):
#         if some_list[i] == element:
#             return i
#     return None


# # 테스트
# print(linear_search(2, [2, 3, 5, 7, 11]))
# print(linear_search(0, [2, 3, 5, 7, 11]))
# print(linear_search(5, [2, 3, 5, 7, 11]))
# print(linear_search(3, [2, 3, 5, 7, 11]))
# print(linear_search(11, [2, 3, 5, 7, 11]))
