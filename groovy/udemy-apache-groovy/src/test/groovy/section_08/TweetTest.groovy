package section_08


import org.junit.Test
import section_08.Tweet

import java.time.Instant

class TweetTest {

    @Test
    void authorCanBeSetTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        assert "Rafał Kotowicz" == tweet.author
    }

    @Test
    void dateIsGeneratedTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        assert Instant.now().isAfter(tweet.createdOn.toInstant())
        assert Instant.now().isBefore(tweet.createdOn.toInstant().plusSeconds(10))
    }

    @Test
    void messageCanBeSetTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        tweet.setMessage("Hello World! I decided to learn Groovy too boost my productivity as a Quality Assurance Engineer")
        assert tweet.getMessage() == "Hello World! I decided to learn Groovy too boost my productivity as a Quality Assurance Engineer"
    }

    @Test
    void messageCanBeEmptyTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        tweet.setMessage("")
        assert tweet.getMessage() == ""
    }

    @Test
    void findHashTagsTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        tweet.setMessage("Hello World! I decided to learn Groovy too boost my productivity as a Quality Assurance Engineer (#groovy, #learning)")
        assert ["learning", "groovy"] as HashSet == tweet.findHashTags()
    }

    @Test
    void findMentionsTest() {
        Tweet tweet = new Tweet("Rafał Kotowicz")
        tweet.setMessage("Hi! I just saw @arturczajka and @pawelwlodarki! I even got autographs from both of them!")
        assert ["pawelwlodarki", "arturczajka"] as HashSet == tweet.findMentions()
    }

}
