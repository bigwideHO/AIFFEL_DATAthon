import pandas as pd

# 1. park.csv 파일에서 각 gu별로 park_area 평균값 계산
park_df = pd.read_csv("../dataset/park.csv", encoding="utf-8")

# 'gu'별 'park_area'의 평균값을 계산한 데이터프레임 생성
park_area_avg_by_gu = park_df.groupby("gu")["park_area"].mean().reset_index()
park_area_avg_by_gu.rename(columns={"park_area": "avg_park_area"}, inplace=True)

# 2. train_add__gu.csv 파일 불러오기
train_add__gu_df = pd.read_csv("../dataset/train_add__gu.csv", encoding="utf-8")

# train_add__gu.csv와 park_area_avg_by_gu 데이터를 'gu' 컬럼을 기준으로 병합
train_add__gu__park = pd.merge(
    train_add__gu_df, park_area_avg_by_gu, how="left", on="gu"
)

# 3. 'dong' 열 오른쪽에 평균 'park_area' 값을 추가
# 'park_area_avg_by_gu' 열을 'dong' 열 다음에 추가
train_add__gu__park["avg_park_area"] = (
    train_add__gu__park["avg_park_area"].fillna(0).astype(int)
)
train_add__gu__park.insert(
    train_add__gu__park.columns.get_loc("dong") + 1,
    "park_area_avg_by_gu",
    train_add__gu__park["avg_park_area"],
)

# 불필요한 'avg_park_area' 열 삭제 (병합 후 추가된 원본 컬럼)
train_add__gu__park = train_add__gu__park.drop("avg_park_area", axis=1)


# 결측치 확인
missing_values = train_add__gu__park.isnull().sum()
print("\n=== 결측치 확인 ===")
print(missing_values[missing_values > 0])

# 결측치가 있는 행 5개만 확인
if missing_values.any():
    print("\n=== 결측치가 있는 행 샘플 (5개) ===")
    print(train_add__gu__park[train_add__gu__park.isnull().any(axis=1)].head())

# 결과를 train_add__gu__park.csv로 저장
train_add__gu__park.to_csv(
    "../dataset/train_add__gu__park.csv", index=False, encoding="utf-8"
)

print("train_add__gu__park.csv 파일이 성공적으로 저장되었습니다.")
