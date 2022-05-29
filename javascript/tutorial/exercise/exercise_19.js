// 각 등급별 가격
let VIPPrice = 15;
let RPrice = 13;
let SPrice = 10;
let APrice = 8;

// 각 등급에 맞는 가격을 출력하는 함수 checkPrice를 완성하세요.
function checkPrice(grade) {
	// 여기에 코드를 작성해 주세요.
  function printLog(grade, price) {
    console.log(`${grade}석은 ${price}만원 입니다.`);
  }
  switch (grade) {
    case 'VIP':
      printLog('VIP', VIPPrice);
      break;
    case 'R':
      printLog('R', RPrice);
      break;
    case 'S':
      printLog('S', SPrice);
      break;
    case 'A':
      printLog('A', APrice);
      break;
    default:
      console.log('VIP, R, S, A 중에서 하나를 선택해 주세요.');
  }
}

// 테스트 코드
checkPrice('R');
checkPrice('VIP');
checkPrice('S');
checkPrice('A');
checkPrice('B');