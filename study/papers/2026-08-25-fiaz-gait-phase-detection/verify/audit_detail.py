"""2차 정밀: F/B 트라이얼별 모드 샘플, 이벤트 보유 파일 분포"""
import csv, io, sys, json, collections
from zipfile import ZipFile
z = ZipFile(sys.argv[1])
post = [n for n in z.namelist() if '_Post/' in n and n.endswith('.csv') and 'MVC' not in n]
by_dir = collections.Counter(); ev_files = collections.defaultdict(int)
walk_by_dir = collections.Counter()
for n in post:
    subj = 'HP117' if 'DAQ_HP117' in n else n.split('/')[0].replace('DAQ_','')
    d = 'F' if '_F_' in n.split('/')[-1] else ('B' if '_B_' in n.split('/')[-1] else '?')
    raw = z.read(n).decode('utf8', errors='replace').replace('\x00','')
    rows = csv.reader(io.StringIO(raw, newline='')); next(rows)
    ev = 0
    for r in rows:
        if len(r) < 24: continue
        by_dir[d] += 1
        try: m = int(float(r[23]))
        except ValueError: m = -1
        if m in (2,8,5): walk_by_dir[d] += 1
        if len(r) >= 58 and any(r[c].strip() not in ('','0','0.0') for c in (50,52,54,56)): ev += 1
    if ev: ev_files[f'{subj}_{d}'] += 1
print(json.dumps({'rows_by_direction': dict(by_dir),
 'walking_rows_by_direction': dict(walk_by_dir),
 'files_with_events_by_subject_dir': dict(sorted(ev_files.items()))}, indent=1))
