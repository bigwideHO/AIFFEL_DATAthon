# AIFFEL 9기 DATAthon

## 목차
- [AIFFEL 9기 DATAthon](#aiffel-9기-datathon)
  - [목차](#목차)
  - [팀 정보](#팀-정보)
  - [팀 과제: 아파트 실거래가 예측](#팀-과제-아파트-실거래가-예측)
    - [자료](#자료)
    - [💡'아파트 실거래가 예측' 과제 수행팀 주요 전달사항](#아파트-실거래가-예측-과제-수행팀-주요-전달사항)
    - [아파트 실거래가 예측 AI 경진대회 평가 기준](#아파트-실거래가-예측-ai-경진대회-평가-기준)
      - [코드 검증 절차(모델 검증)](#코드-검증-절차모델-검증)
    - [LMS 노드 제공 정보](#lms-노드-제공-정보)
      - [**배경**](#배경)
      - [**주제**](#주제)
      - [**데이터셋**](#데이터셋)
      - [**train.csv, test.csv**](#traincsv-testcsv)
      - [**park.csv**](#parkcsv)
      - [**day\_care\_center.csv**](#day_care_centercsv)
      - [과업](#과업)
      - [규칙](#규칙)
      - [평가 기준](#평가-기준)

## 팀 정보

- 팀명: 구해줘! 톤즈
- 팀장: 최성호
- 팀원: 김지혜, 민혁, 임만순

## 팀 과제: 아파트 실거래가 예측

### 자료

- 공지글: [9기 DATAthon (9기생 전용 링크)](https://www.notion.so/9-DATAthon-aaf543f5d9534382a4fd3d4b57e6b582?pvs=21)
- 데이터셋: [아파트 실거래가 예측 AI 경진대회](https://dacon.io/competitions/official/21265/overview/rules)

### 💡'아파트 실거래가 예측' 과제 수행팀 주요 전달사항

- train_test_split 시 random_state값은 9, test_size는 default(0.25)로 설정
- 모든 팀이 같은 환경에서 모델 성능을 확인하기 위해 통일

### 아파트 실거래가 예측 AI 경진대회 평가 기준

제출한 예측 결과물은 Root Mean Squared Error(RMSE)로 평가합니다. (평가는 게시된 데이터셋만을 기준으로 합니다).

#### 코드 검증 절차(모델 검증)

1. Pre-Processing for Data Cleaning
2. Feature Engineering and Variable Selection
3. Model Selection and Regularization
4. Optimization Processing

### LMS 노드 제공 정보

[Datathon_CR9 2. 아파트 실거래가 예측 (9기생 전용 링크)](https://lms.aiffel.io/course/1046/node/1963/step/10743/readonly)

**오늘의 데이터톤 주제는 아파트 실거래가 예측입니다. 자세하게 살펴보고 멋진 프로젝트를 완성해보세요!!!**

#### **배경**

**통계청 2015년 자료에 의하면 (<https://bit.ly/2SFyzMA>) 일반적인 한국인의 절반은 48.1%는 아파트에 살고 있습니다.** 그들은 아파트 주거 선호도가 매우 높습니다. 또한 부의 증식 수단으로 생각 하기 때문에 아파트 가격에 관심이 많습니다.

이번 대회의 데이터 제공자는 직방입니다. **직방은 부동산 정보의 비대칭성과 불투명성을 해소하기 위해 노력하며,** 중개사와 구매자를 연결하여 부동산정보 서비스 시장의 신뢰도를 높이는데 기여합니다.

**최근 매물 가격 정보는 직방, 다음부동산, 네이버부동산에서 볼 수 있습니다.** 하지만 최근 매물 가격은 아직 거래되지 않아 정확하지 않은 정보일 수 있습니다.

**이에 따라, 본 대회는 실 거래가와 아파트, 학교, 지하철역 정보를 제공하며,** 아파트 구매자들의 비대칭성 정보를 해결하기 위해 미래의 실 거래가 예측을 목표로 합니다.

// 지하철역 정보는 미제공

#### **주제**

**서울/부산 지역 아파트 실 거래가를 예측하는 모델 개발**

#### **데이터셋**

**해당 데이터를 토대로 자유로운 결과를 추론해주세요.**

약 1,600,000여개의 실거래 데이터, 아파트 거래일, 지역, 전용면적, 공급면적 등의 정보가 제공됩니다.

국토교통부 실거래가 공개시스템([http://rt.molit.go.kr/)과](http://rt.molit.go.kr/)%EA%B3%BC) 같은 법적인 제약이 없는 외부 데이터(공공 데이터) 사용이 가능합니다.

#### **train.csv, test.csv**

```markdown
1. apartment_d - 아파트 아이디
2. city - 도시
3. dong - 동
4. jibun - 지번
5. apt - 아파트 단지 이름
6. addr_kr - 주소
7. exclusive_use_area - 전용면적
8. year_of_completion - 설립일자
9. transaction_year_month - 거래년월
10. transaction_date - 거래날짜
11. floor - 층
12. transaction_real_price - 실거래가(train만 존재)
```

#### **park.csv**

```markdown
1. city - 도시
2. gu - 구
3. dong - 동
4. park_name - 공원이름
5. park_type - 공원 종류
6. park_area - 공원의 넓이
7. park_exercise_facility - 공원보유 운동시설
8. park_entertainment_facility - 공원보유 유희시설
9. park_benefit_facility - 공원보유 편익시설
10. park_cultural_tacitiy - 공원보유 교양시설
11. park facility-other - 공원보유 기타시설
12. park_open_year - 공원 개장년도
13. reference_date - 데이터 기준일자(해당 데이터가 기록된 일자)
```

#### **day_care_center.csv**

```markdown
1. city - 도시
2. gu - 구
3. day_care_name - 어린이집 이름
4. day-care_type - 어린이집 종류
5. day_care_baby_num - 정원수
6. teacher_num - 보육교직원수
7. nursing_room_num - 보육실수
8. playground_num - 놀이터수
9. CCTV_num - CCTV 설치수
10. is_commuting-vehicle - 통학차량 운영여부
11. reference_date - 데이터 기준일자(해당 데이터가 기록된 일자)
```

#### 과업

해당 데이터를 토대로 자유로운 결과를 추론해주세요.

#### 규칙

- 프로젝트 제출 기한내 LMS의 프로젝트 제출 스텝에서 결과 노트북의 링크를 제출해주세요.
- 프로젝트 제출 스텝의 루브릭을 따라 노트북의 내용을 채워주세요.
- 외부 데이터 활용은 허용하되, 제공된 데이터를 활용한 기록이 필수적으로 포함되어야 합니다.
- 부정 제출 행위를 금지하고 있으며, 부정 제출 이력이 있는 경우 평가가 제한됩니다.

#### 평가 기준

1. 데이터에 알맞는 분석 도구를 선택하고 그 이유가 적절한가?
2. 데이터 분석 결과를 올바르게 해석하고 명료하게 정리하였는가?
3. 인사이트를 도출해내는 과정이 논리적인가?
4. 말하는 내용이 시각화 등을 통해 직관적으로 표현되어있는가?
5. 도출된 결론이 충분한 설득력이 있는가?
6. 발표가 매끄럽게 진행되었고 발표시간을 준수하였는가?
