function printGrade(midtermScore, finalScore){
	let totalScore = midtermScore + finalScore;
  // 여기에 코드를 작성해 주세요.
  if (totalScore >= 90) {
    console.log('A');
  }
  else if (totalScore >= 80) {
    console.log('B');
  }
  else if (totalScore >= 70) {
    console.log('C');
  }
  else if (totalScore >= 60) {
    console.log('D');
  }
  else {
    console.log('F');
  }
}

// 테스트 코드
printGrade(25, 35);
printGrade(50, 45);
printGrade(29, 24);
printGrade(37, 42);