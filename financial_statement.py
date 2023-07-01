import requests
from bs4 import BeautifulSoup
import pandas as pd
from xlsxwriter import Workbook
import os

headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

ticker = 'AI'

urls = {}
urls['Income Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
urls['Income Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/?period=quarterly"
urls['Balance Sheet Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/"
urls['Balance Sheet Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/?period=quarterly"
urls['Cash Flow Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/"
urls['Cash Flow Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/?period=quarterly"
urls['Ratio Annually'] = f"https://stockanalysis.com/stocks/aapl/financials/ratios/"
urls['Ratio Quarterly'] = f"https://stockanalysis.com/stocks/aapl/financials/ratios/?period=quarterly"

# Get the current script's directory
current_directory = os.getcwd()

# Specify the relative directory
relative_directory = os.path.join(current_directory, '..', 'Financial Statements')

# Make sure the directory exists
os.makedirs(relative_directory, exist_ok=True)

# Create the file path
file_path = os.path.join(relative_directory, f'{ticker}-finstatement.xlsx')

xlwriter = pd.ExcelWriter(file_path, engine='xlsxwriter')

for key in urls.keys():
    response = requests.get(urls[key], headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    df = pd.read_html(str(soup), attrs={'data-test': 'financials'})[0]
    df.to_excel(xlwriter, sheet_name=key, index=False)

xlwriter.close()
