export function findGreatestCommonDivisor(a: number, b: number): number {
  a = Math.abs(a);
  b = Math.abs(b);
  let gcd: number = 0;

  for (let i = 1; i <= a || i <= b; i++) {
    if (a % i === 0 && b % i === 0) {
      gcd = i;
    }
  }
  return gcd;
}

export class Rational {
  numerator: number;
  denominator: number;

  constructor(a: number, b: number) {
    this.numerator = a;
    if (b !== 0) {
      this.denominator = b;
    } else {
      throw new Error("Denominator cannot be 0")
    }
  }

  add(other: Rational): Rational {
    let a1: number = this.numerator;
    let b1: number = this.denominator;
    let a2: number = other.numerator;
    let b2: number = other.denominator;
    this.numerator = a1 * b2 + a2 * b1;
    this.denominator = b1 * b2;

    return this.reduce();
  }

  sub(other: Rational): Rational {
    let a1: number = this.numerator;
    let b1: number = this.denominator;
    let a2: number = other.numerator;
    let b2: number = other.denominator;
    this.numerator = a1 * b2 - a2 * b1;
    this.denominator = b1 * b2;

    return this.reduce();
  }

  mul(other: Rational): Rational {
    let a1: number = this.numerator;
    let b1: number = this.denominator;
    let a2: number = other.numerator;
    let b2: number = other.denominator;
    this.numerator = a1 * a2;
    this.denominator = b1 * b2;

    return this.reduce();
  }

  div(other: Rational): Rational {
    let a1: number = this.numerator;
    let b1: number = this.denominator;
    let a2: number = other.numerator;
    let b2: number = other.denominator;
    this.numerator = a1 * b2;
    this.denominator = a2 * b1;

    return this.reduce();
  }

  abs() {
    this.numerator = Math.abs(this.numerator);
    this.denominator = Math.abs(this.denominator)

    return this.reduce();
  }

  exprational(exponential: number): Rational {
    this.numerator = this.numerator ** exponential;
    this.denominator = this.denominator ** exponential;

    return this.reduce();
  }

  expreal(exponential: number): number {
    // lack of precision 8^(4/3) = ~16 for Math.pow(8, 4/3); Math.cbrt returned more accurate result
    if (this.denominator === 3) {
      return Math.cbrt(exponential ** this.numerator);
    }
    return Math.pow(exponential, this.numerator / this.denominator);
  }

  reduce(): Rational {
    if (this.numerator === 0) {
      this.denominator = 1;
      return this;
    }
    let gcd: number = findGreatestCommonDivisor(this.numerator, this.denominator)
    this.numerator /= gcd;
    this.denominator /= gcd;
    if ((this.numerator < 0 && this.denominator < 0) || (this.numerator > 0 && this.denominator < 0)) {
      this.numerator = -this.numerator;
      this.denominator = -this.denominator;
    }
    return this;
  }
}