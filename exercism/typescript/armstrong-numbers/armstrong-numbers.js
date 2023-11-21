export function isArmstrongNumber(number) {
    const bigIntNumber = BigInt(number);
    const digits = Array.from(bigIntNumber.toString(), (char) => BigInt(parseInt(char)));
    const digitsRaised = digits.map((e) => BigInt(e ** BigInt(digits.length)));
    const sum = digitsRaised.reduce((accumulator, currentValue) => accumulator + currentValue);
    return bigIntNumber === sum;
}
