// 여기에 orderSetMenu 함수를 작성해 주세요.
function orderSetMenu(sandwich, drink = '스프라이트') {
  console.log(`주문하신 ${sandwich}, ${drink} 세트메뉴 나왔습니다!`);
}

// 테스트 코드
orderSetMenu('코드웨잇 클럽');
orderSetMenu('터키베이컨 아보카도', '코카콜라');
orderSetMenu('코드웨잇 멜트');
orderSetMenu('이탈리안 비엠티', '닥터페퍼');
orderSetMenu('에그마요', '환타 오렌지');