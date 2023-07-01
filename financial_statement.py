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

#Ticker Symbol (US Stock Market only)
ticker = 'ai'

#Folder path to save the excel file (modify accordingly to your preference)
folderpath = 'Financial Statements'

urls = {}
urls['Income Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
urls['Income Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/?p=quarterly"
urls['Balance Sheet Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/"
urls['Balance Sheet Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/?p=quarterly"
urls['Cash Flow Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/"
urls['Cash Flow Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/?p=quarterly"
urls['Ratio Annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/ratios/"
urls['Ratio Quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/ratios/?p=quarterly"

# Get the current script's directory
current_directory = os.getcwd()

# Specify the relative directory
relative_directory = os.path.join(current_directory, '..', folderpath)

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

    # Create formats for numbers and percentages.
    num_format = xlwriter.book.add_format({'num_format': '#,##0.00'})
    percent_format = xlwriter.book.add_format({'num_format': '0.00%'}) # 0.00% will change the decimals to 2

    ### Adjust the column widths to fit the longest string in the column. Remove if not needed.
    worksheet = xlwriter.sheets[key]  # pull worksheet object
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]

        for row_num, value in enumerate(series.values):
            try:
                # Check if the value ends with a '%' symbol
                if str(value).endswith('%'):
                    # If yes, remove the '%' symbol and convert the value to a float
                    value = float(value.replace('%', ''))

                    # Then, divide by 100 to convert the percentage to a decimal
                    value = value / 100

                    # Write the value to the Excel file, using the percentage format
                    worksheet.write(row_num+1, idx, value, percent_format)
                else:
                    # If not, simply convert the value to a float
                    value = float(value)

                    # Write the value to the Excel file, using the number format
                    worksheet.write(row_num+1, idx, value, num_format)
            except ValueError:
                # If a ValueError occurs, this means that the value could not be converted to a float
                # In this case, simply pass to the next value
                pass
                
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            )) + 4  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width

xlwriter.close()
