from functools import reduce


def order_weight(st):
    list_st = sorted(st.split())
    res = []
    minimus = list(
        map(lambda x: reduce(lambda i, j: int(i) + int(j), x), list_st)
    )
    minimus = list(map(int, minimus))

    for i in range(len(list_st)):
        list_mini = list_st[minimus.index(min(minimus))]
        res.append(list_mini)
        list_st.remove(list_mini)
        minimus.remove(min(minimus))

    return ' '.join(res)
