Post: [한국어 글](https://chon91.tistory.com/4) | [한국어 글 (Velog)](https://velog.io/@tasklift/Claude-Code-%EC%9E%90%EB%8F%99-%ED%98%B8%EC%B6%9C-%EB%AC%B8%EB%A7%A5-4%EB%A7%8C900%ED%86%A0%ED%81%B0-%EC%8B%A4%EC%B8%A1%EA%B8%B0)

# 2026-10-21-series-token_cut

Shrink the context of automated `claude -p` calls with a few flags, and sum token usage from the stream-json log.

**요약** claude -p 를 자동으로 부를 때 플래그로 호출 크기를 줄이고, stream-json 기록에서 토큰을 합산합니다.

## Run

```bash
python main.py
```

The code runs on small sample data that ships in this folder, so it works offline.

## Results

In the post, one call dropped from 39,967 to 900 context tokens (-97.7%), measured once per condition with haiku.

Those numbers are the author's own measurements described in the post; the sample data here only demonstrates the code.
