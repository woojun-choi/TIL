const N = 180;
// 여기에 코드를 작성해 주세요.
let i = 1;
let measure = 0;

while (i <= N) {
  if (N % i === 0) {
    console.log(i);
    measure++;
  }
  i++;
}
console.log(`${N}의 약수는 총 ${measure}개입니다.`);