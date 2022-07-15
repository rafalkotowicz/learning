export function sum(multiples, limit) {
    let sum = 0;
    for (let curr = 0; curr < limit; curr++) {
        for (let multiple of multiples) {
            if (curr % multiple === 0) {
                sum += curr;
                break;
            }
        }
    }
    return sum;
}
