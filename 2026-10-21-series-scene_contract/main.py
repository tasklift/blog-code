"""Scene contract: facts a picture must keep, graded as true/false per candidate."""

import json

CONTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "facts": {"type": "array", "items": {"type": "string"}},
        "people_count": {"type": "integer"},
        "must_have": {"type": "array", "items": {"type": "string"}},
        "must_not_have": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["facts", "people_count"],
}


def contract_prompt(script, image_description):
    return (
        "Before looking at the picture, extract the contract from the script: who does what, how many people, "
        "props that must appear, things that must not appear. Then grade the picture description with three "
        "booleans: contract_kept, body_ok, count_ok.\n"
        f"Script: {script}\nPicture: {image_description}"
    )


def passes(grade):
    return bool(grade["contract_kept"] and grade["body_ok"] and grade["count_ok"])


def main():
    print(json.dumps(CONTRACT_SCHEMA)[:80], "...")
    print(contract_prompt("An old man eats soup; a girl watches.", "A girl eating soup.")[:60], "...")
    grades = [
        {"contract_kept": False, "body_ok": True, "count_ok": True},
        {"contract_kept": True, "body_ok": True, "count_ok": True},
    ]
    assert [passes(g) for g in grades] == [False, True]
    print("pass rate:", sum(map(passes, grades)) / len(grades))


if __name__ == "__main__":
    main()
