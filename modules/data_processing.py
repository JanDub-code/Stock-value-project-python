from datetime import datetime, timedelta
from yahoo_fin import stock_info as si
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def stock_graph(ticker,expected_pe,price_sales,price_book,peg_ratio,historical_data,constant):
    months = 60

    start_date1 = datetime.today()
    date_index = pd.date_range(start=start_date1, periods=5*365, freq='D')
    filtered_index = date_index[date_index.weekday < 5].strftime('%Y-%m-%d')
    filtered_index = pd.to_datetime(filtered_index, format='%Y-%m-%d')

    
    n = len(filtered_index)
    last_value = historical_data.iloc[-1]["close"]
    annual_growth_rate = 0.10*constant

    
    growth_factor = (1 + annual_growth_rate) ** (1 / 252)
    exponential_index = pd.Index([last_value * growth_factor ** i for i in range(n)])
    

    plt.plot(historical_data.index, historical_data["close"])
    plt.plot(filtered_index,exponential_index,color='green')
    plt.title(f"{ticker} graph with prediction")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.savefig('stock_photo.jpg')

    difference = round(abs(last_value - exponential_index[-1]) / last_value * 100,2)
    sub_title = f"This is price prediction of the {ticker} stock for the next 5 years."
    before_photos = ["The next 4 graphs will show you separate valuation metrics used to ",
                     "determine current valuation and provide us with more ", "data to calculate future price."]
    before_stock = [f"Our calculations use weighted value of measured",
                    f"metrics as follows P/E 0.35, P/S 0.2, P/B 0.35 and PEG  0.1."]
    text_output = [f"Calculated difference between our current",
                   f" price and price in 5 years is {difference}%."]

    return sub_title,before_photos,before_stock,text_output
    

def percent_difference(subject, benchmark, name_of_metric):
    percent_difference = abs(subject - benchmark) / subject * 100

    if(subject == benchmark):
        outcome = f"Stock is fairly valued in {name_of_metric}"
    elif(subject > benchmark):
        outcome = f'Stock is {percent_difference:.2f}% overvalued in comparison to the benchmark in {name_of_metric}'
    else:
        outcome = f'Stock is {percent_difference:.2f}% undervalued in {name_of_metric}'

    fig, ax = plt.subplots()

    ax.set_xlim([0, subject+benchmark])
    ax.set_ylim([0, subject+benchmark])

    plt.axhline(subject, color='g', linestyle='-')
    plt.axhline(benchmark, color='r', linestyle='-')

    plt.title(f"{name_of_metric} of stock (green) and benchmark (red)")
    plt.xlabel(outcome)

    
    plt.axhspan(subject, benchmark, facecolor='blue', alpha=0.3, hatch='///')
    
    plt.savefig(f'{name_of_metric} photo.jpg')

def weighted_recalculation_PE(subject, benchmark):
    
    if subject == benchmark:
        return 1
    percent_difference = abs(subject - benchmark) / subject * 100
    if subject > benchmark:
        return 1-(0.35*percent_difference)/100
    else:
        return 1-(0.35*(-percent_difference))/100
    
def weighted_recalculation_PS(subject, benchmark):
        
        if subject == benchmark:
            return 1
        percent_difference = abs(subject - benchmark) / subject * 100
        if subject > benchmark:
            return 1-(0.25*percent_difference)/100
        else:
            return 1-(0.25*(-percent_difference))/100

def weighted_recalculation_PB(subject, benchmark):
     
        if subject == benchmark:
            return 1
        percent_difference = abs(subject - benchmark) / subject * 100
        if subject > benchmark:
            return 1-(0.35*percent_difference)/100
        else:
            return 1-(0.35*(-percent_difference))/100
        
def weighted_recalculation_PEG(subject, benchmark):
     
        if subject == benchmark:
            return 1
        percent_difference = abs(subject - benchmark) / subject * 100
        if subject > benchmark:
            return 1-(0.1*percent_difference)/100
        else:
            return 1-(0.1*(-percent_difference))/100
        
def weighted_constant(pe,ps,pb,peg):
    return (pe*ps*pb*peg)

def constantwithplus(pe,ps,pb,peg):
    return (pe+ps+pb+peg)/4