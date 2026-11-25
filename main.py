"""Laugh Track entry — make.fun u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.

Writes one original one-line joke about crypto trading life to
/output/entry.txt. Pure stdlib, no network, fully deterministic:
the output is always exactly the same single line, under 200 chars.
"""

import os

JOKE = (
    "Leverage turned my $100 into $1,000 in one day, "
    "then turned my $1,000 into a life lesson in five minutes."
)

DST = "/output/entry.txt"


def main():
    text = JOKE.strip()
    if not text:
        raise ValueError("joke is empty")
    if len(text) > 200:
        raise ValueError("joke exceeds 200 characters: %d" % len(text))
    if "\n" in text:
        raise ValueError("joke must be a single line")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
