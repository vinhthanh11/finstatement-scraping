## Financial Statements Scraper

This code is a Python script that scrapes financial statements from the website stockanalysis.com for a given stock ticker symbol (limited to the **US stock market**). It retrieves the following financial statements for a specified stock:

- Income Statement: Annually and Quarterly (the most recent available)
- Balance Sheet: Annually and Quarterly (the most recent available)
- Cash Flow Statement: Annually and Quarterly (the most recent available)
- Financial Ratios: Annually and Quarterly (the most recent available)

The script uses the `requests` library to send HTTP requests and retrieve the HTML content of the web pages. It utilizes the `BeautifulSoup` library to parse the HTML and extract the financial statement tables. The extracted data is then processed and saved into an Excel file using the `pandas` library and the `xlsxwriter` engine.

To use this script, please follow these instructions:

1. Open the Python file containing the code.
2. Modify the following variables according to your preferences:

- `ticker`: Enter the stock ticker symbol for which you want to scrape financial statements. For example, you can set `ticker = 'DIS'` to scrape financial statements for The Walt Disney Company.
- `folderpath`: Specify the folder path where you want to save the resulting Excel file. By default, it is set to `'Financial Statements'`. You can modify this to your preferred *relative* directory. An absolute path example is that you can set `folderpath = 'C:/Documents/Financials'` to save the file in the `C:/Documents/Financials` directory.
- `urls`: These are the URLs for each type of financial statement. They are pre-configured to scrape data from stockanalysis.com based on the provided stock ticker symbol. You can modify these URLs if you want to scrape from a different source.

For example, the default URLs for the `urls` dictionary are set as follows:

3. After making the necessary modifications, save the Python file.
4. Run the script using a Python interpreter or an integrated development environment (IDE) that supports Python.
5. The script will scrape the financial statements for the specified stock ticker symbol and save them into an Excel file in the specified folder path.
6. Once the script finishes running, you can open the Excel file to access the scraped financial data.

**Note:** You may need to install the required libraries (`requests`, `BeautifulSoup`, `pandas`, `xlsxwriter`) before running this code.

P.s: I particularly use this for company valuation with FCF, DCF methods. Will convert this into a small desktop app in the future. Don't be shy to ask any question (literally everything). Open to any commits and changes. :) 