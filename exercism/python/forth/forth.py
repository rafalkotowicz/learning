import math
import re


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def tokenize(input_data: str) -> list:
    tokenized: list = []

    tokens: [str] = input_data.split()
    for token in tokens:
        if re.findall('[-+]?\d+', token):
            tokenized.append(int(token))
        else:
            tokenized.append(token)
    return tokenized


def evaluate(input_data: list) -> list:
    user_defined: list = dict()
    evaluated: list = list()

    for expression in input_data:
        expression = expression.lower()
        # defining new words
        if expression[0] == ":" and expression[-1] == ";":
            expression = expression[2:-2]
            tokenized_user = str(expression).split(maxsplit=1)
            if re.findall('[-+]?\d+', tokenized_user[0]):
                raise ValueError("illegal operation")
            else:
                for user_word in user_defined:
                    found_user_word = re.findall(user_word, tokenized_user[1])
                    if found_user_word:
                        if found_user_word == tokenized_user[1]:
                            user_defined[tokenized_user[0]] = user_defined[tokenized_user[1]]
                        else:
                            tokenized_user[1] = tokenized_user[1].replace(found_user_word[0],
                                                                          str(user_defined[user_word]))
                            user_defined[user_word] = tokenized_user[1]
                        break
                user_defined[tokenized_user[0]] = tokenized_user[1]
        # evaluation
        else:
            tokenized: list = tokenize(expression)
            # substitute words with values
            after_substitution: list = list()
            for token in tokenized:
                if token in user_defined:
                    if str(user_defined[token].split()).find(" ") != -1:
                        after_substitution.extend(user_defined[token].split())
                    else:
                        after_substitution.append(user_defined[token])
                else:
                    after_substitution.append(token)

            for token in after_substitution:
                index = after_substitution.index(token)
                if re.findall('[-+]?\d+', str(token)):
                    evaluated.append(int(token))
                elif token == "+":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        addend: int = evaluated.pop()
                        augend: int = evaluated.pop()
                        evaluated.append(augend + addend)
                elif token == "-":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        substrahend: int = evaluated.pop()
                        minuend: int = evaluated.pop()
                        evaluated.append(minuend - substrahend)
                elif token == "*":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        multiplicand: int = evaluated.pop()
                        multiplier: int = evaluated.pop()
                        evaluated.append(multiplier * multiplicand)
                elif token == "/":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        denominaotr: int = evaluated.pop()
                        numerator: int = evaluated.pop()
                        if denominaotr == 0:
                            raise ZeroDivisionError("divide by zero")
                        evaluated.append(math.floor(numerator / denominaotr))
                elif str(token).casefold() == "dup":
                    if index < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        evaluated.append(evaluated[-1])
                elif str(token).casefold() == "drop":
                    if index < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        evaluated.pop()
                elif str(token).casefold() == "swap":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        last: int = evaluated.pop()
                        next_to_last: int = evaluated.pop()
                        evaluated.append(last)
                        evaluated.append(next_to_last)
                elif str(token).casefold() == "over":
                    if index < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    else:
                        evaluated.append(evaluated[-2])
                else:
                    raise ValueError("undefined operation")

    return evaluated
