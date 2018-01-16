import pandas as pd
import os

# get all the raw data filenames (CitiBike-trips) from the data directory
file_list = os.listdir("./odata/2016/")


# grab the characters of month from file name:
def month_chars(x):
    return (x[4:5])


# sorted filename
sorted(file_list, key=month_chars)
print(file_list)

drop_columns=['stoptime','start station name','start station latitude','start station longitude','end station name','end station latitude','end station longitude']
df_list = []
for filename in file_list[0:2]:
  print(filename)
  df_list.append(pd.read_csv('odata/2016/'+filename))
trip2016q1_df = pd.concat(df_list)
trip2016q1_df.dropna(how='any')

trip2016q1_df.info()
print(trip2016q1_df.head())

trip2016q1_df=trip2016q1_df.drop(drop_columns,axis=1)
trip2016q1_df.info()
trip2016q1_df.to_csv('pdata/2016Q6.csv')
print(trip2016q1_df.head())