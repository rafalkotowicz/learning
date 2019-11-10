package playground

import org.junit.Assert
import org.junit.Test

class HelloWorldTest {
    @Test
    public void helloWorldShouldReturnProvidedNameTest() {
        HellowWorld helloWorld = new HellowWorld()
        Assert.assertEquals("Hello, Rafał!", helloWorld.hello("Rafał"))
        assert "Hello, Rafał!" == helloWorld.hello("Rafał")
    }

    @Test
    public void helloWorldShouldHandleEmptyNameTest() {
        HellowWorld helloWorld = new HellowWorld()
        assert "Hello, !" == helloWorld.hello("")
    }
}
