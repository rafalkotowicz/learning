export function reverse(input) {
    if (input === "") {
        return "";
    }
    return input.split("").reverse().reduce((x, y) => x + y);
}
