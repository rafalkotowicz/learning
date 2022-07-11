// Plain:  abcdefghijklmnopqrstuvwxyz
// Cipher: zyxwvutsrqponmlkjihgfedcba
const plain = "abcdefghijklmnopqrstuvwxyz";
const cipher = "zyxwvutsrqponmlkjihgfedcba";
export function sanitizeInput(unsanitized) {
    let cutUnwantedCharachers = unsanitized.replaceAll(new RegExp("[ ,.]", "g"), "");
    return cutUnwantedCharachers.split("").map(x => x.toLowerCase()).join("");
}
export function cutToChunks(input) {
    let result = "";
    let position = 0;
    for (let i = 0; i < input.length; i++) {
        if (position === 5) {
            result += " ";
            position = 1;
        }
        else {
            position += 1;
        }
        result += input[i];
    }
    return result;
}
export function encode(plainText) {
    let result = "";
    plainText = sanitizeInput(plainText);
    let plainTextArray = plainText.split("");
    for (let i = 0; i < plainTextArray.length; i++) {
        if (plainTextArray[i].match(new RegExp("[0-9]"))) {
            result += plainTextArray[i];
        }
        else {
            result += cipher[plain.indexOf(plainTextArray[i])];
        }
    }
    return cutToChunks(result);
}
export function decode(cipherText) {
    let result = "";
    cipherText = sanitizeInput(cipherText);
    let cipherTextArray = cipherText.split("");
    for (let i = 0; i < cipherTextArray.length; i++) {
        if (cipherTextArray[i].match(new RegExp("[0-9]"))) {
            result += cipherTextArray[i];
        }
        else {
            result += plain[cipher.indexOf(cipherTextArray[i])];
        }
    }
    return result;
}
