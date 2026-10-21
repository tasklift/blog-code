"""Top-10% view threshold of a board, and how over-represented each post format is among top posts."""

from collections import Counter

SAMPLE = (
    [("share", 900)] * 5
    + [("question", 40)] * 30
    + [("chat", 120)] * 40
    + [("making-of", 700)] * 6
    + [("question", 300)] * 3
    + [("chat", 60)] * 16
)


def percentile(values, p):
    s = sorted(values)
    return s[min(len(s) - 1, round(p * (len(s) - 1)))]


def format_multiples(posts, p=0.9):
    """multiple = share among top posts / share among all posts (1.0 = just common there)."""
    thr = percentile([v for _, v in posts], p)
    top = [f for f, v in posts if v >= thr]
    allc, topc = Counter(f for f, _ in posts), Counter(top)
    mult = {f: round((topc[f] / len(top)) / (allc[f] / len(posts)), 1) for f in topc}
    return thr, mult


def main():
    thr, mult = format_multiples(SAMPLE)
    views = [v for _, v in SAMPLE]
    med = percentile(views, 0.5)
    print("median:", med, "top10 threshold:", thr, "ratio:", round(thr / med, 1))
    print("multiples:", mult)
    assert thr > med


if __name__ == "__main__":
    main()
