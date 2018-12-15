package section_10.challenges;

import org.junit.Test;

import static org.junit.Assert.*;

public class TeamTest {
    @Test
    public void addPlayerShouldAcceptOnlyUniquePlayers() {
        FootballPlayer john = new FootballPlayer("John");
        Team<FootballPlayer> footballTeam = new Team();
        assertTrue(footballTeam.addPlayer(john));
        assertFalse(footballTeam.addPlayer(john));
        assertEquals(1, footballTeam.size());
    }
}
