export const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];

export function decodedValue(bandsColors: string[]): number {
  let resistance: string = "";
  for (let i = 0; i <= bandsColors.length && i < 2; i++) {
    resistance += "" + COLORS.indexOf(bandsColors[i].toLowerCase());
  }
  return parseInt(resistance);
}
