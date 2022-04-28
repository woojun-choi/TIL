// 여기에 코드를 작성해 주세요.
function interestCalculator(rate, payment, term) {
  console.log(Math.round(payment * term * (term + 1) / 2 * rate / 12));
};


// 이율이 4.3%일 때 매월 80만원씩 24개월 납입할 경우
interestCalculator(0.043, 800000, 24);

// 이율이 4.3%일 때 매월 60만원씩 24개월 납입할 경우
interestCalculator(0.043, 600000, 24);