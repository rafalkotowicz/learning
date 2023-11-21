export function isArmstrongNumber(number: number | bigint): boolean {
    const bigIntNumber = BigInt(number);
    const digits: bigint[] = Array.from(bigIntNumber.toString(), (char) => BigInt(parseInt(char)));
    const digitsRaised: bigint[] = digits.map((e) => BigInt(e ** BigInt(digits.length)));
    const sum: bigint = digitsRaised.reduce((accumulator: bigint, currentValue: bigint) => accumulator + currentValue);

    return bigIntNumber === sum;
}
