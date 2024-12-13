def test_config():
    return True

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    AAPL = Stock("AAPL", "Apple Inc")
    CAT = Stock( "CAT", "Caterpillar")
    EK = Stock("EK", "Eastman Kodak")
    GOOG = Stock("GOOG", "Google")
    MSFT = Stock("MSFT", "Microsoft")

    dictionary = {
        "AAPL":AAPL,
        "CAT":CAT,
        "EK":EK,
        "GOOG":GOOG,
        "MSFT":MSFT
    }

    print("Symbol \t\t| Company Name")
    print("_______________________________")
    for entry in dictionary:
        print(dictionary.get(entry).get_symbol(), "\t\t|", dictionary.get(entry).get_company_name())
