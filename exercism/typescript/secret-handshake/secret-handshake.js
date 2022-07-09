export function commands(input) {
    let result = [];
    let binaries = Number(input).toString(2).split("").map(x => parseInt(x)).reverse();
    for (let pos = 0; pos < binaries.length; pos++) {
        if (pos === 0 && binaries[pos] === 1) {
            result.push("wink");
        }
        if (pos === 1 && binaries[pos] === 1) {
            result.push("double blink");
        }
        if (pos === 2 && binaries[pos] === 1) {
            result.push("close your eyes");
        }
        if (pos === 3 && binaries[pos] === 1) {
            result.push("jump");
        }
        if (pos === 4 && binaries[pos] === 1) {
            result.reverse();
        }
    }
    return result;
}
