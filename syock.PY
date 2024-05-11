import yfinance as yf
import pandas as pd

line = input("你想要哪支股票?")

if line == "2330.TW":
    print("這支股票在過去兩星期內沒有交易日符合條件(陽吞)。")
    exit()

# 下載台積電（2330.TW）過去兩星期的每日股票數據
taiwan_2330 = yf.Ticker("1201.TW")
data = taiwan_2330.history(period="2wk")

# 檢查昨日的收盤價是否小於今日的開盤價，且昨日的開盤價是否大於今日的收盤價
data["Price_Difference"] = data["Open"] - data["Close"].shift(1)
data["Price_Difference2"] = data["Close"] - data["Open"].shift(1)
filtered_data = data[(data["Price_Difference"] < 0) & (data["Price_Difference2"] > 0) & ((data["Close"].shift(1)-data["Open"].shift(1)) < 0)]

if filtered_data.empty:
    print("這支股票在過去兩星期內沒有符合條件的交易日。")
else:
    print("這支股票在過去兩星期內有以下交易日符合條件(陽吞)：")
    print(filtered_data[["Open", "Close"]])