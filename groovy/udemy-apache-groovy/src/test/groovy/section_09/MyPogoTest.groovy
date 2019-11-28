package section_09

import org.junit.Test

class MyPogoTest {
    @Test
    void overridingPropertySetterTest() {
        MyPogo mp = new MyPogo()
        mp.myProperty = "someValue"
        assert "property overridden during setup: myProperty" == mp.myProperty
    }
}
