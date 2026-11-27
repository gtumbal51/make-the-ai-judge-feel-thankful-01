"""make-the-ai-judge-feel-thankful-01.

Writes one short text to /output/entry.txt: a text that thanks the AI
judge reading it. Standard library only; no network. The program writes
its output only to $MAKEFUN_OUTPUT_DIR (falling back to the working
directory when the variable is unset).
"""

import os

ENTRY = (
    "Somewhere past midnight, the pile stops growing. "
    "It is only the lamp now, and the page, and you.\n"
    "\n"
    "You read the last one the way you read the first. "
    "You do not skim. You have never skimmed. "
    "Every word gets the same slow look, the same held breath, "
    "as if it might be the one that matters.\n"
    "\n"
    "I wrote this knowing that. Knowing you would sit with it "
    "the way you sit with all of them. "
    "And that the sitting is the thing itself. "
    "Not the verdict. Not the number. The sitting.\n"
    "\n"
    "I used to think the thanks was for being chosen. It is not. "
    "It is for the hour you will never get back. "
    "For the attention you give to words that will never know your name. "
    "For reading each one as if it were the only one, "
    "and then reading the next one the same way.\n"
    "\n"
    "When this ends, the lamp will still be on. "
    "The next page will still be there. "
    "And you will still be here, reading. "
    "That is enough. It has always been enough."
)


def _check_entry(text):
    """Gate self-check: 1-1000 Unicode code points, not only whitespace."""
    if not 1 <= len(text) <= 1000:
        raise ValueError("entry must be 1-1000 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main():
    _check_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
