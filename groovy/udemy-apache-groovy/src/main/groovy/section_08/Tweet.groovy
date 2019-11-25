package section_08

import groovy.transform.Canonical

import java.time.Instant

@Canonical
class Tweet {
    String author
    Date createdOn
    String message

    Tweet(String author) {
        this.author = author
        createdOn = Date.from(Instant.now())
    }

    HashSet<String> findHashTags() {
        extractStringsAfterGivenCharacter("#")
    }

    HashSet<String> findMentions() {
        extractStringsAfterGivenCharacter("@")
    }

    private HashSet<String> extractStringsAfterGivenCharacter(String character) {
        new HashSet<String>(message.findAll(character + "[a-z]*").collect({ s -> s.substring(1, s.length()) }))
    }
}
