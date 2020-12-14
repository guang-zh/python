# pylint: disable=missing-docstring

# Dictionary Slides
phones={'john':4019,'paul':4121}
print(type(phones))
print(phones['john'])
print(phones)

populations = {'paris':2.2,'london':8.1}
populations['brussels']=1.2
populations['london']
populations.get('new-york',0)
populations['london']=populations['london']+0.00001
del(populations['paris'])
print(populations)

musicians = {'john':'guitar', 'paul':'bass'}
for name, instrument in musicians.items():
    print(f'{name.capitalize()} plays the {instrument}.')



# TODO: start by defining a `portfolio` using a dict!

# portfolio_advanced.py
portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "FB": {
    "volume": 18,
    "strike": 209.0
  }
}

print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])

market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "FB":    179.06
}
sum=0
for index,value in market.items():
    sum+=portfolio[index]['volume']*(portfolio[index]['strike']-value)
print(sum)

import requests

url = "https://api.iextrading.com/1.0/tops/last?symbols=AAPL,GOOG,TSLA,FB"
real_time_market = requests.get(url).json()
print(real_time_market)

market = {}
for stock in real_time_market:
    market[stock['symbol']]=stock['price']
print(market)
market = dict((stock['symbol'], stock['price']) for stock in real_time_market)
print(market)

portfolio["AMZN"] = {
  "volume": 10,
  "strike": 1812.11
}
symbols = ",".join(portfolio.keys())
url = f"https://api.iextrading.com/1.0/tops/last?symbols={symbols}"
real_time_market = requests.get(url).json()
print(real_time_market)

