export const square = (pow: number): bigint => {
  if (pow < 1 || pow > 64) {
    throw new Error(`Parameter pow must be in range [1-64]. Actual value: ${pow}`);
  }
  return BigInt(2 ** (pow - 1));
}

export const total = (): bigint => {
  let current: bigint = 1n;
  let sum: bigint = current;
  for (let i = 1; i < 64; i++) {
    current = current * 2n;
    sum += current;
  }

  return sum;
}
