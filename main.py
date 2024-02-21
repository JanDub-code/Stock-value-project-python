from modules import data_acquisition
from modules import data_processing
from modules import pdf
import os
import subprocess


modules = ["numpy", "pandas", "matplotlib",'yahoo_fin', 'datetime', 'reportlab', 'PyPDF2']

for modulex in modules:
    try:
        subprocess.check_call(["pip", "install", modulex])
    except subprocess.CalledProcessError as e:
        print(f"Module {modulex} is already installed.")

# image path definitions
image1 = 'PEG Ratio photo.jpg'
image2 = 'Price to Book photo.jpg'
image3 = 'Price to Earnings photo.jpg'
image4 = 'Price to Sales photo.jpg'
image5 = 'stock_photo.jpg'

input=input("Zadejte ticker akcie: ")

historical_data, years, ticker= data_acquisition.get_raw_data(input)
price_sales, price_book, expected_pe, peg_ratio =data_acquisition.get_valuation_data(ticker)
bench_pe, bench_price_sales, bench_price_book, bench_peg_ratio=data_acquisition.get_benchmark_data()

pe = data_processing.weighted_recalculation_PE(expected_pe,bench_pe)
ps = data_processing.weighted_recalculation_PS(price_sales,bench_price_sales)
pb = data_processing.weighted_recalculation_PB(price_book,bench_price_book)
peg = data_processing.weighted_recalculation_PEG(peg_ratio,bench_peg_ratio)

weightedconstant=data_processing.weighted_constant(pe,ps,pb,peg)

sub_title,before_photos,before_stock,text_output =data_processing.stock_graph(ticker,expected_pe,price_sales,price_book,peg_ratio,historical_data,weightedconstant)
data_processing.percent_difference(expected_pe,bench_pe,"Price to Earnings")
data_processing.percent_difference(price_sales,bench_price_sales,"Price to Sales")
data_processing.percent_difference(price_book,bench_price_book,"Price to Book")
data_processing.percent_difference(peg_ratio,bench_peg_ratio,"PEG Ratio")

pdf.pdf_gen(ticker, image1, image2, image3, image4, image5, sub_title, before_photos, before_stock, text_output)

#   removal of temporary files
os.remove(image1)
os.remove(image2)
os.remove(image3)
os.remove(image4)
os.remove(image5)