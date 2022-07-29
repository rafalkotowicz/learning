export class Series {
    base;
    constructor(series) {
        if (series.length > 0) {
            this.base = (series);
        }
        else {
            throw new Error("series cannot be empty");
        }
    }
    slices(sliceLength) {
        if (sliceLength === 0) {
            throw new Error("slice length cannot be zero");
        }
        else if (sliceLength < 0) {
            throw new Error("slice length cannot be negative");
        }
        else if (sliceLength > this.base.length) {
            throw new Error("slice length cannot be greater than series length");
        }
        let result = [];
        for (let curr = 0; curr < this.base.length - sliceLength + 1; curr++) {
            result.push(this.base.substring(curr, curr + sliceLength).split("").map(x => parseInt(x)));
        }
        return result;
    }
}
