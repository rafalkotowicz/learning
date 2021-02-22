#Requirement:
#Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
#and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzBuzz(value):
    if value % 15 == 0:
        return 'FizzBuzz'
    if value % 3 == 0:
        return 'Fizz'
    if value % 5 == 0:
        return 'Buzz'
    return value

def printer(numbers):
    transformed = list()
    for number in numbers:
        transformed.append(str(fizzBuzz(number)))
    return "".join(transformed)


def test_multiples_of_three():
    expected_value = 'Fizz'
    assert fizzBuzz(3) == expected_value
    assert fizzBuzz(9) == expected_value
    assert fizzBuzz(12) == expected_value
    assert fizzBuzz(21) == expected_value
    assert fizzBuzz(333) == expected_value

def test_multiples_of_five():
    expected_value = 'Buzz'
    assert fizzBuzz(5) == expected_value
    assert fizzBuzz(10) == expected_value
    assert fizzBuzz(25) == expected_value
    assert fizzBuzz(35) == expected_value
    assert fizzBuzz(55555) == expected_value

def test_multiples_of_fifteen():
    expected_value = 'FizzBuzz'
    assert fizzBuzz(15) == expected_value
    assert fizzBuzz(30) == expected_value
    assert fizzBuzz(45) == expected_value
    assert fizzBuzz(60) == expected_value
    assert fizzBuzz(6000) == expected_value

def test_printer5():
    expected_value = "12Fizz4Buzz"
    actual_value = printer([1,2,3,4,5])
    assert actual_value == expected_value

def test_printer100():
    expected_value = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132" \
                     "Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162" \
                     "Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192" \
                     "Fizz94BuzzFizz9798FizzBuzz"
    actual_value = printer(list(range(1,101)))
    assert actual_value == expected_value