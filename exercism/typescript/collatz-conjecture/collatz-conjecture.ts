export function steps(n: number): number {
  if (n <= 0) {
    throw new Error("Only positive numbers are allowed");
  }

  let steps: number = 0;
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = n * 3 + 1;
    }
    steps += 1;
  }

  return steps;
}
