def cut_out_prefix_and_by_suffix(question: str) -> str:
    expected_prefix: str = 'What is'
    if question[:len(expected_prefix)] != expected_prefix:
        raise ValueError("unknown operation")
    return question[len(expected_prefix) + 1:].replace('?', '').replace('by', '')


def calculate(result: int, operation: str, number: int) -> int:
    if operation == 'plus':
        return result + number
    elif operation == 'minus':
        return result - number
    elif operation == 'divided':
        return result / number
    elif operation == 'multiplied':
        return result * number
    else:
        raise ValueError("unknown operation")


def answer(question: str) -> int:
    question = cut_out_prefix_and_by_suffix(question)
    question_chunked: [str] = question.split()

    if (len(question_chunked)) < 1:
        raise ValueError("syntax error")

    if question_chunked[0].lstrip('-').isdigit():
        result = int(question_chunked.pop(0))
    else:
        raise ValueError("syntax error")

    operation: str = None
    number: int = None
    for chunk in question_chunked:
        if operation is None:
            if chunk in ['plus', 'minus', 'divided', 'multiplied']:
                operation = chunk
                continue
            else:
                if chunk.lstrip('-').isdigit():
                    raise ValueError("syntax error")
                else:
                    raise ValueError("unknown operation")
        if number is None:
            if chunk.lstrip('-').isdigit():
                number = int(chunk)

        if number and operation:
            result = calculate(result, operation, number)
            operation = None
            number = None
        else:
            raise ValueError("syntax error")

    if operation or number:
        raise ValueError("syntax error")

    return result
