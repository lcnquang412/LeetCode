function findAllDivisors(num: number): number[] {
  const divisors: number[] = [];
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) {
      divisors.push(i);
      if (num / i !== i) {
        divisors.push(i);
      }
    }
  }
  return divisors;
}

// Greatest Common Divisor
function gcd(a: number, b: number): number {
  // console.log("[Here] ", a, b);
  return b > 0 ? gcd(b, a % b) : a;
}

console.log("[Here] ", gcd(6, 12));
