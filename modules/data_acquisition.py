from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
import pandas as pd

def get_valuation_data(ticker):
    valuations = si.get_stats_valuation(ticker)
    df = pd.DataFrame(valuations)

    row= df.loc[df[0] == 'Price/Sales (ttm)']
    row1= df.loc[df[0] == 'Price/Book (mrq)']
    row2= df.loc[df[0] == 'Trailing P/E']
    row3= df.loc[df[0] == 'Forward P/E']
    row4= df.loc[df[0] == 'PEG Ratio (5 yr expected)']

    price_sales = row.iloc[0,1]
    price_book = row1.iloc[0,1]
    trailing_pe = row2.iloc[0,1]
    forward_pe = row3.iloc[0,1]
    peg_ratio = row4.iloc[0,1]

    expected_pe = (float(trailing_pe )+ float(forward_pe)) / 2
    return float(price_sales), float(price_book), expected_pe, float(peg_ratio)

def get_benchmark_data():
	bench_pe = 16
	bench_price_sales = 1.69
	bench_price_book = 2.98
	bench_peg_ratio = 2.2
	
	return bench_pe, bench_price_sales, bench_price_book, bench_peg_ratio

def get_raw_data(ticker):
    years = 5
    end_date = datetime.today().strftime('%m/%d/%Y')
    start_date = (datetime.today() - timedelta(days=years*365)).strftime('%m/%d/%Y')

    historical_data = si.get_data(ticker, start_date=start_date, end_date=end_date)
    return historical_data, years, ticker

