if __name__ == '__main__':
    amount = 83
    feet = 240

    """
    假設雞兔都是兩隻腳
    83 * 2 = 166
    240 - 166 = 74
    rabbit = 74 / 2
    """

    if amount * 2 <= feet <= amount * 4:
        rabbit: float = (feet - amount * 2) / (4 - 2)
        chicken = amount - rabbit
        print('rabbit:', rabbit, 'chicken:', chicken)
    else:
        print('amount:', amount, 'feet:', feet, 'setting wrong')