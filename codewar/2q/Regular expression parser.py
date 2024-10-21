'''
Your task is to implement a simple regular expression parser. We will have a parser that outputs the following AST of a regular expression:

Normal(c)           # ^ A character (string) that is not in "()*|."
Any()               # ^ Any character
ZeroOrMore(regexp)  # ^ Zero or more occurances of the same regexp
Or(regexp, regexp)  # ^ A choice between 2 regexps
Str([regexps])      # ^ A sequence of regexps.
As with the usual regular expressions, Any is denoted by the '.' character, ZeroOrMore is denoted by a subsequent '*' and Or is denoted by '|'. Brackets, ( and ), are allowed to group a sequence of regular expressions into the Str object.

Or is not associative, so "a|(a|a)" and "(a|a)|a" are both valid regular expressions, whereas "a|a|a" is not.

Operator precedences from highest to lowest are: *, sequencing and |. Therefore the followings hold:

"ab*"     -> Str([Normal ('a'), ZeroOrMore(Normal('b'))])
"(ab)*"   -> ZeroOrMore(Str([Normal('a'), Normal('b')]))
"ab|a"    -> Or(Str([Normal('a'), Normal('b')]), Normal('a'))
"a(b|a)"  -> Str([Normal('a'), Or(Normal('b'), Normal('a'))])
"a|b*"    -> Or(Normal('a'), ZeroOrMore(Normal('b')))
"(a|b)*"  -> ZeroOrMore(Or(Normal('a'), Normal('b')))
Some examples:

"a"          -> Normal('a')
"ab"         -> Str([Normal('a'), Normal('b')])
"a.*"        -> Str([Normal('a'), ZeroOrMore(Any())])
"(a.*)|(bb)" -> Or(Str([Normal('a'), ZeroOrMore(Any())]), Str([Normal('b'), Normal('b')]))
The followings are invalid regexps and the parser should return Nothing in Haskell / 0 in C or C++ / null in JavaScript or C# / None in Python or Rust / new Void() in Java/Void() in Kotlin:

"", ")(", "*", "a(", "()", "a**", etc.

Feel free to use any parser combinator libraries available on codewars, or implement the parser "from scratch".


'''

# from preloaded import Any, Normal, Or, Str, ZeroOrMore

# preloaded defines the following:

class RegExp:
    def __init__(self, *args):
        self.args = args
    def __repr__(self):
        args = ", ".join(map(repr, self.args))
        return f"{self.__class__.__name__}({args})"
    def __eq__(self, other):
        return type(self) is type(other) and self.args == other.args
class Any(RegExp): pass
class Normal(RegExp):
    pass
class Or(RegExp): pass
class Str(RegExp): pass
class ZeroOrMore(RegExp): pass

# Your task is to build an AST using those nodes.
# See sample tests or test output for examples of usage.

def parse_regexp(indata):
    return Str([Normal('H'), Normal('e'), Normal('l'), Normal('l'), Normal('o')])