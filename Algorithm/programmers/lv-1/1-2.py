#Failed
def solution(numbers):
  answer = []
  answer_idx = 0
  idx = 0

  def add(a, b):
    return a+b

  for i in range(0, len(numbers)):
    j = i + 1
    while j < len(numbers):
      num = add(numbers[i], numbers[j])
      if answer_idx > 0:
        for x in range(0, len(answer)):
          if num < answer[x]:
            idx = x
            break
          if num == answer[x]:
            idx = -1
            break
        if idx > -1:
          answer.insert(idx, num)
          answer_idx += 1
        if idx == -1:
          continue
      else:
        answer.append(num)
        answer_idx += 1
      j += 1

  return answer
