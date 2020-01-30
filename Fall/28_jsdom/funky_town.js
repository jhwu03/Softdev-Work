function fibonacci(n){
  if (n == 0) return 0;
  if (n == 1) return 1;
  if (n == 2) return 1;
  return fibonacci(n-1) + fibonacci(n-2);
}

var myfib = fibonacci;
document.getElementById("1").addEventListener("click", () => console.log(myfib(7)));

// function gcd(a, b){
//   if (a == 0) return b;
//   if (b == 0) return a;
//   if (a == b) return a;
//   if (a > b) return gcd(a-b, b);
//   return gcd(a, b-a);
// }
//
// var mygcd = gcd;

var gcd = function(a, b){
  if (b == 0) {return a;}
  else return gcd(b, a % b);
}
document.getElementById("2").addEventListener("click", () => console.log(gcd(124,324)));


var names = ["Ethan", "David", "William", "Jionghao", "Tim", "Kevin"]

function randomStudent(){
  return randSHelper(names);
}

function randSHelper(){
  i = Math.floor(Math.random() * names.length);
  return names[i];
}

var randName = randomStudent;

document.getElementById("3").addEventListener("click", () => console.log(randomStudent()));
