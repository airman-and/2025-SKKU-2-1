import pandas as pd

df = pd.read_csv(r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\Midterm_______.csv')

gb = df.groupby('Date')['TotalPrice'].sum().mean()

print(gb)



