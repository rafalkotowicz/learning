enum ParsingErrors {
  UNKNOWN_OPERATION = "Unknown operation",
  SYNTAX_ERROR = "Syntax error",
}

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
    default:
      throw new Error(ParsingErrors.SYNTAX_ERROR)
  }
}

export const answer = (command: string): number => {
  let result: number = 0;
  let operatorCount: number = 0;
  let sanitizedCommand = sanitize(command);
  let tokens: string[] = sanitizedCommand.split(" ");
  let operation: string = "";

  if (command.substring(0, 7) !== "What is") {
    throw new Error(ParsingErrors.UNKNOWN_OPERATION);
  }
  if (isNaN(Number(tokens[0])) || sanitizedCommand === "") {
    throw new Error(ParsingErrors.SYNTAX_ERROR);
  }


  for (let pos = 0; pos < tokens.length; pos++) {
    let currentToken: string = tokens[pos];
    if (isNaN(Number(currentToken))) {
      operation += currentToken;
    } else {
      if (operation === "" && pos > 0) {
        throw new Error(ParsingErrors.SYNTAX_ERROR);
      }
      result = doOperation(result, parseInt(currentToken), operation);
      operation = "";
      operatorCount += 1;
    }
  }

  if (operation === "cubed") {
    throw new Error(ParsingErrors.UNKNOWN_OPERATION);
  }
  if (operation !== "" || operatorCount === 0) {
    throw new Error(ParsingErrors.SYNTAX_ERROR);
  }

  return result;
}
