def berKiszamitas(oraszam: int) -> int:
    ber: int = None
    if (oraszam<=40):
        ber = oraszam * 1000
    else:
        oraszam = oraszam - 40
        ber = oraszam*1500 + 40000

    return ber