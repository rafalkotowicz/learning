var ParsingErrors;
(function (ParsingErrors) {
    ParsingErrors["UNKNOWN_OPERATION"] = "Unknown operation";
    ParsingErrors["SYNTAX_ERROR"] = "Syntax error";
})(ParsingErrors || (ParsingErrors = {}));
function sanitize(command) {
    let removeBegining = command.replaceAll(new RegExp("What is", "g"), "").trim();
    let removeQuestionMark = removeBegining.replaceAll(new RegExp("[?]", "g"), "");
    return removeQuestionMark;
}
export function doOperation(accumulator, num, operation) {
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
            throw new Error(ParsingErrors.SYNTAX_ERROR);
    }
}
export const answer = (command) => {
    let result = 0;
    let operatorCount = 0;
    let sanitizedCommand = sanitize(command);
    let tokens = sanitizedCommand.split(" ");
    let operation = "";
    if (command.substring(0, 7) !== "What is") {
        throw new Error(ParsingErrors.UNKNOWN_OPERATION);
    }
    if (isNaN(Number(tokens[0])) || sanitizedCommand === "") {
        throw new Error(ParsingErrors.SYNTAX_ERROR);
    }
    for (let pos = 0; pos < tokens.length; pos++) {
        let currentToken = tokens[pos];
        if (isNaN(Number(currentToken))) {
            operation += currentToken;
        }
        else {
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
};
