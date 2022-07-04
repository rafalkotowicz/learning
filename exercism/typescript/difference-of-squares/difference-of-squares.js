export class Squares {
    _count;
    constructor(count) {
        this._count = count;
    }
    createSequence() {
        return [...Array(this._count + 1).keys()];
    }
    get sumOfSquares() {
        return this.createSequence().map(x => x ** 2).reduce((x, y) => x + y);
    }
    get squareOfSum() {
        return (this.createSequence().reduce((x, y) => x + y)) ** 2;
    }
    get difference() {
        return this.squareOfSum - this.sumOfSquares;
    }
}
