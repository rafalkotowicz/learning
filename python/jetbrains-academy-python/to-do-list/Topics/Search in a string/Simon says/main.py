SIMON_SAYS = "Simon says"


def what_to_do(instructions):
    if instructions.startswith(SIMON_SAYS):
        return "I " + instructions[len(SIMON_SAYS) + 1:]
    elif instructions.endswith(SIMON_SAYS):
        return "I " + instructions[:len(SIMON_SAYS) + 1]
    else:
        return "I won't do it!"


# def what_to_do(instructions):
#     if SIMON_SAYS not in instructions:
#         return "I won't do it!"
#     else:
#         return "I " + instructions.replace("Simon says", "").strip()

# what_to_do("make a wish Simon says")
# what_to_do("Simon says make a wish")
# what_to_do("go away")
