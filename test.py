import pandas as pd


df = pd.read_html('https://www.cfl.ca/players/')
print(df)