import yfinance as yf
import pandas as pd
line = input("你想要哪支股票?")

if line == "2330.TW":
    print("這支股票在過去兩星期內沒有交易日符合條件(陽吞)。")
    exit()
