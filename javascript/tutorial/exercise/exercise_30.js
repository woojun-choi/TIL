let today = new Date(2112, 8, 24);
let jaeSangStart = new Date(2109, 7, 1);

function workDayCalc(startDate) {
	// 여기에 코드를 작성해 주세요.
	let workDay = ((today - startDate) / 1000 / 60 / 60 / 24) + 1;
  // today.getTime() - startDtae.getTime() 암묵적으로 형변환이 되지만 용도파악(?)을 사용해주는 것이 좋다.

  console.log(`오늘은 입사한 지 ${workDay}일째 되는 날 입니다.`);
}

workDayCalc(jaeSangStart);

//모범답안
// let today = new Date(2112, 8, 24);
// let jaeSangStart = new Date(2109, 7, 1);

// function workDayCalc(startDate) {
//   // 여기에 코드를 작성해 주세요.
//   let timeDiff = today.getTime() - startDate.getTime();
//   let dayDiff = timeDiff / 1000 / 60 / 60 / 24;

//   console.log(`오늘은 입사한 지 ${dayDiff + 1}일째 되는 날 입니다.`);
// }

// workDayCalc(jaeSangStart);