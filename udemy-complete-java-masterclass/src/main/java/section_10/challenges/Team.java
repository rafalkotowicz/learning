package section_10.challenges;

import java.util.ArrayList;
import java.util.List;

public class Team<T extends Player> implements Comparable<Team<T>> {
    private String name;
    private int score;
    private List<Player> players = new ArrayList<>();

    public Team(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public Team(String name) {
        new Team(name, 0);
    }

    public Team() {
        new Team("RandomTeam-"+ System.nanoTime(), (int)(System.nanoTime() % 100));
    }

    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    public int size() {
        return players.size();
    }

    public boolean addPlayer(T player) {
        if(players.contains(player)) {
            return false;
        } else {
            players.add(player);
            return true;
        }
    }

    @Override
    public int compareTo(Team<T> otherTeam) {
        if (this.score < otherTeam.score) {
            return 1;
        } else if (this.score > otherTeam.score) {
            return -1;
        } else {
            return 0;
        }
    }
}
