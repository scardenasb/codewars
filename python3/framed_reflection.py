# 100th Kata
# You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see,
# complete with the mirror frame. Example:
#
# 'Hello World'
#
# would give:
#
#
# Words in your solution should be left-aligned.


def mirror(text):
    text = text.split()
    maxim = len(max(text, key=len)) + 4
    mirror = ""
    for x in text:
        mirror += "* " + x[::-1] + " " * (maxim - 4 - len(x)) + " *\n"
    return "*" * maxim + "\n" + mirror + "*" * maxim
