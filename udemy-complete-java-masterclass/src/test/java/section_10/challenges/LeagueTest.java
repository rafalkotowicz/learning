package section_10.challenges;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.*;

public class LeagueTest {
    private ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private PrintStream originalOutput = System.out;

    @Before
    public void catchOutputStream() {
        setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreOutputStream() {
        setOut(originalOutput);
    }

    @Test
    public void addTeamAcceptsOnlyUniqueTeams() {
        Team<BaseballPlayer> baseballTeam = new Team<>();
        League<Team<BaseballPlayer>> baseballLeague = new League();

        assertTrue(baseballLeague.addTeam(baseballTeam));
        assertFalse(baseballLeague.addTeam(baseballTeam));
        assertFalse(baseballLeague.addTeam(baseballTeam));
        assertEquals(1, baseballLeague.size());
    }

    @Test
    public void leagueStandingsArePrintedInOrder() {
        League<Team<BaseballPlayer>> baseballLeague = new League();
        baseballLeague.addTeam(new Team("Team A1", 1));
        baseballLeague.addTeam(new Team("Team A2", 5));
        baseballLeague.addTeam(new Team("Team A3", 23));
        baseballLeague.addTeam(new Team("Team A4", 12));

        final String expectedPrintout =
        "Team A3 - 23\r\n" +
        "Team A4 - 12\r\n" +
        "Team A2 - 5\r\n" +
        "Team A1 - 1\r\n";
        baseballLeague.printStandings();
        assertEquals(expectedPrintout, caughtOutput.toString());
    }
}
