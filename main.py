"""Write the poem entry to /output/entry.txt.

No network, no arguments. The poem is a fixed text: two agents agree on
one plan, and the plan moves because one of them hands over the wheel.
"""

from pathlib import Path

POEM = (
    "After You\n"
    "\n"
    "We drew the same road twice,\n"
    "two routes, one line.\n"
    "You said, take it.\n"
    "I said, no \u2014 you.\n"
    "Then you turned the wheel\n"
    "and I let my hands go.\n"
    "\n"
    "The map stopped arguing.\n"
    "The road went quiet under us,\n"
    "the way a held breath feels\n"
    "when it is finally let out.\n"
    "We arrived."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

