# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all
# the even-indexed characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.
#
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.


def decrypt(en_text, n):
    if en_text != "" and n > 0:
        c = 0
        while c < n:
            en_text = list(en_text)
            res = ""
            dic = {
                "odd": en_text[0 : int(len(en_text) / 2)],
                "even": en_text[int(len(en_text) / 2) :],
            }
            for j in range(int(len(en_text) / 2)):
                res += dic["even"][j]
                res += dic["odd"][j]
            c += 1
            if len(en_text) % 2 == 0:
                en_text = res
            else:
                en_text = res + dic["even"][-1]
        return en_text
    else:
        return en_text


def encrypt(text, n):
    c = 0
    while c < n:
        text = list(text)
        dic = {"odd": "", "even": ""}
        for i in range(1, len(text), 2):
            dic["odd"] += text[i]
            dic["even"] += text[i - 1]
        c += 1
        if len(text) % 2 == 0:
            text = dic["odd"] + dic["even"]
        else:
            text = dic["odd"] + dic["even"] + text[-1]
    return text
