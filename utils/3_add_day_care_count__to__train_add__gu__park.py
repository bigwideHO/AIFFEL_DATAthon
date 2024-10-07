import pandas as pd

# 1. day_care_center.csv 파일에서 각 city, gu별 어린이집 개수 계산
day_care_df = pd.read_csv('../dataset/day_care_center.csv', encoding='utf-8')

# 'city'와 'gu'별 'day_care_name'의 개수를 계산한 데이터프레임 생성
day_care_count_by_city_gu = day_care_df.groupby(['city', 'gu'])['day_care_name'].count().reset_index()
day_care_count_by_city_gu.rename(columns={'day_care_name': 'day_care_count'}, inplace=True)

# 2. train_add__gu__park.csv 파일 불러오기
train_add__gu__park_df = pd.read_csv('../dataset/train_add__gu__park.csv', encoding='utf-8')

# train_add__gu__park.csv와 day_care_count_by_city_gu 데이터를 'city'와 'gu' 컬럼을 기준으로 병합
train_add__gu__park__day_care = pd.merge(train_add__gu__park_df, day_care_count_by_city_gu, how='left', on=['city', 'gu'])

# 'day_care_count' 열의 결측치를 0으로 채우고 int로 변환
train_add__gu__park__day_care['day_care_count'] = train_add__gu__park__day_care['day_care_count'].fillna(0).astype(int)

# 3. 'day_care_count' 열을 'park_area_avg_by_gu' 열 다음에 위치시키기
day_care_index = train_add__gu__park__day_care.columns.get_loc('park_area_avg_by_gu') + 1
train_add__gu__park__day_care.insert(day_care_index, 'day_care_count', train_add__gu__park__day_care.pop('day_care_count'))

# 결측치 확인
missing_values = train_add__gu__park__day_care.isnull().sum()
print("\n=== 결측치 확인 ===")
print(missing_values[missing_values > 0])

# 결측치가 있는 행 5개만 확인
if missing_values.any():
    print("\n=== 결측치가 있는 행 샘플 (5개) ===")
    print(train_add__gu__park__day_care[train_add__gu__park__day_care.isnull().any(axis=1)].head())

# 결과를 train_add__gu__park__day_care_count.csv로 저장
train_add__gu__park__day_care.to_csv('../dataset/train_add__gu__park__day_care_count.csv', index=False, encoding='utf-8')

print("train_add__gu__park__day_care_count.csv 파일이 성공적으로 저장되었습니다.")
