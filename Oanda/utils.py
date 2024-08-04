def get_data_filename(pair, granularity):
    return f"./Oanda/data/{pair}_{granularity}.pkl"

def get_data_filename_ipynb(pair, granularity):
    return f"./data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    return "./Oanda/instruments.pkl"

if __name__ == "__main__":
    print(get_data_filename("EUR_USD", "H1"))
    print(get_instruments_data_filename())