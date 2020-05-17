from pycoingecko import CoinGeckoAPI
import time

# https://github.com/man-c/pycoingecko
# https://www.youtube.com/watch?v=hpkOjWn8j5U

# coded by Taj and HMan

# add - time when new price was added
# add - write data out to file

cg = CoinGeckoAPI()

cryptoNames = ['bitcoin', 'ethereum']

priceDict = {
}
while True:
    for crypto in cryptoNames:

        price = cg.get_price(ids=crypto, vs_currencies="usd")

        usdPrice = price[crypto]['usd']

        if priceDict.get(crypto):
            priceList = priceDict.get(crypto)
            if priceList[-1] != usdPrice:
                priceList.append(usdPrice)
        else:
            newList = [usdPrice]
            priceDict[crypto] = newList

    print(priceDict)
    time.sleep(60)




