export function classify(num: number): string {
  if (num <= 0) {
    throw new Error("Classification is only possible for natural numbers.")
  }

  let factors: number[] = []
  if (num === 1) {
    return "deficient";
  } else {
    for (let i = 0; i <= num / 2; i++) {
      if (num % i === 0) {
        factors.push(i)
      }
    }
  }

  let aliquotSum = factors.reduce((x, y) => x + y);

  if (aliquotSum === num) {
    return "perfect";
  } else if (aliquotSum > num) {
    return "abundant";
  } else {
    return "deficient";
  }
}
