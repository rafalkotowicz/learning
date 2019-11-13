package section_06

class MyClosure {

    static Closure<Integer> summingClosure = { int a = 0, int b = 0, int c = 0 -> a + b + c }
    static Closure<Boolean> isNumber = { String p -> p.matches("[0-9]*") }
    static Closure printMap = { def key, def value -> return ("$key:= $value") }

    static Closure<BigDecimal> calculatePaintPrice = {
        def areaToPaint,
        def paintEfficiencyFromLiter,
        def paintPricePerLiter ->
            areaToPaint / paintEfficiencyFromLiter * paintPricePerLiter
    }

    static Closure calculatePaintPriceFixedArea = calculatePaintPrice.curry(10.0)
    static Closure calculatePaintPriceFixedPrice = calculatePaintPrice.ncurry(2, 4.0)
}
