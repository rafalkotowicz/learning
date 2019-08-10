package section_03.first_class

import groovy.transform.ToString

@ToString
class Tweet {
    String owner
    def text
    Date postedDate
    int reputation
    int retweets
}