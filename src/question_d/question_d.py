class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    AAPL = Stock("AAPL", "Apple Inc")
    CAT = Stock( "CAT", "Caterpillar")
    EK = Stock("EK", "Eastman Kodak")
    GOOG = Stock("GOOG", "Google")
    MSFT = Stock("MSFT", "Microsoft")
    return [AAPL, CAT, EK, GOOG, MSFT]

def list_the_stocks(stock_list):
    for entry in stock_list:
        print(entry.get_symbol(), "\t\t|", entry.get_company_name())
