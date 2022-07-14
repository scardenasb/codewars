# The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")" if that character appears more than
# once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


def duplicate_encode(word):
    new_str = ""
    word = word.lower()
    for _, v in enumerate(word):
        if word.count(v) > 1:
            new_str += "".join(")")
        else:
            new_str += "".join("(")
    return new_str
