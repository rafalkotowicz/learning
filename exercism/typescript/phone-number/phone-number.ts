export function clean(dirtyNumber: string): string {
  let cleanedNumber = dirtyNumber.replaceAll(new RegExp("[-\.\ \(\)\+]", "g"), "");

  if (cleanedNumber.match(new RegExp("[a-zA-Z]", "g"))) {
    throw new Error('Letters not permitted');
  }
  if (cleanedNumber.match(new RegExp("[@:!]", "g"))) {
    throw new Error('Punctuations not permitted');
  }


  if (cleanedNumber.length < 10) {
    throw new Error('Incorrect number of digits');
  }

  if (cleanedNumber.length === 11) {
    if (cleanedNumber[0] === "1") {
      cleanedNumber = cleanedNumber.substring(1);
    } else {
      throw new Error('11 digits must start with 1');
    }
  }

  if (cleanedNumber.length === 10) {
    if (cleanedNumber[0] === "0") {
      throw new Error('Area code cannot start with zero');
    } else if (cleanedNumber[0] === "1") {
      throw new Error('Area code cannot start with one');
    }
    if (cleanedNumber[3] === "0") {
      throw new Error('Exchange code cannot start with zero');
    } else if (cleanedNumber[3] === "1") {
      throw new Error('Exchange code cannot start with one');
    }
    return cleanedNumber;
  } else {
    throw new Error('More than 11 digits');
  }
}
