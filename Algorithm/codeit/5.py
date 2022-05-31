#삽입 정렬? 이거 맞아?
def insertion_sort(list):
  for pointer in range(1, len(list)):
    idx = -1
    for i in range(pointer, 0, -1):
      if list[i - 1] > list[i]:
        list[i - 1], list[i] = list[i], list[i - 1]
  return list

def ins_sort(list):
  key = 0
  for i in range(1, len(list)):
    key = list[i]
    for j in range(i - 1, -1, -1):
      if list[j] > key:
        list[j + 1] = list[j]
    list[j + 1] = key
  return list


print(insertion_sort([5, 3, 4, 1, 2, 6]))
print(insertion_sort([1, 2, 7, 4, 9, 3]))
print(insertion_sort([10, 6, 3, 6, 2, 4, 1, 5, 1]))
print(ins_sort([5, 3, 4, 1, 2, 6]))
print(ins_sort([1, 2, 7, 4, 9, 3]))
print(ins_sort([10, 6, 3, 6, 2, 4, 1, 5, 1]))
