# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os

OUTPUT_FOLDER = "data_output"

if not os.path.exists(OUTPUT_FOLDER):
    # if the demo_folder directory is not present
    # then create it.
    os.makedirs(OUTPUT_FOLDER)

# Getting the Data from APIs
gold_url = "https://datahub.io/core/gold-prices/r/monthly.csv"
bitcoin_url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2010-07-17&end=2023-05-07"
dow_url = "https://query1.finance.yahoo.com/v7/finance/download/%5EDJI?period1=1271433600&period2=1651900800&interval=1d&events=history&includeAdjustedClose=true"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Gold Data from Quandl
gold_df = pd.read_csv(gold_url, parse_dates=['Date'], index_col='Date')
gold_df = gold_df.rename(columns={"Price": "Gold_Price"})
gold_df["Gold_Change"] = gold_df["Gold_Price"].pct_change()
gold_df = gold_df.loc['2014-01-01':'2020-01-01']


# Bitcoin Data from CoinDesk
bitcoin_response = requests.get(bitcoin_url, headers=headers)
bitcoin_data = bitcoin_response.json()['bpi']

bitcoin_df = pd.DataFrame.from_dict(bitcoin_data, orient='index', columns=['Bitcoin_Price'])
bitcoin_df.index = pd.to_datetime(bitcoin_df.index)
bitcoin_df = bitcoin_df.resample('MS').mean()
bitcoin_df["Bitcoin_Change"] = bitcoin_df["Bitcoin_Price"].pct_change()
bitcoin_df = bitcoin_df.loc['2014-01-01':'2020-01-01']


# Dow Jones Data from Yahoo Finance
dow_df = pd.read_csv(dow_url)
dow_df['Date'] = pd.to_datetime(dow_df['Date'])
dow_df.set_index('Date', inplace=True)
dow_df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)
dow_df.columns = ['Dow_Jones']
dow_df = dow_df.resample('MS').mean()
dow_df["Dow_Jones_Change"] = dow_df["Dow_Jones"].pct_change()
dow_df = dow_df.loc['2014-01-01':'2020-01-01']


# Joining all Datasets
df_abs = pd.concat([gold_df["Gold_Price"], bitcoin_df["Bitcoin_Price"], dow_df["Dow_Jones"]], axis=1)
df_percent = pd.concat([gold_df["Gold_Change"], bitcoin_df["Bitcoin_Change"], dow_df["Dow_Jones_Change"]], axis=1)

# Data Processing
df_abs.fillna(method='ffill', inplace=True)
df_abs.dropna(inplace=True)

df_percent.fillna(method='ffill', inplace=True)
df_percent.dropna(inplace=True)

# Data Visualization
plt.figure()
plt.title('Gold, Bitcoin and Dow Jones Prices')
sns.lineplot(data=df_abs)
plt.savefig(f'{OUTPUT_FOLDER}/gold_bitcoin_dow_raw.png')
plt.show()

plt.figure()
plt.title('Relative Development of Gold, Bitcoin and Dow Jones Prices')
sns.lineplot(data=df_percent)
plt.ylabel('Relative Percent Change')
plt.savefig(f'{OUTPUT_FOLDER}/gold_bitcoin_dow_rel_dev.png')
plt.show()

fig = plt.figure(constrained_layout=True)
ax1 = fig.add_subplot(111)
line_bitcoin = ax1.plot(df_abs.index, df_abs['Bitcoin_Price'], color='tab:orange', label="Bitcoin Price", linestyle='dashed')
line_gold = ax1.plot(df_abs.index, df_abs['Gold_Price'], color='tab:blue', label="Gold Price")
ax2 = ax1.twinx()
line_dow = ax2.plot(df_abs.index, df_abs['Dow_Jones'], color='tab:green', label="Dow Jones", linestyle='dotted')
fig.legend(loc="upper left", bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes)
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (US Dollar)")
ax2.set_ylabel("Dow Jones")
plt.title("Development of Gold and Bitcoin Price compared to Dow Jones Growth")
plt.savefig(f'{OUTPUT_FOLDER}/gold_bitcoin_dow_dev.png', bbox_inches="tight")
plt.show()

# Machine-Actionable Data
df_abs.to_csv(f'{OUTPUT_FOLDER}/gold_bitcoin_dow.csv')

