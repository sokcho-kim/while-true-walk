#!/usr/bin/env python3
"""식약처 의료기기 품목허가 OpenAPI 수집기 — 재활로봇 리서치용.

데이터: 공공데이터포털 "식품의약품안전처_의료기기 품목허가 정보"
  https://www.data.go.kr/data/15057456/openapi.do
엔드포인트(키 없이 경로 실재 확인됨, 2026-09-10):
  https://apis.data.go.kr/1471000/MdeqPrdlstInfoService02/getMdeqPrdlstInfoInq02

사용:
  export MFDS_API_KEY='발급받은 인증키(Decoding 키)'
  python fetch_devices.py                          # 기본 키워드 세트로 수집
  python fetch_devices.py --keywords 보행 외골격     # 키워드 지정
  python fetch_devices.py --keywords 엔젤 --param entp_name=엔젤로보틱스
  python fetch_devices.py --probe                  # 키·파라미터 동작 확인(1건)

표준 라이브러리만 사용. 결과는 ../../data/mfds/ 에 JSONL(원본)과 CSV(요약)로 저장.
"""
import argparse, csv, json, os, sys, time, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://apis.data.go.kr/1471000/MdeqPrdlstInfoService02/getMdeqPrdlstInfoInq02"
OUT_DIR = Path(__file__).resolve().parents[2] / "data" / "mfds"
# 재활로봇 리서치 기본 키워드 (품목명 기준 부분일치 검색)
DEFAULT_KEYWORDS = ["보행", "재활", "외골격", "착용", "로봇", "운동장치"]
NUM_ROWS = 100
SLEEP = 0.4  # 초당 호출 제한 대비


def call(params: dict) -> dict:
    q = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    url = f"{BASE}?{q}"
    with urllib.request.urlopen(url, timeout=30) as r:
        body = r.read().decode("utf8", errors="replace")
    if body.lstrip().startswith("<"):
        # 오류는 XML로 옴 (SERVICE_KEY_IS_NULL 등)
        raise RuntimeError(f"API가 XML을 반환(오류 가능): {body[:300]}")
    return json.loads(body)


def items_of(data: dict):
    """응답 구조 {header, body:{items:[{item:{...}}] | [...]}} 방어적 파싱."""
    body = data.get("body") or data.get("response", {}).get("body") or {}
    items = body.get("items") or []
    if isinstance(items, dict):
        items = items.get("item") or []
    if isinstance(items, dict):
        items = [items]
    out = []
    for it in items:
        out.append(it.get("item", it) if isinstance(it, dict) else it)
    total = body.get("totalCount") or body.get("total_count") or 0
    return out, int(total)


def fetch_keyword(key: str, keyword: str, extra: dict, max_pages: int):
    rows, page = [], 1
    while page <= max_pages:
        params = {"serviceKey": key, "type": "json", "numOfRows": NUM_ROWS,
                  "pageNo": page, "item_name": keyword, **extra}
        data = call(params)
        items, total = items_of(data)
        rows.extend(items)
        print(f"  [{keyword}] page {page}: +{len(items)} (total={total})")
        if not items or page * NUM_ROWS >= total:
            break
        page += 1
        time.sleep(SLEEP)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keywords", nargs="*", default=DEFAULT_KEYWORDS)
    ap.add_argument("--param", action="append", default=[],
                    help="추가 파라미터 k=v (예: entp_name=엔젤로보틱스)")
    ap.add_argument("--max-pages", type=int, default=50)
    ap.add_argument("--probe", action="store_true", help="1건 호출로 키·스펙 확인")
    args = ap.parse_args()

    key = os.environ.get("MFDS_API_KEY", "")
    if not key:
        sys.exit("MFDS_API_KEY 환경변수에 공공데이터포털 인증키를 넣으세요 "
                 "(README.md의 발급 절차 참고)")
    extra = dict(p.split("=", 1) for p in args.param)

    if args.probe:
        data = call({"serviceKey": key, "type": "json", "numOfRows": 1, "pageNo": 1})
        print(json.dumps(data, ensure_ascii=False, indent=1)[:2000])
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    seen, all_rows = set(), []
    for kw in args.keywords:
        for row in fetch_keyword(key, kw, extra, args.max_pages):
            rid = json.dumps(row, sort_keys=True, ensure_ascii=False)
            if rid not in seen:
                seen.add(rid)
                row["_keyword"] = kw
                all_rows.append(row)

    jsonl = OUT_DIR / f"devices_{stamp}.jsonl"
    with open(jsonl, "w") as f:
        for r in all_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    if all_rows:
        cols = sorted({k for r in all_rows for k in r})
        with open(OUT_DIR / f"devices_{stamp}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(all_rows)
    print(f"\n저장: {jsonl} ({len(all_rows)}건, 중복 제거 후)")


if __name__ == "__main__":
    main()
