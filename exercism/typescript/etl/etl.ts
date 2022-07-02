export function transform(input: Legacy) : NextGen {
  let output : NextGen = {};
  for (let key in input) {
    for (let value of input[key]) {
      output[value.toLowerCase()]=parseInt(key);
    }
  }
  return output
}

type Legacy = {
  [key: number]: string[]
}

type NextGen = {
  [key: string]: number
}
