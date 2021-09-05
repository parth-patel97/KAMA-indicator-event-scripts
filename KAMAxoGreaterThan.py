import math,csv, random
import datetime as dt
import numpy as np
import pandas as pd
import talib

# DEFAULT VARIABLES (do not delete them)

file_name_base = "C:/Users/parth/TradersToolbox/TradersToolbox/Data/ESRaw.txt"
file_name_market2 = None
file_name_market3 = None
file_name_Vix = None
start = dt.datetime(2010, 1, 1)
stop = dt.datetime(2011, 1, 1)
df1, df2, df3, dfV = None, None, None, None


# Read data

def ReadData():
    global df1
    df1 = pd.read_csv(file_name_base, delimiter=',', index_col='Date', parse_dates=True)
    df1 = df1[df1.index >= start]
    df1 = df1[df1.index <= stop]

    if file_name_market2 != None and len(file_name_market2) > 0:
        global df2
        df2 = pd.read_csv(file_name_market2, delimiter=',', index_col='Date', parse_dates=True)
        df2 = df2[df2.index >= start]
        df2 = df2[df2.index <= stop]

    if file_name_market3 != None and len(file_name_market3) > 0:
        global df3
        df3 = pd.read_csv(file_name_market3, delimiter=',', index_col='Date', parse_dates=True)
        df3 = df3[df3.index >= start]
        df3 = df3[df3.index <= stop]

    if file_name_Vix != None and len(file_name_Vix) > 0:
        global dfV
        dfV = pd.read_csv(file_name_Vix, delimiter=',', index_col='Date', parse_dates=True)
        dfV = dfV[dfV.index >= start]
        dfV = dfV[dfV.index <= stop]

#CUSTOM INDICATOR FUNCTION (main entry point called from TradersToolbox)

def GetCustomSignal():
    ReadData()
    # signal calculation code

    global df1
    window, pow1, pow2 = 20, 2, 30
    df1['KAMA'] = talib.KAMA(df1['Close'].values, window)
    Signal = [1 if df1['Close'][i] > df1['KAMA'][i] else 0 for i, m in
              enumerate(df1['KAMA'])]
    df1["Signal"] = Signal

    #Should return list of int (same length as Close)
    return Signal
