from pandas_datareader import data as pdr
import fix_yahoo_finance as yf # <== that's all it takes :-)
# download dataframe
ptt = pdr.get_data_yahoo("PTT.BK", start="2017-01-01", end="2017-04-30")
print(ptt.tail())
