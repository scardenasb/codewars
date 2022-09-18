def order_weight(st):
    list_st = sorted(st.split())
    res = sorted(list_st, key=lambda x: sum(int(i) for i in x))

    return ' '.join(res)
