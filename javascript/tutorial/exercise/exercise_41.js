function isPalindrome(word) {
  // 여기에 코드를 입력해 주세요.
  let count = 0;

  for (let i = 0; i < Math.floor(word.length / 2); i++) {
    if (word[i] === word[word.length - 1 - i]) {
      count++;
    }
  }

  if (count === Math.floor(word.length / 2)) {
    return true;
  }
  else {
    return false;
  }
}

// 테스트 코드
console.log(isPalindrome("racecar"));
console.log(isPalindrome("stars"));
console.log(isPalindrome("기러기"));
console.log(isPalindrome("123321"));
console.log(isPalindrome("hello"));
console.log(isPalindrome("kayak"));