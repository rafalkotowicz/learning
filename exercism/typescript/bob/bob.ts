export function hey(message: string): string {
  message = message.trim()
  const lowercase: RegExp = new RegExp("[a-z]", "g")
  const uppercase: RegExp = new RegExp("[A-Z]", "g");
  const anyLetter: RegExp = new RegExp("[a-zA-Z]", "g");
  let sentence: Set<string> = new Set(message);
  let areAllCaps: boolean = true;
  let noLetters: boolean = true;
  for (let c of sentence) {
    if (c.match(lowercase)) {
      areAllCaps = false;
      break;
    }
    if (c.match(anyLetter)) {
      noLetters = false;
    }
  }
  let lastChar: string = message[message.length - 1] ?? "";

  if (lastChar === "?") {
    if (areAllCaps && !noLetters) {
      return "Calm down, I know what I'm doing!";
    } else {
      return "Sure.";
    }
  } else if (areAllCaps && lastChar === "!" || areAllCaps && lastChar.match(uppercase)) {
    return "Whoa, chill out!";
  } else if (message === "") {
    return "Fine. Be that way!";
  }
  return "Whatever."
}
