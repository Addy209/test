// function curry(f) {
//   return function(a) {
//     return function(b) {
//       return f(a, b);
//     };
//   };
// }

// function sum(a, b) {
//   return a + b;
// }

// let curriedSum = curry(sum);

// console.log( curriedSum(1)(2) );

function test(a, b, c) {
  b = b ?? 0.5;
  console.log(a, b, c);
}

test(4, 0, 45);
