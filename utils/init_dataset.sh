#!/bin/bash

# 컬러 설정
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # 기본 색상

# 첫 번째 단계: train.csv 파일 확인 및 압축 해제
echo -e "\033[1;34m💡 Checking and initializing dataset...\033[0m"

# train.csv가 없으면 train.csv.zip 압축 해제
if [ ! -f "../dataset/train.csv" ]; then
  echo -e "\033[0;33m🔍 train.csv 파일이 존재하지 않습니다. 압축 해제 중...\033[0m"
  unzip ../dataset/train.csv.zip -d ../dataset/
else
  echo -e "\033[0;32m✅ train.csv 파일이 이미 존재합니다.\033[0m"
fi

# 첫 번째 Python 스크립트 실행
echo -e "\033[1;34m💡 Running 1_add_gu__to__train_by_open_data.py...\033[0m"
python3 1_add_gu__to__train_by_open_data.py

# 첫 번째 스크립트가 성공적으로 실행되었는지 확인
if [ $? -ne 0 ]; then
  echo -e "\033[0;31m🚨 1_add_gu__to__train_by_open_data.py 실행 중 오류 발생!\033[0m"
  exit 1
else
  echo -e "\033[0;32m✅ 1_add_gu__to__train_by_open_data.py 성공!\033[0m"
fi

# 두 번째 Python 스크립트 실행
echo -e "\033[1;34m💡 Running 2_add_park_area__to__train_add__gu.py...\033[0m"
python3 2_add_park_area__to__train_add__gu.py

# 두 번째 스크립트가 성공적으로 실행되었는지 확인
if [ $? -ne 0 ]; then
  echo -e "\033[0;31m🚨 2_add_park_area__to__train_add__gu.py 실행 중 오류 발생!\033[0m"
  exit 1
else
  echo -e "\033[0;32m✅ 2_add_park_area__to__train_add__gu.py 성공!\033[0m"
fi

# 세 번째 Python 스크립트 실행
echo -e "\033[1;34m💡 Running 3_add_day_care_count__to__train_add__gu__park.py...\033[0m"
python3 3_add_day_care_count__to__train_add__gu__park.py

# 세 번째 스크립트가 성공적으로 실행되었는지 확인
if [ $? -ne 0 ]; then
  echo -e "\033[0;31m🚨 3_add_day_care_count__to__train_add__gu__park.py 실행 중 오류 발생!\033[0m"
  exit 1
else
  echo -e "\033[0;32m✅ 3_add_day_care_count__to__train_add__gu__park.py 성공!\033[0m"
fi

echo -e "\033[0;32m😄 모든 스크립트가 성공적으로 실행되었습니다!\033[0m"
