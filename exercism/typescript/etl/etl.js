export function transform(input) {
    let output = {};
    for (let key in input) {
        for (let value of input[key]) {
            output[value.toLowerCase()] = parseInt(key);
        }
    }
    return output;
}
