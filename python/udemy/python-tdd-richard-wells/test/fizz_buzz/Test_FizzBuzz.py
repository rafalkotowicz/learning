# Requirement:
# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
from src.fizz_buzz.FizzBuzz import fizz_buzz, printer


def test_multiples_of_three():
    expected_value = 'Fizz'
    assert fizz_buzz(3) == expected_value
    assert fizz_buzz(9) == expected_value
    assert fizz_buzz(12) == expected_value
    assert fizz_buzz(21) == expected_value
    assert fizz_buzz(333) == expected_value


def test_multiples_of_five():
    expected_value = 'Buzz'
    assert fizz_buzz(5) == expected_value
    assert fizz_buzz(10) == expected_value
    assert fizz_buzz(25) == expected_value
    assert fizz_buzz(35) == expected_value
    assert fizz_buzz(55555) == expected_value


def test_multiples_of_fifteen():
    expected_value = 'FizzBuzz'
    assert fizz_buzz(15) == expected_value
    assert fizz_buzz(30) == expected_value
    assert fizz_buzz(45) == expected_value
    assert fizz_buzz(60) == expected_value
    assert fizz_buzz(6000) == expected_value


def test_printer5():
    expected_value = "12Fizz4Buzz"
    actual_value = printer([1, 2, 3, 4, 5])
    assert actual_value == expected_value


def test_printer100():
    expected_value = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132" \
                     "Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859" \
                     "FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86" \
                     "Fizz8889FizzBuzz9192Fizz94BuzzFizz9798FizzBuzz"
    actual_value = printer(list(range(1, 101)))
    assert actual_value == expected_value
