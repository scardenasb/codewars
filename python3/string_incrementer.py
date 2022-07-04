# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.


import re


def increment_string(strng):
    num = ""
    zeros = ""
    if re.findall("[\d]", strng) != []:
        for i in strng[::-1]:
            if i.isdigit() != False:
                num += "".join(i)
                continue
            else:
                break
        num = "".join(list(reversed(num)))
        if num[0] != "0":
            strng = strng.replace(num, str(int(num) + 1))
            return strng
        else:
            zeros = "".join(filter(lambda x: x == "0", num))
            strng = strng.replace(
                num, "0" * (len(num) - len(str(int(num) + 1))) + str(int(num) + 1)
            )
            return strng
    else:
        return strng + "1"
