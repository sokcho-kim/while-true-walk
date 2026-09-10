# 데이터 (커밋 금지)

원시 데이터는 이 폴더에 두되 git에 올리지 않는다 (.gitignore 처리).

| 데이터셋 | 용도 | 받는 곳 |
|---|---|---|
| Zafar — Dataset.zip (2.0 GB) | Fiaz 2026 검산 (`study/papers/2026-08-25-fiaz-gait-phase-detection/verify/audit.ipynb`) | https://ndownloader.figshare.com/files/33417746 |
| Camargo 2021 (Georgia Tech EPIC Lab) | 5주차 실습·본 실험 | https://doi.org/10.1016/j.jbiomech.2021.110320 (논문 내 링크) |

주의: Zafar zip은 HP117 폴더가 `DAQ_HP116/` 안에 중첩돼 있고, CSV에 NUL 문자·비정상 개행이 섞여 있다 (audit.ipynb에 처리 포함).
