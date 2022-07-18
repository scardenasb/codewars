# Build Tower
# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]


def tower_builder(n):
    res = []
    spaces = n - 1
    for i in range(1, n * 2, 2):
        res.append(" " * spaces + "*" * i + " " * spaces)
        spaces -= 1
    return res
