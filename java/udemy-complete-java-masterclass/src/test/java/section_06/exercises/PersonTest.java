package section_06.exercises;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class PersonTest {
    Person person;

    @Before
    public void initializeTestData() {
        person = new Person();
    }

    @Test
    public void extendingAgeBoundariesTest() {
        person.setAge(-1);
        assertEquals(0, person.getAge());
        person.setAge(101);
        assertEquals(0, person.getAge());
    }

    @Test
    public void settingAgeWithinBoundariesTest() {
        person.setAge(40);
        assertEquals(40, person.getAge());
    }

    @Test
    public void checkIfTeenTest() {
        person.setAge(13);
        assertTrue(person.isTeen());
        person.setAge(20);
        assertFalse(person.isTeen());
    }

    @Test
    public void getFullNameTest() {
        person.setFirstName("Jurek");
        assertEquals("Jurek", person.getFullName());
        person.setLastName("Kowalewski");
        assertEquals("Jurek Kowalewski", person.getFullName());
        person.setFirstName("");
        assertEquals("Kowalewski", person.getFullName());
    }

}
