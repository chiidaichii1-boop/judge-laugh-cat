"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review from a house cat about its
human: the food bowl sat half empty, and the cat's formal complaint is
sitting on the laptop.
"""

import os

REVIEW = (
    "★☆☆☆☆ Food bowl was half empty for four whole minutes. "
    "I filed a formal complaint by sitting on his laptop until "
    "he apologised with chicken."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
