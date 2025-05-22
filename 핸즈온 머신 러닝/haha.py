import pandas as pd

df = pd.read_csv(r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\Midterm_______.csv')


gb = df.groupby('Date')['TotalPrice']


gb = gb.sum().sort_values(ascending = False).head(3)


dates = list(gb.index)
print(dates)


