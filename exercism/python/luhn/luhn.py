class Luhn:
    card_num: str

    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        number = self.card_num.replace(" ", "")
        number = number.strip()

        if len(number) <= 1:
            return False

        if not number.isdigit():
            return False

        doubled = 0
        parity = 1
        for curr in reversed(number):
            if parity % 2 == 0:
                doubled += int(curr) * 2 if int(curr) * 2 <= 9 else int(curr) * 2 - 9
            else:
                doubled += int(curr)
            parity += 1

        if doubled % 10 == 0:
            return True

        return False
