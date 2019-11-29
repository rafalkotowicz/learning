package section_09

import org.junit.Test

class MyExpando {
    String prop1

    static String foo() { "foo" }
}

class ExpandoTest {
    @Test
    void myExpandoTest() {
        MyExpando me = new MyExpando()
        assert "foo" == me.foo()
        assert me.metaClass.hasProperty(this, "prop1")
    }

    @Test
    void addingMethodsDynamicallyTest() {
        MyExpando me = new MyExpando()
        assert 17 == me.metaClass.getMethods().size()
        me.metaClass.bar = { -> "bar" }
        assert 18 == me.metaClass.getMethods().size()
        assert "bar" == me.bar()
    }

    @Test
    void addingPropertiesDynamicallyTest() {
        MyExpando me = new MyExpando()
        assert 2 == me.metaClass.properties.size()
        me.metaClass.prop2 = "bar2"
        assert 3 == me.metaClass.properties.size()
        assert "bar2" == me.prop2
    }
}
