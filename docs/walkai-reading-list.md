# WalkAI 보행분석·재활로봇 스터디 논문 목록

> 출처: 랩 공유 문서 `WalkAI_보행분석_재활로봇_스터디_논문목록.docx` (2026-09-09 수령).
> Fiaz et al. (2026) 리뷰에서 지적된 한계(윈도우 누수, subject-independent 부재,
> raw flatten ablation 부재, 소표본)를 보완하는 대안 문헌·데이터셋 목록.

## 비교 기준 논문

- Fiaz, Guido, Conforti (2026). *Machine Learning Models for Reliable Gait Phase Detection Using Lower-Limb Wearable Sensor Data.* Appl. Sci. 16(3), 1397. [10.3390/app16031397](https://doi.org/10.3390/app16031397) — [내 노트](../papers/2026-08-25-gait-phase-detection/note.md)

## 추천 문헌

| # | 문헌 | 분류 | 추천 이유 |
|---|------|------|-----------|
| 1 | Camargo, Ramanathan, Flanagan, Young (2021). *A comprehensive, open-source dataset of lower limb biomechanics…* J. Biomech. [10.1016/j.jbiomech.2021.110320](https://doi.org/10.1016/j.jbiomech.2021.110320) | 공개 데이터셋 | 22명, 평지·계단·경사·전환. IMU/EMG/관절각/모캡/force plate. 코드·튜토리얼 제공(GT EPIC Lab). 사실상 표준 벤치마크 |
| 2 | Young & Hargrove (2016). *A classification method for user-independent intent recognition for transfemoral amputees…* IEEE TNSRE. [10.1109/TNSRE.2015.2412461](https://doi.org/10.1109/TNSRE.2015.2412461) | subject-independent | 사용자 독립 의도 인식의 gold standard (Hargrove 랩) |
| 3 | *IMU-Based Real-Time Estimation of Gait Phase Using Multi-Resolution Neural Networks.* Sensors (2024). PMC11054798 | subject-independent | 16명, 속도 0.1~1.9 m/s + 비대칭·급정지. one-subject-out CV + 조건 제외 통계검정(KS) |
| 4 | Zhang, Cao, Ling 외 (2021). *A multi-information fusion method for gait phase classification in lower limb rehabilitation exoskeleton.* Front. Neurorobot. [10.3389/fnbot.2021.692539](https://doi.org/10.3389/fnbot.2021.692539) | 재활 로봇 | 재활 외골격 명시 타겟 |
| 5 | Bae & Tomizuka (2011). *Gait phase analysis based on a Hidden Markov Model.* Mechatronics 21(6). [10.1016/j.mechatronics.2011.03.003](https://doi.org/10.1016/j.mechatronics.2011.03.003) (관련: Kong & Tomizuka 2009) | 고전/HMM | 공경철 교수 계보 초기 연구. 순차 상태 전이의 명시적 모델링 |
| 6 | Shin, Ko, Kong (2026). *Phase Portrait Based Index for Gait Asymmetry Assessment in Post-stroke Patients.* J. Inst. Control Robot. Syst. 32(3) | 임상 | KAIST EXO-Lab 최신. 뇌졸중 보행 비대칭의 위상 궤적 지표 |
| 7 | *A Review of Gait Phase Detection Algorithms for Lower Limb Prostheses.* Sensors (2020). PMC7411778 | 리뷰 | 알고리즘 전반(HMM~CNN) 비교, 입문용 |

## 5주 커리큘럼

1. Kong & Tomizuka (2009/2011) — HMM 고전
2. **Fiaz et al. (2026) 비판적 리뷰** ← 2026-09-09 발제 완료 ([slides](../papers/2026-08-25-gait-phase-detection/slides.md))
3. Young & Hargrove (2016) + Sensors (2024) — subject-independent 설계
4. Zhang (2021), Shin/Ko/Kong (2026) — 재활 로봇·임상
5. Camargo (2021) 데이터셋 자체 실험 — subject-wise vs window-wise split, raw flatten vs 통계 특징, HMM vs 트리 앙상블

※ DOI·서지는 문서 작성 시점 기준 — 접근 전 재확인 (원문 주의사항).
