import pandas as pd

df = pd.read_csv("report1.csv", sep=";", encoding='cp1251', parse_dates=["Data"], dayfirst=True)
df.sort_values(by="Data", inplace=True)
df.reset_index(inplace=True, drop=True)

for i, g in df.groupby(df["Data"].dt.month):
    lst = g.index[-1]+1 if g.index[-1] < df.index[-1] else g.index[-1]
    res = df.iloc[g.index[0]:lst+1]
    res.to_csv(f"report_{i}.csv", sep=";", encoding='cp1251', index=None, date_format='%d.%m.%Y %H:%M:%S')
