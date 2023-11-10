class PhoneNumber:
    def __init__(self, number: str):
        number = self.sanitize_number(number)
        number = self.validate_phone_number_phase1(number)
        self.number = number
        self.area_code: str = number[:3]
        self.exchange_code: str = number[3:6]
        self.subscriber_number: str = number[6:]
        self.validate_phone_number_codes()

    @staticmethod
    def sanitize_number(number: str) -> str:
        translation_table = str.maketrans("", "", " .+-()")
        number = number.translate(translation_table)
        return number

    @staticmethod
    def validate_phone_number_phase1(number: str) -> str:
        min_length = 10
        max_length = 11
        icc = "1"  # international country code
        if len(number) < min_length:
            raise ValueError(f"must not be fewer than {min_length} digits")
        if len(number) > max_length:
            raise ValueError(f"must not be greater than {max_length} digits")
        if len(number) == max_length:
            if not number.startswith(icc):
                raise ValueError(f"{max_length} digits must start with {icc}")
            else:
                number = number[1:]
        if not number.isdigit():
            if any(char in ["@", ":", "!", "?", ","] for char in number):
                raise ValueError("punctuations not permitted")
            else:
                raise ValueError("letters not permitted")
        return number

    def validate_phone_number_codes(self) -> None:
        if self.exchange_code.startswith("0"):
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code.startswith("1"):
            raise ValueError("exchange code cannot start with one")
        if self.area_code.startswith("0"):
            raise ValueError("area code cannot start with zero")
        if self.area_code.startswith("1"):
            raise ValueError("area code cannot start with one")

    def pretty(self) -> str:
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
