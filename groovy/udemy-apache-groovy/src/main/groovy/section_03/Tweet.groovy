package section_03

import groovy.transform.ToString

@ToString
class Tweet {
    String owner
    def text
    Date postedDate
    int reputation
    int retweets
}