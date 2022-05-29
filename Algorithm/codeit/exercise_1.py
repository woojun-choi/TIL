def is_palindrome(word):
  idx = len(word) - 1
  for i in word:
    if i != word[idx]:
      return False
    idx -= 1
  return True


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
