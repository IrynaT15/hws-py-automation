def candles_count(candle_number, make_new):
    total = candle_number
    rest = candle_number
    while rest >= make_new:
        new = rest // make_new
        total += new
        rest = rest - (new * make_new) + new

    return total


print(candles_count(5, 2))
print(candles_count(1, 2))
print(candles_count(15, 5))
print(candles_count(12, 2))
print(candles_count(6, 4))
print(candles_count(13, 5))
print(candles_count(2, 3))
