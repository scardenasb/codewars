# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
#
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"


def what_century(y):
    suffixes = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]
    year = (int(y) - 1) // 100 + 1
    if year in [11, 12, 13]:
        return f"{year}th"
    else:
        return f"{year}{suffixes[int(str(year)[-1])]}"
