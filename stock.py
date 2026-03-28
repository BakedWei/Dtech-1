import yfinance as yf
import pandas as pd
from company import get_stock

chosenstock = []
stocks = []
chosenstock, stocks = get_stock()


def YangSwallow(data):
    data["Price_Difference"] = data["Open"] - data["Close"].shift(1)
    data["Price_Difference2"] = data["Close"] - data["Open"].shift(1)
    filtered_data = data[(data["Price_Difference"] < 0) &
                          (data["Price_Difference2"] > 0) &
                            ((data["Close"].shift(1)-data["Open"].shift(1)) < 0) &
                              ((data["Close"]-data["Open"]) > 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日(陽吞)。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(陽吞)")
        print(filtered_data[["Open", "Close"]])
def InSwallow(data):
    data["Price_Difference"] = data["Close"] - data["Open"].shift(1)
    data["Price_Difference2"] = data["Open"] - data["Close"].shift(1)
    filtered_data = data[(data["Price_Difference"] < 0) &
                          (data["Price_Difference2"] > 0) &
                            ((data["Close"].shift(1)-data["Open"].shift(1)) > 0) &
                              ((data["Close"]-data["Open"]) < 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日(陰吞)。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(陰吞)：")
        print(filtered_data[["Open", "Close"]])
def threesolderBlack(data):
    data["Price_Lower"] = data["Close"] - data["Close"].shift(1)
    data["Price_Lower2"] = data["Close"].shift(1) - data["Close"].shift(2)
    data["Price_Lower3"] = data["Close"].shift(2) - data["Close"].shift(3)
    data["Price_Lowera"] = data["Open"] - data["Open"].shift(1)
    data["Price_Lowera2"] = data["Open"].shift(1) - data["Open"].shift(2)
    data["Price_Lowera3"] = data["Open"].shift(2) - data["Open"].shift(3)
    
    filtered_data = data[(data["Price_Lower"] < 0) &
                         (data["Price_Lower2"] < 0) &
                         (data["Price_Lower3"] < 0) &
                         (data["Price_Lowera"] < 0) &
                         (data["Price_Lowera2"] < 0) &
                         (data["Price_Lowera3"] < 0) &
                         ((data["Close"] - data["Open"]) < 0) &
                         ((data["Close"].shift(1) - data["Open"].shift(1)) < 0) &
                         ((data["Close"].shift(2) - data["Open"].shift(2)) < 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日(黑三兵)。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(黑三兵)：")
        print(filtered_data[["Open", "Close"]])


def threesolderRed(data) :
    data["Price_Lower"] = data["Close"] - data["Close"].shift(1)
    data["Price_Lower2"] = data["Close"].shift(1) - data["Close"].shift(2)
    data["Price_Lowera"] = data["Open"] - data["Open"].shift(1)
    data["Price_Lowera2"] = data["Open"].shift(1) - data["Open"].shift(2)
    filtered_data = data[(data["Price_Lower"] < 0) &
                          (data["Price_Lower2"] < 0) &
                            (data["Price_Lowera"] < 0) &
                              (data["Price_Lowera2"] < 0) &
                              ((data["Close"].shift(2)-data["Open"].shift(2)) > 0) &
                              ((data["Close"].shift(1)-data["Open"].shift(1)) > 0) &
                              ((data["Close"]-data["Open"]) > 0)]

    if filtered_data.empty:
        print("這支股票在過去兩星期內沒有符合條件的交易日(紅三兵)。")
    else:
        print("這支股票在過去兩星期內有以下交易日符合條件(紅三兵)：")
        print(filtered_data[["Open", "Close"]])
def create_ticker(symbol):
    ticker = yf.Ticker(symbol)
    return ticker

print("你好呀!這裡是股票檢測小幫手，我們會預先幫你檢測台股喔!\n這邊還可以加多支自選股喔!\n")
print("你想加幾支呢?")
indexn = int(input())
if indexn != 0:
    for i in range(0, indexn):
        symbol = input("請輸入您想額外檢測的股票代碼: ")
        stocks.append(symbol)
        tmp = create_ticker(symbol)
        chosenstock.append(tmp)
for i in range(0, len(chosenstock)) :
    chosenstock[i] = chosenstock[i].history(period="2mo")
for i in range(0, len(chosenstock)) :
    stock = chosenstock[i]
    if stock.empty:
        print("沒有這支股票捏;w;，再找找別的八\n")
    else:
        print("目前檢測股票為:")
        print(stocks[i])
        #print("\n")
        YangSwallow(stock)
        InSwallow(stock)
        threesolderBlack(stock)
        threesolderRed(stock)
        print("\n")