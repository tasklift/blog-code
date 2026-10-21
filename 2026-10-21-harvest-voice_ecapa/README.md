Post: (link will be added when the post goes public)

# 2026-10-21-harvest-voice_ecapa

Score TTS chunks against a reference voice with cosine similarity and flag the drifting ones.

**요약** TTS 조각을 견본 목소리와 코사인 유사도로 채점해 벗어난 조각을 골라냅니다.

## Run

```bash
python main.py
```

Dependencies: optional: speechbrain, torchaudio (only for real audio)

The code runs on small sample data that ships in this folder, so it works offline.

## Results

In the post, 51 Korean chunks had median similarity 0.806 and 10 were below 0.75; 108 English chunks had none below 0.75.

Those numbers are the author's own measurements described in the post; the sample data here only demonstrates the code.
