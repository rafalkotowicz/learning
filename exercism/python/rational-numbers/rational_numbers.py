"""Rational number implementation with normalized arithmetic operations."""

from __future__ import annotations

import math


class Rational:
    """Represent a reduced rational number in standard sign form."""

    def __init__(self, numer: int, denom: int) -> None:
        if not denom:
            raise ZeroDivisionError("Denominator cannot be zero.")

        greatest_common_divisor = math.gcd(numer, denom)
        reduced_numer = numer // greatest_common_divisor

        if (reduced_denom := denom // greatest_common_divisor) < 0:
            reduced_numer *= -1
            reduced_denom *= -1

        if not reduced_numer:
            reduced_denom = 1

        self.numer = reduced_numer
        self.denom = reduced_denom

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numer == other.numer and self.denom == other.denom

    def __hash__(self) -> int:
        return hash((self.numer, self.denom))

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: Rational) -> Rational:
        result_numer = self.numer * other.denom + other.numer * self.denom
        result_denom = self.denom * other.denom
        return Rational(result_numer, result_denom)

    def __sub__(self, other: Rational) -> Rational:
        result_numer = self.numer * other.denom - other.numer * self.denom
        result_denom = self.denom * other.denom
        return Rational(result_numer, result_denom)

    def __mul__(self, other: Rational) -> Rational:
        result_numer = self.numer * other.numer
        result_denom = self.denom * other.denom
        return Rational(result_numer, result_denom)

    def __truediv__(self, other: Rational) -> Rational:
        result_numer = self.numer * other.denom
        result_denom = self.denom * other.numer
        return Rational(result_numer, result_denom)

    def __abs__(self) -> Rational:
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power: int) -> Rational:
        if power >= 0:
            return Rational(self.numer**power, self.denom**power)

        absolute_power = abs(power)
        return Rational(self.denom**absolute_power, self.numer**absolute_power)

    def __rpow__(self, base: float) -> float:
        exponent_value = self.numer / self.denom
        return float(base**exponent_value)
