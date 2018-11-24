package section_10.challenges;

import java.util.ArrayList;
import java.util.List;

public class League<T extends Team> {
    private List<Team> teams = new ArrayList<>();

    public boolean addTeam(T team) {
        if(teams.contains(team)) {
            return false;
        } else {
            teams.add(team);
            return true;
        }
    }

    public int size() {
        return teams.size();
    }

    public void printStandings() {
        teams.sort(Team::compareTo);
//        Collections.sort(teams);

        for(Team team : teams) {
            System.out.println(team.getName() + " - " + team.getScore());
        }
    }
}
