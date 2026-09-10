# while-true-walk

웨어러블 재활로봇에서 생성되는 보행 데이터를 AI로 분석하여 임상적 의미를 만드는 연구.
모두의연구소 **WalkAI LAB** (2026-08 ~ 2027-02) · 목표: 공개 데이터셋 기반 분석 파이프라인 구축 → 해외 학회 투고 (RehabWeek/ICORR·IEEE EMBC 2027)

## 구조

```
ROADMAP.md  4회차 이후 계획 (26주 여정 × 커리큘럼 매핑)
study/      스터디 트랙 — 회차별 발표자료·논문 리뷰·읽기 목록
research/   연구 트랙 — 실험 코드·리서치 노트·데이터
```

### study/

- `sessions/` — 회차별 발표자료
  - `01-domain/` 1회차 도메인 특강 (보행주기 8단계·시공간 파라미터·이상보행·평가지표)
  - `02-wearable-robots/` 2회차 웨어러블 로봇 (지형도·센서·개인차·데이터)
- `papers/` — 논문 리뷰 (폴더당 논문 하나: 노트 → 해설 → 슬라이드 → 검산)
  - `2026-08-25-fiaz-gait-phase-detection/` 3회차: gait phase detection 비판 리뷰
    + Zafar 데이터셋 실측 검산 (`verify/audit.ipynb`)
- `reading-list.md` — 추천 논문 7편 + 5주 커리큘럼

### research/

- `notes/` — 리서치 노트 (연구설계·정책·RWE 등)
- `experiments/` — 실험 코드·결과 (5주차 Camargo 실습부터)
- `data/` — 원시 데이터 (커밋 금지, 다운로드 방법은 폴더 README)

## 진행 중인 질문

> Fiaz et al. (2026)의 97.9%는 윈도우 누수 위의 상한선이었다.
> **"처음 보는 환자에게 채우면 몇 %인가?"** — Camargo 2021(22명)에서
> subject-wise vs window-wise split으로 직접 잰다. (`research/experiments/`)

## 컨벤션

- 논문 리뷰 폴더: `study/papers/YYYY-MM-DD-슬러그/` (읽기 시작일)
- 발표자료는 md가 정본, pptx는 산출물
- 논문 수치는 요약하지 말고 **검산**한다 — 검산 코드는 해당 논문 폴더 `verify/`에 노트북으로
