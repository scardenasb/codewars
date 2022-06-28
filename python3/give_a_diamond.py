# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James.
# Since James doesn't know how to make this happen, he needs your help.
#
# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*)
# characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#
# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond
# of even or negative size.
#
# Examples
# A size 3 diamond:
#
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"
#
# A size 5 diamond:
#
#   *
#  ***
# *****
#  ***
#   *
# ...that is:
#
# "  *\n ***\n*****\n ***\n  *\n"


def diamond(n):
    res = []
    space = 0
    if n % 2 != 0 and n > 0:
        for i in range(0, n, 2):
            res.extend([" " * (n // 2 - space) + "*" * (i + 1) + "\n"])
            space += 1
        res.extend(list(res[-2::-1]))
    else:
        return None
    return "".join(res)
