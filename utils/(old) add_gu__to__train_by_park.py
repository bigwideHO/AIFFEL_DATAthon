import pandas as pd

# 1. park.csv 데이터 불러오기
park_df = pd.read_csv('../dataset/park.csv', encoding='utf-8')

# park.csv에서 'city', 'dong', 'gu' 정보만 추출하여 딕셔너리로 매핑
gu_mapping = park_df[['city', 'dong', 'gu']].drop_duplicates().set_index(['city', 'dong'])['gu'].to_dict()

# 2. train.csv 데이터 불러오기
train_df = pd.read_csv('../dataset/train.csv', encoding='utf-8')

# 3. 'city'와 'dong'을 기반으로 'gu'를 매핑하여 train.csv에 추가
train_df['gu'] = train_df.apply(lambda row: gu_mapping.get((row['city'], row['dong'])), axis=1)

# 4. 'gu' 열을 'city' 열 다음에 삽입
train_df.insert(train_df.columns.get_loc('city') + 1, 'gu', train_df.pop('gu'))

# 5. 결과를 train_add_gu.csv로 저장
train_df.to_csv('../dataset/train_add_gu.csv', index=False, encoding='utf-8')

# 6. 결측치 확인
missing_values = train_df.isnull().sum()
print("\n=== 결측치 확인 ===")
print(missing_values)
