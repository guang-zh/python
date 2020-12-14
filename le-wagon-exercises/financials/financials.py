# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
import math
def forward_price(spot, interest_rate, time):
    price = spot * math.exp(interest_rate*time)
    return(round(price,2))


spot = 9999
interest_rate=0.1
time=10
print(forward_price(spot, interest_rate, time))




# TODO: 2nd exercise: Define the `short_pnl` function
def short_pnl(positions, mtm):
    sum = 0
    counter = 0
    length = len(positions)
    while counter < length:
        sum += (positions[counter] - mtm[counter])
        counter += 1
    return round(sum,2)

print(short_pnl([ 100, 140, 200 ], [ 110, 120, 180 ]))

positions=[100,140,200]
mtm=[110, 120, 180]
print(short_pnl(positions, mtm))
        