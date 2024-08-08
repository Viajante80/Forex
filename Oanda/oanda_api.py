import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import Oanda.defs as defs
import pandas as pd
import Oanda.utils as utils 


class Instrument:
    def __init__(self, ob):
        self.name = ob['name']
        self.ins_type = ob['type']
        self.displayName = ob['displayName']
        self.pipLocation = pow(10, ob['pipLocation']) # -4 -> 0.0001
        self.marginRate = ob['marginRate']
        
    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def get_instruments_df(cls):
        return pd.read_pickle(utils.get_instruments_data_filename())
    
    @classmethod
    def get_instruments_list(cls):
        df = cls.get_instruments_df()
        return [Instrument(x) for x in df.to_dict(orient='records')]
    
    @classmethod
    def get_currency_instruments_df(cls):
        return pd.read_pickle(utils.get_currency_instruments_data_filename())
    
    @classmethod
    def get_currency_instruments_list(cls):
        df = cls.get_currency_instruments_df()
        return [Instrument(x) for x in df.to_dict(orient='records')]

   
    @classmethod
    def get_instruments_api(cls, environment="practice"):
        
        # Create the API client
        client = oandapyV20.API(access_token=defs.API_KEY, environment=environment)

        # Define the request for instruments associated with your account
        request = accounts.AccountInstruments(accountID=defs.ACCOUNT_ID)

        # Perform the request
        response = client.request(request)

        return response

