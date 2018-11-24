package section_10.challenges;

import org.junit.Assert;
import org.junit.Test;

public class TeamTest {
    @Test
    public void addPlayerShouldAcceptOnlyUniquePlayers() {
        FootballPlayer john = new FootballPlayer("John");
        Team<FootballPlayer> footballTeam = new Team();
        Assert.assertTrue(footballTeam.addPlayer(john));
        Assert.assertFalse(footballTeam.addPlayer(john));
        Assert.assertEquals(1, footballTeam.size());
    }
}
