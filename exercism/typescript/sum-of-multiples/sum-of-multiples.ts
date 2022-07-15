export function sum(multiples: number[], limit: number): number {
  let sum: number = 0;
  for (let curr = 0; curr < limit; curr++) {
    for (let multiple of multiples) {
      if (curr % multiple === 0) {
        sum += curr;
        break;
      }
    }
  }

  return sum;
}
