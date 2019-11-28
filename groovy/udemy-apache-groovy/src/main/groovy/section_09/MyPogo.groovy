package section_09

class MyPogo implements GroovyObject {
    String myProperty

    void setProperty(String propertyName, Object value) {
        this.@"$propertyName" = "property overridden during setup: $propertyName"
    }
}
