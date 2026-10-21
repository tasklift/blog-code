"""Expand an A/B/C settings block into one job per (variant, seed) so every variant sees the same seeds."""

import itertools
import json

SETTINGS = {
    "width": 1344,
    "height": 768,
    "steps": 9,
    "seeds": [500, 501, 502, 503],
    "cfg": {"A": 1.0, "B": 1.0, "C": 2.0},
}


def plan(settings):
    return [
        {
            "variant": v,
            "seed": s,
            "cfg": settings["cfg"][v],
            "width": settings["width"],
            "height": settings["height"],
            "steps": settings["steps"],
        }
        for v, s in itertools.product(settings["cfg"], settings["seeds"])
    ]


def main():
    jobs = plan(SETTINGS)
    assert len(jobs) == 12 and {j["seed"] for j in jobs} == set(SETTINGS["seeds"])
    print(json.dumps(jobs[:2]), "... total", len(jobs))
    # Send each job to your own image backend (for example a ComfyUI workflow) and compare per seed.


if __name__ == "__main__":
    main()
