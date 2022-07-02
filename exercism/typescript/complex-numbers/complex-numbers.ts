export class ComplexNumber {
  _real: number;
  _imaginary: number;

  constructor(real: number, imaginary: number) {
    this._real = real;
    this._imaginary = imaginary;
  }

  public get real(): number {
    return this._real;
  }

  public get imag(): number {
    return this._imaginary;
  }

  public add(other: ComplexNumber): ComplexNumber {
    return new ComplexNumber(this._real + other._real, this._imaginary + other._imaginary);
  }

  public sub(other: ComplexNumber): ComplexNumber {
    return new ComplexNumber(this._real - other._real, this._imaginary - other._imaginary);
  }

  public div(other: ComplexNumber): ComplexNumber {
    let a: number = this._real
    let b: number = this._imaginary
    let c: number = other._real
    let d: number = other._imaginary
    return new ComplexNumber((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))
  }

  public mul(other: ComplexNumber): ComplexNumber {
    let a: number = this._real
    let b: number = this._imaginary
    let c: number = other._real
    let d: number = other._imaginary
    return new ComplexNumber(a * c - b * d, b * c + a * d)
  }

  public get abs(): number {
    return Math.sqrt(this._real ** 2 + this._imaginary ** 2);
  }

  public get conj(): ComplexNumber {
    return new ComplexNumber(this._real, this._imaginary === 0 ? 0 : -this._imaginary);
  }

  public get exp(): ComplexNumber {
    // e^(a + i * b) = e^a * e^(i * b)`, the last term of which is given by Euler's formula `e^(i * b) = cos(b) + i * sin(b)
    let e: number = Math.E
    let a: number = this._real
    let b: number = this._imaginary
    return new ComplexNumber(e ** a * Math.cos(b), e ** a * Math.sin(b))
  }
}
