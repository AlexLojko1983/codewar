'''Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


def strip_comments(strng: str, markers: list):
    should = ""
    # qwe = ''.join(strng.split(" ")).split("\n")
    qwe = strng.split("\n")
    print(qwe)
    for i in qwe:
        if i in markers:
            should += i[:i.find('#')] + "\n"
    return should
print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))