# 5회차 스터디 가이드 — 재활 로봇·임상 논문 (일정·구성 확정 전 초안)

> 작성: 김지민 (공동랩장) · 랩장 docx 커리큘럼 4주차(재활 로봇 특화 문헌) 기준 초안.
> 4회차 임상 특강 결과에 따라 조정 예정.

## 이 회차의 위치

임상 특강(4회차)에서 "임상이 무엇을 요구하는가"를 들었다면, 이번엔 **그 요구를
로봇·공학 쪽에서 실제로 받아낸 논문들**을 읽는다. 기초 다지기의 마지막 —
다음 회차(Camargo 실습)부터는 우리 손을 움직인다.

## 읽을 논문 (docx 커리큘럼 4주차)

### 1. Zhang et al. (2021) — 재활 외골격의 다중정보 융합 위상 분류
*A multi-information fusion method for gait phase classification in lower limb
rehabilitation exoskeleton* (Front. Neurorobot., [10.3389/fnbot.2021.692539](https://doi.org/10.3389/fnbot.2021.692539))

읽으며 체크:
- Fiaz(3회차)와 같은 문제인데 **재활 외골격 제어**를 명시 타깃으로 한다 — 문제 설정이
  어떻게 달라지나? (실시간성? 위상 수? 전이 처리?)
- 검증 방식은 Fiaz보다 나은가 — subject-independent인가, window 분할인가 (**검산 습관 적용**)
- 융합하는 정보가 무엇이고, 우리 데이터(IMU 중심)로 재현 가능한 조합인가

### 2. Shin, Ko, Kong (2026) — 뇌졸중 보행 비대칭의 위상 궤적 지표
*Phase Portrait Based Index for Gait Asymmetry Assessment in Post-stroke Patients*
(J. Inst. Control Robot. Syst. 32(3))

읽으며 체크:
- **분류가 아니라 지표(index)** — "위상을 맞히는" 우리 관점과 "비대칭을 재는" 임상
  관점의 차이. 4회차 특강의 지표 논의와 연결
- 공경철 계보의 최신작 — [공경철 프로필 노트](../../../research/notes/2026-09-10-kong-kyoungchul-profile.md)
  의 계보(smart shoes→HMM→워크온슈트) 끝에 이 논문을 놓고 읽기
- 이 지표가 우리 본 실험의 **biomechanical endpoint 후보**가 될 수 있는가

## 곁들일 우리 자료 (10분)

- **MFDS 재활로봇 허가 지형** — A67080.01 32건 타임라인(2007 Lokomat → 2022 엔젤 M20
  → 2025 현대 sMEX), HAL 국내 미진입. "우리가 읽는 논문들의 장치가 국내 제도에서
  어디에 있는가"를 실물로: [지형 노트](../../../research/notes/2026-09-10-mfds-rehab-robot-landscape.md)
- 모티브 논문 서베이 요약 — 상위 저널 공통 문법 5가지 (환자 cohort·LOSO·연속 위상·
  endpoint 사다리·device-in-loop): [서베이](../../../research/notes/2026-09-10-motive-paper-survey.md)

## 토론 안건

1. **투고 타깃 확정** (로드맵 결정 1번): 학회(RehabWeek/ICORR·EMBC, 현행 목표) vs
   저널(TNSRE 1순위) — 마감 역산이 10월 이후 전체 일정을 정하므로 이번에 결정 권장
2. 본 실험의 위상 정의: 이산 3클래스 vs 연속 위상 회귀 (서베이 결론은 후자가 주류)
3. 6회차 Camargo 킥오프 준비: 데이터 다운로드 분담, exp01 역할

---
*초안입니다 — 4회차 진행 결과와 발제자 확정에 따라 갱신.*
