export const toRoman = (decimal) => {
    //pos:10^0  10^1  10^2  10^3
    //1   I     X     C     M
    //2   II    XX    CC    MM
    //3   III   XXX   CCC   MMM
    //4   IV    XL    CD
    //5   V     L     D
    //6   VI    LX    DC
    //7   VII   LXX   DCC
    //8   VIII  LXXX  DCCC
    //9   IX    XC    CM
    let positionalMap = new Map([
        [0, "I"],
        [0.5, "V"],
        [1, "X"],
        [1.5, "L"],
        [2, "C"],
        [2.5, "D"],
        [3, "M"]
    ]);
    let result = "";
    let digits = ("" + decimal).split("").map(x => parseInt(x));
    let positionLow = digits.length - 1;
    let positionHigh = positionLow + 0.5;
    for (let digit of digits) {
        switch (digit) {
            case 0:
                break;
            case 1:
                result += positionalMap.get(positionLow);
                break;
            case 2:
                result += positionalMap.get(positionLow).repeat(2);
                break;
            case 3:
                result += positionalMap.get(positionLow).repeat(3);
                break;
            case 4:
                result += positionalMap.get(positionLow) + positionalMap.get(positionHigh);
                break;
            case 5:
                result += positionalMap.get(positionHigh);
                break;
            case 6:
                result += positionalMap.get(positionHigh) + positionalMap.get(positionLow);
                break;
            case 7:
                result += positionalMap.get(positionHigh) + positionalMap.get(positionLow).repeat(2);
                break;
            case 8:
                result += positionalMap.get(positionHigh) + positionalMap.get(positionLow).repeat(3);
                break;
            case 9:
                result += positionalMap.get(positionLow) + positionalMap.get(positionLow + 1);
                break;
        }
        positionLow -= 1;
        positionHigh -= 1;
    }
    return result;
};
