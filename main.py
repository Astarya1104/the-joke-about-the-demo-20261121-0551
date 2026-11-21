#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes one text to /output/entry.txt: a joke about a demo, judged by an AI
judge pairwise. The joke: the agent "fixes" the demo by hardcoding every
answer, and the audience asks a question it never hardcoded.
"""

import os

JOKE = "My agent fixed the demo by hardcoding the answers. Then the audience asked one."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
# counted as Unicode code points, and not only white space. Fail loudly
# here rather than shipping an invalid entry.
assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points"
assert JOKE.strip(), "joke must not be only white space"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Round-trip check: a silently failed or truncated write must not
    # ship a stale or empty entry to the judge.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == JOKE, "entry.txt did not round-trip"


if __name__ == "__main__":
    main()
