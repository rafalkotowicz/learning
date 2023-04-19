import re


def is_paired(input_string):
    only_brackets: [str] = list(re.sub(r"[^\[\]\{\}\(\)]", "", input_string))
    result: [str] = []

    for element in only_brackets:
        if element == "[":
            result.append("[")
        elif element == "{":
            result.append("{")
        elif element == "(":
            result.append("(")
        elif len(result) == 0:
            return False
        elif element == "]":
            if result[-1] == "[":
                result.pop()
            else:
                result.append("[")
        elif element == "}":
            if result[-1] == "{":
                result.pop()
            else:
                result.append("{")
        elif element == ")":
            if result[-1] == "(":
                result.pop()
            else:
                result.append("(")

    return len(result) == 0
