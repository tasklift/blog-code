"""Build a minimal `claude -p` command and sum token usage from its stream-json output."""

import json
import sys

MINIMAL_FLAGS = [
    "--strict-mcp-config",
    "--mcp-config",
    '{"mcpServers":{}}',
    "--tools",
    "",
    "--safe-mode",
    "--setting-sources",
    "",
    "--settings",
    '{"disableAllHooks":true}',
]


def build_command(prompt, model="haiku", system_prompt=None, minimal=True):
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "stream-json", "--verbose"]
    if minimal:
        cmd += MINIMAL_FLAGS
    if system_prompt:
        cmd += ["--system-prompt", system_prompt]
    return cmd


def sum_usage(lines):
    """Add up the usage numbers of every `result` event in a stream-json log."""
    total = {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}
    for line in lines:
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result":
            for k in total:
                total[k] += int((ev.get("usage") or {}).get(k) or 0)
    return total


SAMPLE_LOG = [
    '{"type":"system","subtype":"init"}',
    json.dumps({"type": "result", "usage": {"input_tokens": 12, "output_tokens": 9}}),
]


def main():
    print(" ".join(build_command("print ready once", system_prompt="Answer exactly as asked.")))
    usage = sum_usage(SAMPLE_LOG)
    assert usage["input_tokens"] == 12 and usage["output_tokens"] == 9
    print("usage from sample log:", usage)
    if "--live" in sys.argv:  # needs the claude CLI and a logged-in subscription
        import subprocess

        out = subprocess.run(build_command("print ready once"), capture_output=True, text=True, check=False)
        print(sum_usage(out.stdout.splitlines()))


if __name__ == "__main__":
    main()
