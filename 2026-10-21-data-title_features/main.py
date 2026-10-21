"""Share of 'hit' videos (views >= 3x the channel median) by title length bucket."""

import csv
from pathlib import Path

BUCKETS = [(0, 15), (16, 25), (26, 35), (36, 10**6)]
HIT_MULTIPLE = 3


def bucket_of(n):
    for lo, hi in BUCKETS:
        if lo <= n <= hi:
            return f"{lo}-{hi}" if hi < 10**6 else f"{lo}+"
    return "?"


def hit_rates(rows):
    out = {}
    for r in rows:
        b = out.setdefault(bucket_of(len(r["title"])), [0, 0])
        b[0] += 1
        b[1] += int(r["views"]) >= HIT_MULTIPLE * int(r["channel_median"])
    return {k: {"videos": v[0], "hit_pct": round(100 * v[1] / v[0], 1)} for k, v in sorted(out.items())}


def main(path=None):
    path = Path(path or Path(__file__).with_name("sample_titles.csv"))
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    res = hit_rates(rows)
    assert sum(v["videos"] for v in res.values()) == len(rows)
    for k, v in res.items():
        print(k, v)


if __name__ == "__main__":
    main()
