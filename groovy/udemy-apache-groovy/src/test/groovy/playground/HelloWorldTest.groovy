package playground

import org.junit.Assert
import org.junit.Test

class HelloWorldTest {
    @Test
    public void helloWorldShouldReturnOurName() {
        HellowWorld helloWorld = new HellowWorld();
        Assert.assertEquals("Hello, Rafał!", helloWorld.hello("Rafał"));
    }
}
