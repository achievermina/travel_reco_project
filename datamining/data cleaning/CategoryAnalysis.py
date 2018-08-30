import pandas as pd

df = pd.read_csv('/Users/mina/Dropbox/dropbox_project/category.csv',index_col=0)

df2 = df.groupby(['city_name','category_name'],as_index=False, sort=False)['category_id'].count()
df2.sort_values('category_id',ascending=False)
print(df2)

df2.rename(columns={'category_id':'count_category'},inplace=True)
print(df2)
