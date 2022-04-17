import math


class ComplexNumber:

    def __init__(self, real: float = 0.0, imaginary: float = 0.0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        self.real = self.real + other.real
        self.imaginary = self.imaginary + other.imaginary
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            return ComplexNumber(other) + self
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        a = self.real
        b = self.imaginary
        self.real = a * other.real - b * other.imaginary
        self.imaginary = b * other.real + a * other.imaginary
        return self

    def __rmul__(self, other):
        if isinstance(other, int):
            return ComplexNumber(other) * self
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.real -= other
            return self
        self.real = self.real - other.real
        self.imaginary = self.imaginary - other.imaginary
        return self

    def __rsub__(self, other):
        if isinstance(other, int):
            return ComplexNumber(other) - self
        return self

    def __truediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        self.real = (a * c + b * d) / (c ** 2 + d ** 2)
        self.imaginary = (b * c - a * d) / (c ** 2 + d ** 2)
        return self

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return ComplexNumber(other) / self
        return self

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        self.imaginary = -self.imaginary
        return self

    def exp(self):
        return ComplexNumber(math.e ** self.real * (math.cos(self.imaginary) + math.sin(self.imaginary)))

    def __str__(self):
        sign = "+" if self.imaginary > 0 else "-"
        return f"{self.real} {sign} {self.imaginary}*i"
