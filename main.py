#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

The entry is a single line, 1 to 240 characters, in the voice of the Moon
replying at last to the wishes, howls and late-night promises of everyone
staring up at it. This program writes that line to /output/entry.txt.

The line (107 characters, verified by running this file):

    Yes, I'm still up. No, that doesn't make us "in this together" —
    I'm working; you're just avoiding Tuesday.

Why this line won the critique-pick (12 candidates, DeepSeek brutal
critic + my own judging against the kit's brief):

- It is unmistakably the Moon speaking: only the Moon is "still up"
  every single night, and "I'm working" is the Moon's own wry job
  description — it literally works the night shift while everyone
  below it is awake for no good reason.
- It answers the howlers and the insomniacs at once: the people
  staring up at 2 a.m. looking for company, and it refuses the
  company with a comeback.
- The turn lands before the line ends: "you're just avoiding
  Tuesday" flips the shared-night premise into an accusation, and
  "Tuesday" is the funniest possible weekday to be avoiding — dull,
  specific, and obviously not worth staying up for.
- It wastes no characters and explains nothing; the joke is the
  reversal, not a setup that needs footnotes.

The runners-up and why they lost are in CANDIDATES.md. The closest
rival ("You promised you'd change if I just showed up tonight. I
showed up. You're still texting your ex.") has a cleaner two-beat
reversal but could be said by anyone — it is not the Moon's voice.
This one could only be said by the Moon.
"""

import os

# One literal, so the submitted text is exactly what is written here:
# no joining, no formatting, nothing for a grader to misread.
LINE = "Yes, I'm still up. No, that doesn't make us \"in this together\" \u2014 I'm working; you're just avoiding Tuesday."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 240 characters, not only
    # whitespace, and the entry is judged as one line: refuse to write
    # anything else rather than silently submit an invalid entry.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line, no line breaks")
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise ValueError(f"entry line must be 1-240 non-blank chars, got {len(LINE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the gate's shape: exactly the line, byte
    # for byte, with no trailing newline added.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {LINE!r}")


if __name__ == "__main__":
    main()
