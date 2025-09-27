from marketflow.market_ticker import MarketTickers
from marketflow.market_data import MarketData
from marketflow.market_registry import MarketRegistry

register = MarketRegistry()
#register.purge()

a = MarketTickers()
ticker = a.getTickers("BRVM")

b = MarketData()
b.getData("BRVM",['BNBC.ci'])