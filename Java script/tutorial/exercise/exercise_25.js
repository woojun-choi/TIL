let first = 1;
let second = 1;

for (let i = 0; i < 25; i++) {
  console.log(first);
  console.log(second);
  first = first + second;
  second = first + second;
}