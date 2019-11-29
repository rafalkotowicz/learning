package section_09

import org.junit.Test

class IntegerCategory {
    static Integer timesTwo(Integer integer) { integer * 2 }
}

class CategoryTest {
    @Test
    void categoryTest() {
        use(IntegerCategory) {
            assert 26 == 13.timesTwo()
        }
    }
}
