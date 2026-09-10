# 실험

## 예정 — exp01: split 방식에 따른 gait phase 성능 낙차 (5주차 실습)

Fiaz 2026 리뷰의 후속 질문: **"누수 없는 피험자 분할에서 97.9%는 몇 %가 되는가?"**

- 데이터: Camargo 2021 (22명) — Zafar(6명) 대신 표준 벤치마크 사용
- 비교: window-wise split (논문 방식, 누수 있음) vs trial-wise vs subject-wise(LOSO)
- 부가: raw flatten(2944차원) vs 통계 특징, 발바닥 채널 제외 ablation
- 산출: 노트북 + 결과 표. 학회 투고의 첫 실험 후보
