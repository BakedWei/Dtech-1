import yfinance as yf
import pandas as pd

def YangSwallow(data):
    data["Price_Difference"] = data["Open"] - data["Close"].shift(1)
    data["Price_Difference2"] = data["Close"] - data["Open"].shift(1)
    filtered_data = data[(data["Price_Difference"] < 0) & (data["Price_Difference2"] > 0) & ((data["Close"].shift(1)-data["Open"].shift(1)) < 0) & ((data["Close"]-data["Open"]) > 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(陽吞)：")
        print(filtered_data[["Open", "Close"]])
def InSwallow(data):
    data["Price_Difference"] = data["Close"] - data["Open"].shift(1)
    data["Price_Difference2"] = data["Open"] - data["Close"].shift(1)
    filtered_data = data[(data["Price_Difference"] < 0) & (data["Price_Difference2"] > 0) & ((data["Close"].shift(1)-data["Open"].shift(1)) > 0) & ((data["Close"]-data["Open"]) < 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(陰吞)：")
        print(filtered_data[["Open", "Close"]])

def create_ticker():
    symbol = input("請輸入您的目標股票代碼: ")
    ticker = yf.Ticker(symbol)
    return ticker


chosenStock = create_ticker()
stock = chosenStock.history(period="2mo")
if stock.empty:
    print("沒有這支股票捏;w;，再找找別的八")
else:
    YangSwallow(stock)
    InSwallow(stock)



