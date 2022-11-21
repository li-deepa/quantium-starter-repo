import pandas as pd
import dash

# loading the data into pandas
data_1=pd.read_csv("data/daily_sales_data_0.csv")
data_2=pd.read_csv("data/daily_sales_data_1.csv")
data_3=pd.read_csv("data/daily_sales_data_2.csv")

# selecting the data that only contain the products of 'pink morsel'
data_1=data_1.loc[data_1['product'] == 'pink morsel']
data_2=data_2.loc[data_2['product'] == 'pink morsel']
data_3=data_3.loc[data_3['product'] == 'pink morsel']

#merging the datasets to make into a single data
data=pd.concat([data_1,data_2,data_3],ignore_index=True)

#the head of the  data merged
print(data.head())

# dropping the nan values
data=data.dropna(axis='columns')

# summary of the data
print(data.info())
print(data.describe())

# converting the columns quantity and price to int and float for sales calculation
quantity=data['quantity'].astype(int)
price=data['price'].str.replace('$','')
price=price.astype('float')

sales=quantity*price
region=data['region']
date=data['date']
#print(sales)
# addding the sales column into data



print(data.head())
# adding the data to csv file
df=pd.DataFrame()
df['sales']=sales
df['date']=date
df['region']=region



print(df.head())
df.to_csv('final_data.csv')









