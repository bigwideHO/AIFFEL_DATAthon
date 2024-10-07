import pandas as pd

# train.csv 데이터 불러오기
train_df = pd.read_csv("../dataset/train.csv", encoding="utf-8")

# 국토교통부 법정동 코드 데이터 불러오기
korea_land_df = pd.read_csv(
    "../dataset/국토교통부_전국 법정동_20240802.csv", encoding="utf-8"
)

# '삭제일자'가 있는 행 제거 (삭제된 항목을 제외)
korea_land_df = korea_land_df[korea_land_df["삭제일자"].isna()]

# 필요없는 컬럼 제거 (시도명, 순위, 생성일자, 삭제일자, 과거법정동코드 제거)
korea_land_df = korea_land_df[["시도명", "시군구명", "읍면동명"]]

# 중복된 '읍면동명'과 '시도명'에 대해 첫 번째 값만 남기고 제거
korea_land_df = korea_land_df.drop_duplicates(subset=["시도명", "읍면동명"])


# train.csv의 'dong' 열에서 ' '로 split하여 첫 번째 단어만 가져오는 함수
def extract_dong(dong):
    return dong.split(" ")[0]  # 공백을 기준으로 첫 번째 부분만 반환


# train.csv의 'dong' 컬럼을 처리하여 'dong_extracted' 열로 저장
train_df["dong_extracted"] = train_df["dong"].apply(extract_dong)

# 'dong_extracted' 컬럼과 korea_land_df의 '읍면동명' 컬럼을 이용하여 매칭
train_df = pd.merge(
    train_df,
    korea_land_df[["시도명", "시군구명", "읍면동명"]],
    how="left",
    left_on=["city", "dong_extracted"],
    right_on=["시도명", "읍면동명"],
)

# 'gu' 열을 'city' 열 다음에 추가
train_df.insert(
    train_df.columns.get_loc("city") + 1, "gu", train_df["시군구명"]
)

# 불필요한 컬럼 삭제 (병합 과정에서 추가된 컬럼 삭제)
train_df = train_df.drop(
    ["시도명", "시군구명", "읍면동명", "dong_extracted"], axis=1
)

# 결측치 확인 코드
missing_values = train_df.isnull().sum()

# 결측치가 있는 열만 필터링하여 출력
missing_values = missing_values[missing_values > 0]

# 결측치 여부에 따라 문구 출력
if missing_values.empty:
    print("결측치가 없습니다.")
else:
    print("=== 결측치가 있는 열 및 결측치 개수 ===")
    print(missing_values)

    # 결측치가 있는 행 필터링
    missing_rows = train_df[train_df.isnull().any(axis=1)]
    # 결측치가 있는 행 5개만 출력
    print(missing_rows.head(5))

# 결과를 train_add__gu.csv로 저장
train_df.to_csv("../dataset/train_add__gu.csv", index=False, encoding="utf-8")

print("train_add__gu.csv 파일이 성공적으로 저장되었습니다.")
