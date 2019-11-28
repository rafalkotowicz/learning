package section_09


import org.junit.Test

class MyGroovyObjectTest {
    @Test
    void invokeMethodTest() {
        MyGroovyObject mgo = new MyGroovyObject()
        assert "default method" == mgo.unexistingMethod()
    }

    @Test
    void getSetPropertyTest() {
        MyGroovyObject mgo = new MyGroovyObject()
        mgo.setMyProperty("someValue")
        assert "default property manager" == mgo.myProperty
    }

    @Test
    void missingPropertyTest() {
        MyGroovyObject mgo = new MyGroovyObject()
        assert "caught missing property: unExistingProperty" == mgo.unExistingProperty
    }
}
