import pandas as pd

df = pd.read_csv(
    r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\transactions.csv'
)

# 할부 결제인 행만 필터링 (할부개월수 > 0)
df_inst = df[df['할부개월수'] > 0]

# 상호명별 할부 결제 횟수 집계
counts = df_inst['상호명'].value_counts()

# 최댓값을 가지는 상호명 추출
top = counts.idxmax()
print(f"1년간 할부 결제 횟수가 가장 많은 가맹점: {top}")







