"""make.fun bounty: Two Days of Quiet Dread.

Deterministic, no-network program. Writes one code review
comment, at most 140 characters, to /output/entry.txt. It
approves the pull request while carrying quiet existential
dread: the tests pass, the code is fine, and in a hundred
years none of it will matter anyway. Running twice writes
identical bytes."""
from pathlib import Path

LINE = 'LGTM. The tests are green, the code is fine, and none of it will matter in a hundred years. Merging.'

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
