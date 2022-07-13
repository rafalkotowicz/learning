function sanitize(command: string) {
  let removeBegining: string = command.replaceAll(new RegExp("What is", "g"), "").trim();
  let removeQuestionMark: string = removeBegining.replaceAll(new RegExp("[?]", "g"), "");
  return removeQuestionMark;
}

export function doOperation(accumulator: number, num: number, operation: string) {
  switch (operation) {
    case "":
      return num;
    case "plus":
      return accumulator + num;
    case "minus":
      return accumulator - num;
    case "multipliedby":
      return accumulator * num;
    case "dividedby":
      return accumulator / num;
  }
  return accumulator;
}

export const answer = (command: string): number => {
  let result: number = 0;
  command = sanitize(command);
  let tokens: string[] = command.split(" ");

  let operation: string = "";

  for (let pos = 0; pos < tokens.length; pos++) {
    let currentToken: string = tokens[pos];
    if (isNaN(Number(currentToken))) {
      operation += currentToken;
    } else {
      result = doOperation(result, parseInt(currentToken), operation);
      operation = "";
    }
  }

  if(operation === "plus") {
    throw new Error('Syntax error');
  }

  if(operation !== "") {
    throw new Error('Unknown operation');
  }

  return result;
}
