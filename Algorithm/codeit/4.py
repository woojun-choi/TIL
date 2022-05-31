#선택정렬
#이건 뭐가 문제여;
def selection_sort(list):
  def list_min_idx(fir, list):
    min_idx = fir
    for i in range((len(list) - fir)):
      if list[min_idx] > list[i]:
        min_idx = i
      else:
        continue
    return min_idx
  s = 0
  for i in range(len(list)):
    idx = list_min_idx(i, list)
    s = list[i]
    list[i] = list[idx]
    list[idx] = s
  return list


def ss(list):
  idx = 0
  s = 0
  for i in range(len(list)):
    idx = i
    for j in range(i, len(list)):
      if list[idx] > list[j]:
        idx = j
    # s = list[i]
    # list[i] = list[idx]
    # list[idx] = s
    list[i], list[idx] = list[idx], list[i]
  return list

print(ss([5, 3, 4, 1, 2, 6]))
print(ss([1, 2, 7, 4, 9, 3]))
print(ss([10, 6, 3, 6, 2, 4, 1, 5, 1]))