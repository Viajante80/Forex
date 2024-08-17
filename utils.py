def get_data_filename(pair, granularity, subfolder=False):
    if subfolder:
        return f"../his_data/{pair}_{granularity}.pkl"
    else:
        return f"his_data/{pair}_{granularity}.pkl"


def get_instruments_data_filename(subfolder=False):
    if subfolder:
        return "../instruments.pkl"
    else:
        return "instruments.pkl"


def get_currency_instruments_data_filename(subfolder=False):
    if subfolder:
        return "../currency_instruments.pkl"
    else:
        return "currency_instruments.pkl"


if __name__ == "__main__":
    print(get_data_filename("EUR_USD", "H1", True))
    print(get_instruments_data_filename(True))
