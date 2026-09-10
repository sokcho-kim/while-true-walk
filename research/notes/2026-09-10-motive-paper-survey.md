# 모티브 논문 서베이 (1차) — TNSRE/JNER급 연구 설계 벤치마킹

> 리서치 노트 · 2026-09-10 · 작성: 김지민
> 목적: [[2026-09-10-journal-targeting-discussion]]의 후속 — "Fiaz를 발전시키지 말고
> 상위 저널의 최근 설계를 벤치마킹하라"에 따른 후보 수집. **1차 = 웹 서베이 기반 후보
> 10편**; 저널·연도·상세는 원문 확인 전이므로 ⚠ 표시 항목은 인용 전 검증 필수.

## 선정 기준 (Fiaz의 약점을 하나씩 깨는 논문)

`6명 → 환자 cohort` · `window 누수 → LOSO/신규 피험자 검증` · `오프라인 분류 → 실기기
실시간` · `정확도 endpoint → 생체역학·임상 endpoint`

## Tier A — 방법론: 위상 추정을 "제대로 검증"한 논문

| # | 논문 | 핵심 | Fiaz 대비 무엇을 깨나 |
|---|---|---|---|
| 1 | **Real-Time Gait Phase and Task Estimation for Controlling a Powered Ankle Exoskeleton on Extremely Uneven Terrain** (IEEE TNSRE 2023) [링크](https://ieeexplore.ieee.org/iel7/8860/10144918/10024512.pdf) | 실기기(발목 외골격)·실시간·험지 — 위상 추정이 제어 루프 안에서 평가됨 | 오프라인 분류 → **device-in-the-loop** |
| 2 | ⚠ Lee et al., **Continuous gait phase estimation using LSTM for robotic transfemoral prosthesis across walking speeds** (TNSRE 2021) | 이산 분류가 아니라 **연속 위상(0~100%)** 회귀, 속도 변화 강건성 | 3클래스 이산 → 연속 위상 + 속도 일반화 (우리 "1.28초 고정 토막" 비판의 해법) |
| 3 | ⚠ Hong et al., **Piecewise Linear Labeling for Speed-Adaptability in Gait Phase Estimation** (TNSRE 2023) | 라벨 정의 자체를 속도 적응형으로 — 라벨링 방법론 논문 | mid-swing "시간 20~25%" 임의 정의 → 원리 있는 라벨 |
| 4 | **IMU-Based Real-Time Estimation of Gait Phase Using Multi-Resolution NN** (Sensors 2024) [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11054798/) — *읽기 목록 3주차와 동일* | 16명, 0.1~1.9 m/s, one-subject-out + 조건 제외 통계검정 | **LOSO + condition-independent** 검증 설계의 교본 |
| 5 | ⚠ **Abnormal Gait Phase Recognition and Limb Angle Prediction in Lower-Limb Exoskeletons** (2025) [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12467789/) | 정상 아닌 **병적 보행**의 위상 인식 + 각도 예측 | healthy-dominant → 병적 보행 대상 |

## Tier B — 임상: 장치 효과를 임상 endpoint로 증명한 논문

| # | 논문 | 핵심 | 왜 참고 |
|---|---|---|---|
| 6 | **Efficacy of Wearable Exoskeleton for Gait Recovery in Patients With Stroke: Multicenter RCT** (Stroke, 2026) [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12928783/) | 아급성 뇌졸중 다기관 RCT — 보행기능에서 기존 재활 대비 **우월성 입증 실패**, 하지 운동기능은 추가 개선 | 임상 endpoint 설계 + "안 되는 것도 정직하게"의 모범. 2회차 코크란 결론과 합치 |
| 7 | ⚠ **Real-time assistive hip-wearable exoskeleton based on motion prediction, single-blinded RCT** (2025) [PubMed](https://pubmed.ncbi.nlm.nih.gov/41023973/) | 아급성 뇌졸중, 의도 예측 기반 고관절 보조 — 보행·균형 개선 | **"위상/의도 추정 → 보조 → 임상 개선"** 전체 사다리를 한 편에 담은 최신 설계 |
| 8 | Awad, Walsh et al., **A soft robotic exosuit improves walking in patients after stroke** (Science Translational Medicine 2017) [링크](https://www.science.org/doi/10.1126/scitranslmed.aai9084) | 소프트 엑소수트가 편마비 보행의 **추진 비대칭·발끝 클리어런스·대사 비용** 개선 | 생체역학 endpoint의 고전. ReStore(FDA 2019)의 근거 논문 계보 |
| 9 | ⚠ **Effects of Bilateral Assistance for Hemiparetic Gait Post-Stroke Using a Powered Hip Exoskeleton** (2022) [PubMed](https://pubmed.ncbi.nlm.nih.gov/35963920/) | 양측 고관절 보조 — 추진 대칭엔 효과 적고 스윙 개시·발목 일 대칭 개선 | 관절 부위별 보조 전략의 효과 차이 — endpoint 선택이 결론을 바꾼다는 실례 |

## Tier C — 측정·평가: IMU + ML을 임상 지표로 연결

| # | 논문 | 핵심 | 왜 참고 |
|---|---|---|---|
| 10 | **Identifying key gait features in stroke patients using wearable IMU + supervised/unsupervised ML** (Sci Rep 2026) [링크](https://www.nature.com/articles/s41598-026-43666-7) | 뇌졸중 보행의 판별 특징 선택(9개) + 해석 가능성 | "정확도"가 아니라 **어떤 특징이 임상적으로 판별력 있나** — Gait & Posture식 관점 |
| + | **IMU-based quantitative assessment of stroke from gait** (Sci Rep 2025) [링크](https://www.nature.com/articles/s41598-025-94167-y) / PD 중증도 예측 (XGBoost·SVM) [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12370646/) | 보행 → 임상 척도 점수 예측 | 랩 장기 방향(회복을 숫자로 증명)에 근접 |

## 종합 — 상위 저널 설계의 공통 문법

1. **대상**: 건강인 벤치마크가 아니라 **환자 cohort** (뇌졸중 편마비가 지배적)
2. **검증**: LOSO/신규 피험자 + 조건 일반화가 기본값. window-wise 분할은 안 보임
3. **위상**: 이산 3클래스가 아니라 **연속 위상 회귀**가 주류 (속도 강건성 확보 수단)
4. **평가**: 정확도 → **latency·연속 위상 RMSE**(공학) → **추진 대칭·클리어런스·대사**(생체역학)
   → **10MWT·6MWT·FAC·균형**(임상) 사다리
5. **장치**: 추정기가 논문의 끝이 아니라 **제어 루프의 입력** — device-in-the-loop 평가

→ 우리 exp01(Camargo split 낙차)은 이 문법의 2번을 체득하는 훈련.
본 연구 설계는 **3(연속 위상)·4(endpoint 사다리)** 를 어디까지 가져갈지가 랩장 논의 핵심.

## 다음 단계

- [ ] ⚠ 표시 5편 원문 확보·서지 확정 (Lee/Hong TNSRE, hip-RCT, bilateral-hip, abnormal-phase)
- [ ] 각 편을 리뷰 5단계 템플릿으로 1페이지 요약 → `study/papers/`에 축적
- [ ] 랩 공유: Tier B 6·7번은 4주차(임상 확장) 발제 후보로 제안
