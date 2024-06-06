import yfinance as yf
import pandas as pd
line = input("你想要哪支股票?")
prestockls = ["2330.TW", "2388.TW", "2454.TW", "1101.TW", "1216.TW", "6505.TW", "2207.TW",
               "2201.TW", "2548.TW", "2603.TW", "2707.TW", "2912.TW", "2731.TW", "9917.TW"]

print(len(prestockls))

#if line == "2330.TW":
#    print("這支股票在過去兩星期內沒有交易日符合條件(陽吞)。")
#    exit()
