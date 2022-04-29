function calculateChange(payment, cost) {
  // 코드를 작성해 주세요.
  let money = payment - cost;
  console.log(`50000원 지폐: ${Math.floor(money / 50000)}장`);
  money = money % 50000;
  console.log(`10000원 지폐: ${Math.floor(money / 10000)}장`);
  money = money % 10000;
  console.log(`5000원 지폐: ${Math.floor(money / 5000)}장`);
  money = money % 5000;
  console.log(`1000원 지폐: ${Math.floor(money / 1000)}장`);
}

// 테스트 코드
calculateChange(100000, 33000);
console.log('');
calculateChange(500000, 378000);