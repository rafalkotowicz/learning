export function valid(digitString) {
    let digitStringNormalized = digitString.replaceAll(" ", "");
    if (digitStringNormalized === "0") {
        return false;
    }
    // let reversedNumbers: number[] = [...digitStringNormalized].map(x => parseInt(x)).reverse();
    // for (let i = 0; i < reversedNumbers.length; i++) {
    //   if (i % 2 === 1) {
    //     let tmp = reversedNumbers[i] * 2
    //     reversedNumbers[i] = tmp > 9 ? tmp - 9 : tmp;
    //   }
    // }
    // return reversedNumbers.reduce((x, y) => x + y) % 10 === 0;
    return [...digitStringNormalized]
        .map(x => parseInt(x))
        .reverse()
        .map((x, i) => {
        if (i % 2 === 1) {
            let tmp = x * 2;
            return tmp > 9 ? tmp - 9 : tmp;
        }
        else {
            return x;
        }
    })
        .reduce((x, y) => x + y) % 10 === 0;
}
