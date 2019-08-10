package section_03.ast_transformation

import groovy.transform.Field

@Field
List awe = [1, 2, 3]
def awesum() { awe.sum() }
assert awesum() == 9