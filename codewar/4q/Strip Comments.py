'''Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

import re


def strip_comments(strng: str, markers: list):
    escaped_markers = [re.escape(marker) for marker in markers]
    markers = '|'.join(escaped_markers)
    strng = strng.split('\n')
    trimmed_lines = [re.split(markers, line)[0].rstrip() if markers else line for line in strng]
    return '\n'.join(trimmed_lines)


print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))
