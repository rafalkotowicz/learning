package section_03.first_class

import groovy.transform.ToString

import java.time.Instant

@ToString
class Tweet1 {
    String owner
    def text
    Date postedDate
    int reputation
    int retweets
}

def tweet1 = new Tweet1(owner: "Rafał Kotowicz", text: "I have started learning Groovy and it is awesome", postedDate: Date.from(Instant.now()), reputation: -10, retweets: 0)
println(tweet1)
def tweet2 = new Tweet(owner: "Rafał Kotowicz", text: "Groovy is awesome, but it is time to sleep...", postedDate: Date.from(Instant.now()), reputation: -10, retweets: 0)
println(tweet2)