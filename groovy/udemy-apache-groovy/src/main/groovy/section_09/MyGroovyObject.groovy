package section_09

class MyGroovyObject implements GroovyObject {
    String myProperty

    String invokeMethod(String name, Object args) { return "default method" }

    String getProperty(String propertyName) {
        if (metaClass.hasProperty(this, propertyName)) {
            return "default property manager"
        } else {
            return propertyMissing(propertyName)
        }
    }

    String propertyMissing(String propertyName) {
        return "caught missing property: $propertyName"
    }
}
