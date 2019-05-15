from pandas import *

f = pandas.read_csv('my-food-test-data.csv')
df.to_sql(table_name, conn, if_exists='append', index=False)
