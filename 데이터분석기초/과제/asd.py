import pandas as pd

df = pd.read_csv(r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\Midterm_______.csv')

k = (df['Category'] == 'Accessories')
df = df[k]

print(df['TotalPrice'].sum())