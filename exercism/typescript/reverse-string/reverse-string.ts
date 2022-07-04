export function reverse(input: string): string {
  if (input === "") {
    return ""
  }
  return input.split("").reverse().reduce((x, y) => x + y);
}
