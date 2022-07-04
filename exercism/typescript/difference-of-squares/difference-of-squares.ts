export class Squares {
  _count: number;

  constructor(count: number) {
    this._count = count;
  }

  private createSequence(): number[] {
    return [...Array(this._count + 1).keys()];
  }

  get sumOfSquares(): number {
    return this.createSequence().map(x => x ** 2).reduce((x, y) => x + y);
  }

  get squareOfSum(): number {
    return (this.createSequence().reduce((x, y) => x + y)) ** 2;
  }

  get difference(): number {
    return this.squareOfSum - this.sumOfSquares;
  }
}
