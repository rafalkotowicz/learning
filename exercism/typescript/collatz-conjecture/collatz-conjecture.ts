export function steps(n: number): number {
  if (n <= 0) {
    throw new Error("Only positive numbers are allowed");
  }

  return count_steps(n, 0);
}

function count_steps(n: number, steps: number): number {
  if (n == 1) {
    return steps;
  } else if (n % 2 === 0) {
    n = n / 2;
  } else {
    n = n * 3 + 1;
  }
  return count_steps(n, steps + 1); // This line is unreachable, but TypeScript requires a return statement
}
