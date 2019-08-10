package section_03.ast_transformation

import groovy.transform.TailRecursive

class SumMeUp {
    @TailRecursive
    long sumUp (long number, long sum) {
        if (number == 0)  return sum
        sumUp(number -1, sum + number)
    }
}

calc = new SumMeUp()
def out = calc.sumUp(3, 0)
assert out == 7