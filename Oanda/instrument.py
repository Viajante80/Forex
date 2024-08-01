import pandas as pd
import utils  

class Instrument:
    def __init__(self, ob):
        self.name = ob['name']
        self.ins_type = ob['type']
        self.displayName = ob['displayName']
        self.pipLocation = pow(10, ob['pipLocation']) # -4 -> 0.0001
        self.marginRate = ob['marginRate']
        
    def __repr__(self):
        return str(vars(self))
    
    # ---------------------------
    @classmethod
    def get_instruments_df(cls, subfolder = False):
        return pd.read_pickle(utils.get_instruments_data_filename(subfolder))
    
    @classmethod
    def get_instruments_list(cls, subfolder = False):
        df = cls.get_instruments_df(subfolder)
        return [Instrument(x) for x in df.to_dict(orient='records')]
    
    @classmethod
    def get_currency_instruments_df(cls, subfolder = False):
        return pd.read_pickle(utils.get_currency_instruments_data_filename(subfolder))
    
    @classmethod
    def get_currency_instruments_list(cls, subfolder = False):
        df = cls.get_currency_instruments_df(subfolder)
        return [Instrument(x) for x in df.to_dict(orient='records')]
    
if __name__ == "__main__":
    print(Instrument.get_currency_instruments_df(True))