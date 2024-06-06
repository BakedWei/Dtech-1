import yfinance as yf
import pandas as pd

chosenstock = []
cpystock = []
prestockls = ["2330.TW", "2388.TW", "2454.TW", "1101.TW", "1216.TW", "6505.TW", "2207.TW",
               "2201.TW", "2548.TW", "2603.TW", "2707.TW", "2912.TW", "2731.TW", "9917.TW"]
for i in range(0, len(prestockls)):
    cpystock.append(prestockls[i])
    chosenstock.append(yf.Ticker(prestockls[i]))

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

def threesolderBlack(data) :
    data["Price_Lower"] = data["Close"] - data["Close"].shift(1)
    data["Price_Lower2"] = data["Close"].shift(1) - data["Close"].shift(2)
    data["Price_Lowera"] = data["Open"] - data["Open"].shift(1)
    data["Price_Lowera2"] = data["Open"].shift(1) - data["Open"].shift(2)
    filtered_data = data[(data["Price_Lower"] > 0) &
                          (data["Price_Lower2"] > 0) &
                            (data["Price_Lowera"] >0) &
                              (data["Price_Lowera2"]>0) &
                              ((data["Close"].shift(2)-data["Open"].shift(2)) < 0) &
                              ((data["Close"].shift(1)-data["Open"].shift(1)) < 0) &
                              ((data["Close"]-data["Open"]) < 0)]

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
def create_ticker():
    symbol = input("請輸入您想額外檢測的股票代碼: ")
    ticker = yf.Ticker(symbol)
    return ticker

print("你好呀!這裡是股票檢測小幫手，我們會預先幫你間檢測精選台股喔!\n這邊還可以加多支自選股喔!\n")
print("你想加幾支呢?")
indexn = int(input())
for i in range(0, indexn):
    tmp= create_ticker()
    chosenstock.append(tmp)

for i in range(0, len(chosenstock)) :
    cpystock.append(chosenstock[i])
    chosenstock[i] = chosenstock[i].history(period="2mo")

for i in range(0, len(chosenstock)) :
    stock = chosenstock[i]
    if stock.empty:
        print("沒有這支股票捏;w;，再找找別的八\n")
    else:
        print("目前檢測股票為:")
        print(cpystock[i])
        #print("\n")
        YangSwallow(stock)
        InSwallow(stock)
        threesolderBlack(stock)
        threesolderRed(stock)
        print("\n")


