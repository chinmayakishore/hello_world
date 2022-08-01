import codeacademylib3
import pandas as pd
movies=pd.read_csv("netflix.csv")
print(movies.head())
print(movies['rating'].unique())
