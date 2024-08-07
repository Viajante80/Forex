def get_data_filename(pair, granularity):
    return f"../data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    return "instruments.pkl"

def get_currency_instruments_data_filename():
    return "currency_instruments.pkl"

if __name__ == "__main__":
    print(get_data_filename("EUR_USD", "H1"))
    print(get_instruments_data_filename())