import pandas as pd

# 파일 경로
path_m = r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\merchants.csv'
path_p = r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\payments.csv'

# CSV 읽기 (BOM 포함 UTF-8)
merchants = pd.read_csv(path_m, encoding='utf-8-sig')
payments  = pd.read_csv(path_p, encoding='utf-8-sig')

# 병합 및 분기 계산
df = payments.merge(merchants, on='상호명')
df['month']   = df['결제월'].str.rstrip('월').astype(int)
df['quarter'] = ((df['month'] - 1) // 3) + 1

# 분기·업종별 합계 구하고, 분기별 최댓값만 추출
agg = df.groupby(['quarter','업종'], as_index=False)['결제금액'].sum()
top = agg.loc[agg.groupby('quarter')['결제금액'].idxmax()]

# 출력
for _, r in top.sort_values('quarter').iterrows():
    print(f"{int(r['quarter'])}분기: {r['업종']}")
