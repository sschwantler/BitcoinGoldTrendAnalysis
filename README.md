# DS_EX1_SS23

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
* These dataframes are aggregated, plotted and stored in the csv file
* 
The generated file contains the following structure:

| Date | Gold_Price | Bitcoin_Price | Dow_Jones |
|------|------------|---------------|-----------|

All prices are in US Dollar.

The file name will be `aggregated_gold_bitcoin_dowJones_<date YYYYMMDD>.csv`