export const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];
export function decodedResistorValue(bandsColors) {
    let resistance = "";
    for (let i = 0; i <= bandsColors.length && i < 2; i++) {
        resistance += "" + COLORS.indexOf(bandsColors[i].toLowerCase());
    }
    let zeros = "";
    if (bandsColors[2] !== null) {
        for (let i = 0; i < COLORS.indexOf(bandsColors[2].toLowerCase()); i++) {
            zeros += "0";
        }
    }
    let resistanceValue = parseInt(resistance + zeros);
    let unit;
    if (resistanceValue % 1000 === 0) {
        resistanceValue /= 1000;
        unit = "kiloohms";
    }
    else {
        unit = "ohms";
    }
    return resistanceValue + " " + unit;
}
