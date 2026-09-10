# 공경철 (Kyoungchul Kong) — 국내 웨어러블 재활로봇 권위자 리서치

> 리서치 노트 · 2026-09-10 · 작성: 김지민
> 왜 조사했나: 읽기 목록 1주차(Kong & Tomizuka 2009/2011)와 4주차(Shin·Ko·Kong 2026)가
> 모두 이 계보다. 2회차 발표의 "성능의 상한선" 축이자, 우리 스터디의 학문적 족보에 해당.

## 한 줄 요약

**보행 위상 인식(우리 3회차 주제)의 초기 고전을 쓴 연구자가, 그 기술을 20년에 걸쳐
국제대회 우승 로봇(워크온슈트)과 보험수가 받는 상용 제품(엔젤렉스)까지 끌고 간 사례.**
"측정 → 제어 → 임상 → 수가"의 전체 사다리를 혼자 다 밟았다.

## 경력 타임라인

| 시기 | 내용 |
|---|---|
| 2004 | 서강대 기계공학 B.Eng. + 물리학 B.S. (복수전공) |
| 2006 | 서강대 기계공학 M.S. |
| 2009 | **UC Berkeley 기계공학 Ph.D.** — 지도교수 Masayoshi Tomizuka. 학위논문 "Mechatronic Considerations for Human Assistive and Rehabilitation Systems" |
| 2009–2011 | UC Berkeley 포닥 |
| 2011–2018 | 서강대 조교수→부교수 |
| 2017 | **엔젤로보틱스 창업** (CEO/의장 겸임) |
| 2019– | **KAIST 기계공학과 교수** (EXO-Lab) |
| 2024.3 | 엔젤로보틱스 **코스닥 상장** (2024-03-26, LG전자 초기투자) |

## 연구 계보 — 우리 스터디와의 접점

### ① 초기: 보행 위상 인식 (버클리 시절, ~2009-2011)

- **Smart Shoes**: 신발에 공기압 센서를 넣어 발바닥 접지 패턴으로 보행을 모니터링
  — *A Gait Monitoring System Based on Air Pressure Sensor Embedded in a Shoe* (IEEE/ASME Trans. Mechatronics, 2009)
- 접지력 기반 **연속·부드러운 보행 위상 검출** (퍼지 로직) + 이상 보행 정량화
- 랩메이트 Bae와의 **HMM 기반 보행 위상 분석** (Bae & Tomizuka 2011, Mechatronics) ← **읽기 목록 1주차**
- **3회차 Fiaz 논문과의 대비**: 같은 문제(발바닥 센서로 위상 인식)를 15년 먼저,
  raw flatten이 아니라 **순차 구조를 명시적으로 모델링**(HMM)하는 방식으로 풀었다.
  우리가 "시간 순서를 버렸다"고 비판한 그 지점의 원조 해법.

### ② 중기: 구동기와 힘 제어

- **cRSEA(compact rotary series elastic actuator)** — 직렬 탄성 구동기의 소형화·토크 증폭
- 힘 모드 구동과 인간 의도 인식 (IEEE AIM 2008 최우수 학생논문상)
- 2회차에서 배운 "필요한 만큼만 보조"(안경 비유)의 기술적 뿌리가 이 힘 제어 계열

### ③ 현재: 두 갈래 전략

| 갈래 | 대상 | 제품/성과 |
|---|---|---|
| **성능의 상한선** (KAIST EXO-Lab) | 하반신 완전마비(ASIA-A) | 워크온슈트 시리즈(2015~). F1(2024)은 로봇이 **스스로 걸어와 착용**됨. 사이배슬론 2016 동메달 → 2020 금메달 → **2024 우승(디펜딩 챔피언)** |
| **현장의 보급** (엔젤로보틱스) | 재활 환자·일상 | 엔젤렉스 M20(병원 재활, **보험수가 획득 — 국내 병원 수익성 개선 확인**), 엔젤슈트 H10·K10(일상 보조), MEDI/GEAR/SUIT/KIT 4개 사업부. CE 인증 → 유럽 진출 추진 |
| 최신 연구 | 뇌졸중 임상 | Shin, Ko, **Kong** (2026) — 위상 궤적(phase portrait) 기반 보행 비대칭 지표 ← **읽기 목록 4주차** |

## 우리 랩에 주는 시사점

1. **1주차 발제 준비 맥락**: Kong & Tomizuka / Bae & Tomizuka를 읽을 때 "고전 HMM 논문"이
   아니라 **"현재 한국 재활로봇 산업의 출발점"**으로 읽어야 한다. 그 저자가 지금 KAIST에 있다.
2. **3회차 후속 논의**: Fiaz의 트리 앙상블 vs Kong 계보의 HMM — "순차 모델 vs 비순차 모델"
   비교(reading-list 실습 질문 3)가 곧 이 계보와의 대화다.
3. **수가 관점(research/notes의 보험수가 노트와 연결)**: 엔젤렉스 M20의 보험수가 획득은
   2회차에서 배운 HAL(일본 J118-4) 선례의 **국내 실현 사례**. "근거 → 수가 → 병원 도입"
   사다리가 한국에서도 작동함을 보여줌 — 우리 연구의 5~6단계(경제성·수가) 프레임에 실물 참조.
4. **잠재적 접점**: 랩장(조효성)이 2회차에서 워크온슈트 논문·엔젤 제품을 이미 다룸.
   사내 로봇 데이터 융합(1회차 2단계 로드맵)의 산업 파트너 지형에서 핵심 인물.

## 출처

- [Wikipedia — Kyoungchul Kong](https://en.wikipedia.org/wiki/Kyoungchul_Kong) (학력·경력·수상)
- [KAIST 뉴스 — 워크온슈트 F1 공개](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=40770) · [로봇신문](https://www.irobotnews.com/news/articleView.html?idxno=36433)
- [ZDNet — 사이배슬론 2024 우승](https://zdnet.co.kr/view/?no=20241024100135)
- [KAIST EXO-Lab — 엔젤로보틱스 코스닥 상장](https://robotics.kaist.ac.kr/bbs/board.php?bo_table=sub1_6&wr_id=65) · [아시아경제 — LG가 픽한 엔젤로보틱스](https://core.asiae.co.kr/article/2024013116295262393)
- [데일리인베스트 — M20 보험수가·해외 매출 전망](http://www.dailyinvest.kr/news/articleView.html?idxno=62869)
- [ResearchGate 프로필](https://www.researchgate.net/profile/Kyoungchul-Kong) · [KAIST Pure](https://pure.kaist.ac.kr/en/persons/kyoungchul-kong/)
- [NSF Award 0800501 — Smart Shoes and Smart Socks](https://www.nsf.gov/awardsearch/showAward?AWD_ID=0800501)

※ 세부 수치(수가 금액·매출 등)는 기사 기준이므로 인용 시 원출처 재확인.
