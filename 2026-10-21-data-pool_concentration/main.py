"""Median vs mean and top-share of a view-count list (the post's channel check)."""

import csv
import statistics
from pathlib import Path


def top_share(views, frac):
    s = sorted(views, reverse=True)
    k = max(1, round(len(s) * frac))
    return sum(s[:k]) / sum(s)


def summarize(views):
    med = statistics.median(views)
    mean = statistics.mean(views)
    return {
        "videos": len(views),
        "median": med,
        "mean": round(mean),
        "mean_over_median": round(mean / med, 1),
        "top10_share": round(100 * top_share(views, 0.10), 1),
        "top50_share": round(100 * top_share(views, 0.50), 1),
    }


def main(path=None):
    path = Path(path or Path(__file__).with_name("sample_views.csv"))
    with open(path, newline="", encoding="utf-8") as f:
        views = [int(r["views"]) for r in csv.DictReader(f)]
    res = summarize(views)
    assert res["mean"] > res["median"]
    print(res)


if __name__ == "__main__":
    main()
