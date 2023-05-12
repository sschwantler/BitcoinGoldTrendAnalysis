[![DOI](https://zenodo.org/badge/637382943.svg)](https://zenodo.org/badge/latestdoi/637382943)

# Trend Analysis of Bitcoin and Classical Asset Prices: A Comparative Study

This project focuses on the analysis and comparison of trends in three major asset prices, namely gold, bitcoin, and the Dow Jones Index[1][2][3]. The study aims to provide valuable insights into the behavior of these different asset classes and their interrelationships within the financial markets.

The project sources data from three distinct sources and employs various data manipulation techniques to process and aggregate the data. This data is then visualized using plots to facilitate the comparison of trends over time. The aggregated data is ultimately exported as a CSV file, which can be used for further analysis or integration into other tools or systems.

By analyzing the trends of these asset prices, we can gain a deeper understanding of their market dynamics and identify patterns that may be useful in predicting future trends. This knowledge can assist in portfolio management decisions and guide investment strategies. Additionally, the comparative nature of this study may provide insights into the relative performance of these asset classes under different market conditions, thereby helping investors diversify their portfolios and mitigate risks.

Overall, this project represents a valuable contribution to the field of financial analysis and provides a framework for further exploration of the interrelationships between different asset classes.

[1] https://www.nasdaq.com/market-activity/commodities/gc:cmx/historical

[2] https://api.coindesk.com/v1/bpi/historical/close.json?start=2010-07-17&end=2023-05-07

[3] https://query1.finance.yahoo.com/v7/finance/download/%5EDJI?period1=1271433600&period2=1651900800&interval=1d&events=history&includeAdjustedClose=true

## Reused data
File naming for reused data:
`<description>_v<versionNo>_<Access date YYYYMMDD>`


## Data Processing
* The reused data is loaded into pandas dataframes
* The DataFrames are transformed such that comparison is possible:
  * Unused columns are removed
  * Columns are renamed
  * Each dataframe requires a index as a date
  * The relative change in percent for each row is calculated
  * The timeframe considered is 2014-01-01 to 2022-01-01
* These dataframes are aggregated, plotted and stored in the csv file
* 
The generated file contains the following structure:

| Date | Gold_Price | Bitcoin_Price | Dow_Jones |
|------|------------|---------------|-----------|

All prices are in US Dollar.

## Produced Data

[![DOI](https://test.researchdata.tuwien.ac.at/badge/DOI/10.70124/c70yb-q6d73.svg)](https://doi.org/10.70124/c70yb-q6d73)

[Link to dataset at test.researchdata.tuwien.ac.at](https://test.researchdata.tuwien.ac.at/records/c70yb-q6d73?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImFmNzY5NGVmLTU0MWItNDE0Zi04ODAwLTFjNjFlNGQzNWY3OSIsImRhdGEiOnt9LCJyYW5kb20iOiIyYTM0MDE0ZmJjNTQyODVhZGY5YmY2OTk2NTA2NDk4YyJ9.j-bWYFdELo2y3RrC0R9e1_jnlbSryIeHValmldXz9pEDm9VzwSFqP47DjTcKNa4dfZQku6pyQ1mZQV-8iGV2Ow)

The file name will be `aggregated_gold_bitcoin_dowJones_<date YYYYMMDD>.csv`

