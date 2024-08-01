import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import defs 
import pandas as pd

class OandaApi:
    def __init__(self, environment="practice"):
        self.environment = environment
        self.client = oandapyV20.API(access_token=defs.API_KEY, environment=environment)

    def fetch_instruments(self):
        request = accounts.AccountInstruments(accountID=defs.ACCOUNT_ID)
        response = self.client.request(request)
        return response
    
    def fetch_candles(self, instrument, count, granularity):

        params = dict(
            count = count,
            granularity = granularity,
            price = "MBA"
        )
        
        request = instruments.InstrumentsCandles(instrument=instrument, params=params)
        response = self.client.request(request)
        return response
    

if __name__ == "__main__":
    api = OandaApi()
    response = api.fetch_candles('EUR_USD', 5, 'H1')
    print(response)

