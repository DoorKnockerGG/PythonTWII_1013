import math

if __name__ == '__main__':
    ticket = 1000
    amount = 1
    buy = 10 * amount * ticket
    fee_buy = 20 if buy * 0.001425 < 20 else math.floor(buy * 0.001425)

    sell = 10.1 * amount * ticket
    fee_sell = 20 if sell * 0.001425 < 20 else math.floor(sell * 0.001425)
    tax_sell = math.ceil(sell * 0.003)

    money = sell - fee_sell - fee_buy - buy - tax_sell

    print(buy, fee_buy, sell, fee_sell, tax_sell)
    print(money)


