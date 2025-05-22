import pandas as pd
import numpy as np

df = pd.read_csv('jurk\입출금.csv')

# 카테고리 별 총 출금 내역을 특정 기준으로 출력한다.
# 출금 및 카테고리 열을 제외한 나머지 열을 제거
# 카테고리 별 총 출금량을 계산하여, 출금량이 많은 카테고리부터 순서대로 정렬한다.
#총 출금량이 0인 카테고리 또한 제거한다.
#결과물을 out 변수에 저장한다.

df = df.drop(columns=['일시', '입금', '잔고'])
gb = df.groupby('카테고리')
ggb = gb.sum()



out = ggb.sort_values(by = '출금',ascending=False)
print(out)
print(np.array(out.values).flatten())
