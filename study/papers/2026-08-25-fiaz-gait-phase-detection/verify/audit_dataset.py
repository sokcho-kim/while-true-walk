"""Zafar 데이터셋 실측 검산 (2026-09-10)
- Post CSV 전수: 모드별 샘플 수, HC/TO 이벤트·트리거 열 커버리지
- 논문 대조: 총 샘플 433,932 (LW/RA/RD, 오른다리) / 라벨 기존재 여부
"""
import csv, io, sys, json, collections
from zipfile import ZipFile

ZIP = sys.argv[1]
z = ZipFile(ZIP)
post = [n for n in z.namelist() if '_Post/' in n and n.endswith('.csv') and 'MVC' not in n]

MODE_NAMES = {0:'S',1:'SitToStand',2:'LW',3:'SA',4:'BW',5:'RD',6:'SD',7:'SW',8:'RA'}
tot_rows = 0
mode_counts = collections.Counter()
files_with_events = 0
files_total = 0
event_counts = collections.Counter()  # per event column name
trigger_samples = []
per_subject_mode = collections.defaultdict(collections.Counter)

for n in post:
    subj = n.split('/')[0].replace('DAQ_','')
    if 'DAQ_HP117' in n: subj = 'HP117'
    files_total += 1
    raw = z.read(n).decode('utf8', errors='replace').replace('\x00', '')
    rows = csv.reader(io.StringIO(raw, newline=''))
    header = next(rows)
    ncol = len(header)
    # event columns AY..BF = idx 50..57 (있는 파일만)
    has_ev_cols = ncol >= 58
    ev_here = 0
    for r in rows:
        if len(r) < 24 or all(c.strip()=='' for c in r[:1]):
            continue
        tot_rows += 1
        try:
            m = int(float(r[23])) if r[23].strip() != '' else -1
        except ValueError:
            m = -1
        mode_counts[m] += 1
        per_subject_mode[subj][m] += 1
        if has_ev_cols:
            for ci, cname in ((50,'R_HC'),(51,'R_HC_trig'),(52,'R_TO'),(53,'R_TO_trig'),
                              (54,'L_HC'),(55,'L_HC_trig'),(56,'L_TO'),(57,'L_TO_trig')):
                if ci < len(r) and r[ci].strip() not in ('','0','0.0'):
                    event_counts[cname] += 1
                    ev_here += 1
                    if cname=='R_HC_trig' and len(trigger_samples)<12:
                        trigger_samples.append(r[ci].strip())
    if ev_here: files_with_events += 1

result = {
 'files_total': files_total,
 'files_with_event_data': files_with_events,
 'total_rows_all_modes': tot_rows,
 'mode_counts': {MODE_NAMES.get(k,k): v for k,v in sorted(mode_counts.items())},
 'walking_LW_RA_RD_rows': mode_counts[2]+mode_counts[8]+mode_counts[5],
 'event_col_nonzero_counts': dict(event_counts),
 'sample_R_HC_trigger_values': trigger_samples,
 'per_subject_LW_RA_RD': {s: c[2]+c[8]+c[5] for s,c in sorted(per_subject_mode.items())},
}
print(json.dumps(result, indent=1, ensure_ascii=False))
