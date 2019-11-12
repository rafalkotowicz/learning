package section_06

class MyClosure {

    static Closure<Integer> summingClosure = { int a, int b, int c -> a + b + c }
    static Closure<Boolean> isDigit = { String p -> p.matches("[0-9]*") }
}
