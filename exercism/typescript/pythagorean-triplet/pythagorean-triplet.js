export function triplets(input) {
    let foundTriplets = [];
    let minLength = input?.minFactor ?? 1;
    let maxLength = input?.maxFactor ?? input.sum / 2;
    for (let a = minLength; a < maxLength; a++) {
        for (let b = minLength; b < maxLength; b++) {
            for (let c = minLength; c < maxLength; c++) {
                if (a < b && b < c && a + b + c === input.sum) {
                    if (a ** 2 + b ** 2 === c ** 2) {
                        foundTriplets.push(new Triplet(a, b, c));
                    }
                }
            }
        }
    }
    return foundTriplets;
}
class Triplet {
    a;
    b;
    c;
    constructor(a, b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    toArray() {
        return [this.a, this.b, this.c];
    }
}
