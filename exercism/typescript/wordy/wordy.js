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
    }
    return accumulator;
}
export const answer = (command) => {
    let result = 0;
    command = sanitize(command);
    let tokens = command.split(" ");
    let operation = "";
    for (let pos = 0; pos < tokens.length; pos++) {
        let currentToken = tokens[pos];
        if (isNaN(Number(currentToken))) {
            operation += currentToken;
        }
        else {
            result = doOperation(result, parseInt(currentToken), operation);
            operation = "";
        }
    }
    if (operation === "plus") {
        throw new Error('Syntax error');
    }
    if (operation !== "") {
        throw new Error('Unknown operation');
    }
    return result;
};
