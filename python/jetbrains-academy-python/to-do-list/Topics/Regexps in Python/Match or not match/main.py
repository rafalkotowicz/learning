import re


def matched(template, string):
    return True if re.match(template, string) else False
