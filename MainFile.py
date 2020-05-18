from pycoingecko import CoinGeckoAPI
import time

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
   
