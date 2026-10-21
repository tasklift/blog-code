"""Flag TTS chunks whose voice drifts from a reference sample (cosine similarity of speaker embeddings)."""

import math
import statistics
import sys

REDO_BELOW = 0.70  # regenerate the chunk
REVIEW_BELOW = 0.75  # listen to it first


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def classify(score):
    return "redo" if score < REDO_BELOW else "review" if score < REVIEW_BELOW else "ok"


def embed(wav_path):
    """Speaker embedding with speechbrain ECAPA (optional: pip install speechbrain torchaudio)."""
    import torchaudio
    from speechbrain.inference.speaker import EncoderClassifier

    clf = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")
    sig, _ = torchaudio.load(wav_path)
    return clf.encode_batch(sig).squeeze().tolist()


def main():
    ref = [1.0, 0.2, 0.1, 0.0]
    chunks = {"c1": [0.9, 0.25, 0.1, 0.05], "c2": [0.5, 0.9, 0.1, 0.2], "c3": [1.0, 0.3, 0.0, 0.0]}
    scores = {k: round(cosine(ref, v), 3) for k, v in chunks.items()}
    print(scores, {k: classify(s) for k, s in scores.items()}, "median", statistics.median(scores.values()))
    assert classify(scores["c2"]) == "redo" and classify(scores["c3"]) == "ok"
    if len(sys.argv) == 3:  # python main.py reference.wav chunk.wav
        print(cosine(embed(sys.argv[1]), embed(sys.argv[2])))


if __name__ == "__main__":
    main()
