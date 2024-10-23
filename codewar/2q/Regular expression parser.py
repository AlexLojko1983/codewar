'''
Your task is to implement a simple regular expression parser. We will have a parser that outputs the following
AST of a regular expression:

Normal(c)           # ^ A character (string) that is not in "()*|."
Any()               # ^ Any character
ZeroOrMore(regexp)  # ^ Zero or more occurances of the same regexp
Or(regexp, regexp)  # ^ A choice between 2 regexps
Str([regexps])      # ^ A sequence of regexps.
As with the usual regular expressions, Any is denoted by the '.' character, ZeroOrMore is denoted by a subsequent '*'
and Or is denoted by '|'. Brackets, ( and ), are allowed to group a sequence of regular expressions into the Str object.
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
from django.db.models.expressions import result


# from preloaded import Any, Normal, Or, Str, ZeroOrMore

# preloaded defines the following:

# class RegExp:
#     def __init__(self, *args):
#         self.args = args
#
#     def __repr__(self):
#         args = ", ".join(map(repr, self.args))
#         return f"{self.__class__.__name__}({args})"
#
#     def __eq__(self, other):
#         return type(self) is type(other) and self.args == other.args


class Any:
    def __repr__(self):
        return 'Any()'


class Normal:
    def __init__(self, c):
        self.c = c

    def __repr__(self):
        return f'Normal({self.c})'


class Or:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Or({repr(self.left)}, {repr(self.right)})'


class Str:
    def __init__(self, RegExp):
        self.RegExp = RegExp

    def __repr__(self):
        return f'Str({repr(self.RegExp)})'


class ZeroOrMore:
    def __init__(self, RegExp):
        self.RegExp = RegExp

    def __repr__(self):
        return f'ZeroOrMore({repr(self.RegExp)})'


def parse_regexp(regexp:str):
    def parse(s:str):
        result = []
        count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                count +=1
                for j in range(i+1, len(s)):
                    if s[j] == '(':
                        count += 1
                    elif s[j] == ')':
                        count -=1
                    if count ==0:
                        result.append(parse(s[i+1:j]))
                        i=j
                        break
            elif s[i] == '.':
                result.append(Any())
            elif s[i] == '*':
                result[-1] = ZeroOrMore(result[-1])
            elif s[i] == '|':
                left = Str(result)
                right = parse(s[i+1:])
                return Or(left,right)
            else:
                result.append(Normal(s[i]))
            i += 1
        return Str(result)

    return parse(regexp)


regexp = '.*(sk)'
print(parse_regexp(regexp))
