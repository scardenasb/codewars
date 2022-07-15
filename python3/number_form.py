# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    max_zeros = len(str(num))
    res = ""
    for i in range(max_zeros, 0, -1):
        if int(str(num)[-i]) > 0:
            res += str(num)[-i] + "0" * (i - 1) + " + "
    return res[:-3]
