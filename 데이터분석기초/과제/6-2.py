import pandas as pd
file_path = 'data/data.csv' # 파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
f = df.iloc[7:18].copy() # copy를 이용해서 복사본을 만들고 수정을 해야 SettingWithCopyWarning이 일어나지 않는다.
f.drop('성별',axis=1, inplace=True) # iloc과 다르게 drop은 반환값이 None이다.
########################
print(f)

# .copy()를 사용하지 않으면 f를 수정할 때 df 자체가 수정될 수 있다.
# True인 경우에는 원본을 직접 수정, 반환값은 None이 되고 
# False인 경우에는 수정된 새로운 객체를 반환, 원본은 유지하게 된다.
# inplace를 적지 않을 경우 false가 출력된다.

#import pandas as pd 아래의 방법이나 .copy를 이용하자.
pd.options.mode.chained_assignment = None  # 경고 끄기
