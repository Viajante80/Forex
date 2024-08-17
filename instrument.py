import pandas as pd
import utils


class Instrument:
    def __init__(self, ob):
        self.name = ob["name"]
        self.ins_type = ob["type"]
        self.displayName = ob["displayName"]
        self.pipLocation = pow(10, ob["pipLocation"])  # -4 -> 0.0001
        self.marginRate = ob["marginRate"]

    def __repr__(self):
        return str(vars(self))

    # ---------------------------
    @classmethod
    def get_instruments_df(cls, subfolder=False):
        return pd.read_pickle(utils.get_instruments_data_filename(subfolder))

    @classmethod
    def get_instruments_list(cls, subfolder=False):
        df = cls.get_instruments_df(subfolder)
        return [Instrument(x) for x in df.to_dict(orient="records")]

    @classmethod
    def get_currency_instruments_df(cls, subfolder=False):
        return pd.read_pickle(utils.get_currency_instruments_data_filename(subfolder))

    @classmethod
    def get_currency_instruments_list(cls, subfolder=False):
        # Read the data from the pickle file
        df = cls.get_currency_instruments_df(subfolder)

        # Convert the DataFrame to a list of dictionaries and create Instrument objects
        return [Instrument(x) for x in df.to_dict(orient="records")]

    """
    dict to access instruments by pair name

    instrument_dict =
    {
        "EUR_USD" : Instrument(),
        "EUR_GBP" : Instrument(),
        "..." : Instrument(),
    }

    our_instrument = instrument_dict["EUR_USD"]
    """

    @classmethod
    def get_instruments_dict(cls, subfolder=False):
        i_list = cls.get_instruments_list(subfolder)
        i_keys = [x.name for x in i_list]
        return {k: v for (k, v) in zip(i_keys, i_list)}

    @classmethod
    def get_instrument_by_name(cls, pairname, subfolder=False):
        d = cls.get_instruments_dict(subfolder)
        if pairname in d:
            return d[pairname]
        else:
            return None


if __name__ == "__main__":
    # print(Instrument.get_currency_instruments_df(True))
    # for k, v in Instrument.get_instruments_dict().items():
    #     print(k, v)
    print(Instrument.get_instrument_by_name("EUR_USD"))
