"""Check that a one-line intro fits an OG image caption (40 characters including spaces)."""

LIMIT = 40


def check(intro, limit=LIMIT):
    n = len(intro)
    return n, n <= limit


def main():
    n, ok = check("A neighborhood bakery, fresh bread daily")
    print(n, "chars", "ok" if ok else "too long: cut off in the OG image")
    assert not check("x" * 41)[1] and check("x" * 40)[1]


if __name__ == "__main__":
    main()
