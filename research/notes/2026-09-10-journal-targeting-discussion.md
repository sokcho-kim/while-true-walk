# 목표 저널·연구 설계에 대한 외부 의견 검토

> 리서치 노트 · 2026-09-10 · 작성: 김지민
> 외부 AI 의견(Fiaz 논문은 벤치마크 연구일 뿐 모티브 논문으로 부적합, TNSRE/JNER급 설계로
> 다시 벤치마킹하라)을 우리 검산 결과와 대조해 취할 것/이견을 정리.

## 외부 의견 요지

1. Fiaz(2026)의 약점: 6명(건강 5:재활 1), 50% overlap window 단위 분할 → 낙관적 성능,
   **라벨 생성 센서(footswitch/pressure)가 입력 23채널에도 포함** → 일반화 근거 약함,
   전이 윈도우 제외, LOSO 없음. "97.9%를 넘는 것을 목표로 잡지 말라"
2. 목표 저널 기준점: **IEEE TNSRE / JNER / IEEE T-MRB** (1순위), **Gait & Posture**(관점 교정),
   J. Biomech, IEEE JBHI, npj Digital Medicine(최상위 도전)
3. Endpoint 사다리: Engineering(phase latency/error) → Biomechanical(cadence·symmetry·stride)
   → Clinical(10MWT·TUG·6MWT·FAC) → Real-world(사용시간·낙상·재활치료량)
4. 행동 지침: Applied Sciences 논문을 발전시키지 말고, TNSRE/JNER 최근 3~5년
   lower-limb wearable/gait rehab 논문 10~20편으로 **연구 설계 자체를 벤치마킹**하라

## 우리 검산과의 대조

### 독립적으로 동일 결론 (교차 검증됨)

| 외부 의견 | 우리 쪽 대응물 |
|---|---|
| window overlap 누수 | 슬라이드 "시험 문제 유출", explainer 6-1 (쌍둥이 토막) |
| 라벨 센서·입력 겹침 | explainer 2-2 "정답 재료가 문제지에" — ablation 부재 지적 |
| 전이 제외·LOSO 부재 | note.md 한계 §4.7 정리 |
| 97.9%는 벤치마크 아님 | "진짜 질문은 새 사람에게 몇 %냐" 프레이밍 |

### 우리가 더 나간 것 (외부 의견에 없음)

- **윈도우 수 내부 모순(64배)** — 논문 자체 수치의 산수 모순 (검산 ①)
- **원 데이터셋 라벨 기존재 + 실측** — 30% 파일·~3% 커버리지 (검산 ②·③).
  → 외부 의견의 "방법론 참고자료" 평가보다 정확한 판정 가능:
  relabeling은 실측으로 정당성까지 확인된 **재사용 부품**이다.

### 새로 취할 것

1. **Cohort 구성 비판 보강**: "6명"이 아니라 "건강 5 : 재활 1"이라는 구성 자체가
   임상 연구로서의 약점 — healthy-dominant cohort. note.md 한계에 반영할 것.
2. **저널 지형 채택 (조건부)**:
   - 랩 공식 목표는 학회(RehabWeek/ICORR·EMBC 2027) — 저널 조준 추가는 **랩장 논의 사항**
   - 실제 환자 모집이 어려운 여건상 JNER(임상 outcome 요구)은 장기, **1단계 현실적
     타깃은 TNSRE/JBHI류(공개 데이터+방법론)**
   - **Gait & Posture 관점은 즉시 채택 가능**: "정확도 몇 %"가 아니라 보행 지표
     (속도·variability·symmetry·10MWT/6MWT)의 변화를 묻는 outcome 설계 —
     [[2026-09-10-reimbursement-study-design]]의 endpoint 사다리와 정확히 합치
3. **exp01 위치 재정의**: Camargo split-낙차 실험은 목표 논문이 아니라
   **5주차 방법론 위생 훈련**. 학회/저널용 본 연구의 모티브는 별도 서베이에서 찾는다.

## 다음 리서치 태스크

- [ ] TNSRE/JNER/T-MRB/Gait & Posture 최근 3~5년 `lower-limb wearable / gait assistance /
  exoskeleton / gait rehabilitation` 논문 10~20편 수집 → 연구질문/대상자/장치/데이터/
  모델/endpoint/validation 비교표 → **모티브 논문 후보 선정** (reading-list 확장)
- [ ] note.md 한계에 healthy-dominant cohort 비판 한 줄 보강
- [ ] 랩장과 논의: 학회(현행) vs 저널(TNSRE 1순위) 조준, 그리고 endpoint를
  engineering에서 biomechanical/clinical로 올리는 로드맵
