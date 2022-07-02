export class ComplexNumber {
    _real;
    _imaginary;
    constructor(real, imaginary) {
        this._real = real;
        this._imaginary = imaginary;
    }
    get real() {
        return this._real;
    }
    get imag() {
        return this._imaginary;
    }
    add(other) {
        return new ComplexNumber(this._real + other._real, this._imaginary + other._imaginary);
    }
    sub(other) {
        return new ComplexNumber(this._real - other._real, this._imaginary - other._imaginary);
    }
    div(other) {
        let a = this._real;
        let b = this._imaginary;
        let c = other._real;
        let d = other._imaginary;
        return new ComplexNumber((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2));
    }
    mul(other) {
        let a = this._real;
        let b = this._imaginary;
        let c = other._real;
        let d = other._imaginary;
        return new ComplexNumber(a * c - b * d, b * c + a * d);
    }
    get abs() {
        return Math.sqrt(this._real ** 2 + this._imaginary ** 2);
    }
    get conj() {
        return new ComplexNumber(this._real, this._imaginary === 0 ? 0 : -this._imaginary);
    }
    get exp() {
        // e^(a + i * b) = e^a * e^(i * b)`, the last term of which is given by Euler's formula `e^(i * b) = cos(b) + i * sin(b)
        let e = Math.E;
        let a = this._real;
        let b = this._imaginary;
        return new ComplexNumber(e ** a * Math.cos(b), e ** a * Math.sin(b));
    }
}
