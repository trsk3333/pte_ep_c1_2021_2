def get_afa(termek_ara: int, afa=27) -> float:
    """
    Kiszámolja a termék után fizetendő ÁFA mértékét.
    :param termek_ara: A termék ára forintban.
    :param afa: Az áfa kulcs %-ban.
    :return: A termék után fizetendő ÁFA mértéke.
    """
    return termek_ara * afa / 100


def brutto(termek_ara: int, afa=27) -> float:
    return termek_ara + get_afa(termek_ara, afa)


ar = 10000
print(get_afa(ar))
print(brutto(ar))
