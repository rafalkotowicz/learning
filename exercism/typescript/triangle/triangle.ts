export class Triangle {
  a: number
  b: number
  c: number

  constructor(...sides: number[]) {
    this.a = sides[0];
    this.b = sides[1];
    this.c = sides[2];
  }

  private checkZeroLengthSides(): boolean {
    return this.a === 0 || this.b === 0 || this.c === 0;
  }

  private isTriangle(): boolean {
    return this.a + this.b > this.c &&
      this.a + this.c > this.b &&
      this.b + this.c > this.a;
  }

  get isEquilateral(): boolean {
    if (this.checkZeroLengthSides() || !this.isTriangle()) {
      return false
    }
    return this.a === this.b && this.b === this.c && this.c === this.a;
  }

  get isIsosceles(): boolean {
    if (this.checkZeroLengthSides() || !this.isTriangle()) {
      return false
    }
    return this.a === this.b || this.b === this.c || this.c === this.a;
  }

  get isScalene(): boolean {
    if (this.checkZeroLengthSides() || !this.isTriangle()) {
      return false
    }
    return (this.a !== this.b) && (this.b !== this.c) && (this.c !== this.a);
  }
}
