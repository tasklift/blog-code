Post: (link will be added when the post goes public)

# 2026-10-21-harvest-zimage_ab

Expand an A/B/C setting block into one job per variant and seed, so variants are compared on the same seeds.

**요약** A/B/C 설정을 변형·시드별 작업으로 펼쳐 같은 시드끼리 비교합니다.

## Run

```bash
python main.py
```

The code runs on small sample data that ships in this folder, so it works offline.

## Results

In the post, with 4 seeds per condition, removing negative wording and raising cfg to 2.0 gave 0 of 4 images with modern objects.

Those numbers are the author's own measurements described in the post; the sample data here only demonstrates the code.
