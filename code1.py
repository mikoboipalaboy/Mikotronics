
#%%
add(10,5)
#%%

#pip install pandas
import pandas as pd

df_test1=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_Country.csv')
df_test2=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_Group X.csv')
df_test3=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_Group Y.csv')
df_test4=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_Project.csv')
df_test5=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_Response Class.csv')
df_test6=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Info_X Rank Y.csv')

# Checking if Unique %%
df_test2.Country_ID.nunique()


#%%
df_test7=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Response 2007.csv')
df_test8=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Response 2008.csv')
df_test9=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Response 2009.csv')
df_test10=pd.read_csv('C:/Users/AcerUser/Downloads/NMG_MPBagsit/input/Response 2010.csv')
#%%


# Data Frames Merging %%
merge1 = pd.merge(df_test1, df_test2, how='inner')

merge1.columns




