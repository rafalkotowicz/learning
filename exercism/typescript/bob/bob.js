export function hey(message) {
    message = message.trim();
    const lowercase = new RegExp("[a-z]", "g");
    const uppercase = new RegExp("[A-Z]", "g");
    const anyLetter = new RegExp("[a-zA-Z]", "g");
    let sentence = new Set(message);
    let areAllCaps = true;
    let noLetters = true;
    for (let c of sentence) {
        if (c.match(lowercase)) {
            areAllCaps = false;
            break;
        }
        if (c.match(anyLetter)) {
            noLetters = false;
        }
    }
    let lastChar = message[message.length - 1] ?? "";
    if (lastChar === "?") {
        if (areAllCaps && !noLetters) {
            return "Calm down, I know what I'm doing!";
        }
        else {
            return "Sure.";
        }
    }
    else if (areAllCaps && lastChar === "!" || areAllCaps && lastChar.match(uppercase)) {
        return "Whoa, chill out!";
    }
    else if (message === "") {
        return "Fine. Be that way!";
    }
    return "Whatever.";
}
