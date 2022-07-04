export function convert(num: number): string {
  let result: string = ""

  if (num % 3 === 0) {
    result += "Pling";
  }
  if (num % 5 === 0) {
    result += "Plang";
  }
  if (num % 7 === 0) {
    result += "Plong";
  }
  if (result === "") {
    return "" + num;
  }

  return result;
}
