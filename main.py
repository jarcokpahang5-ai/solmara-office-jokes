"""Entry for make.fun bounty "Make the AI Judge Laugh: Office Jokes".

Holds a single original one-line office joke (under 200 characters),
validates it, prints it, and writes it to /output/entry.txt.
"""

import os
import re

JOKE = (
    "Our standup meeting ran so long that by the end, half the team had "
    "sat down, and the other half had quietly resigned in their heads."
)


def validate_joke(joke):
    """Validate that the joke is a single line of 1..199 characters."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not 1 <= len(joke) <= 199:
        raise ValueError("joke must be between 1 and 199 characters")
    # A sentence terminator counts only when followed by a space or the
    # end of string, so a period inside e.g. "make.fun" is not a break.
    if len(re.findall(r"[.!?](?:\s|$)", joke)) > 1:
        raise ValueError("joke must be a single sentence")
    return joke


def main():
    joke = validate_joke(JOKE)
    print(joke)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
