from preloaded import FILTERS


def is_valid(query: str) -> bool:
    res = query.split()
    filter_name = ""
    for i in res:
        try:
            filter_name = i[0 : i.index(":")]
            if filter_name not in FILTERS:
                return False
            else:
                continue
        except:
            continue
    return True
