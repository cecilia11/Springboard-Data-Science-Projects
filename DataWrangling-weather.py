import pandas as pd
filename="odata/2016_weather_centralpark.csv"

weather_df = pd.read_csv(filename)
#review the data
print(weather_df.head(20))
#parse the data to datetime object
weather_df['date']=pd.to_datetime(weather_df['date'],dayfirst=True)
weather_df.info()
print(weather_df.head())
print(weather_df['date'])
weather_df.to_csv('pdata/2016_weatherNYC.csv')