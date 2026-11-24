"""Write the cold email entry to /output/entry.txt.

The Plumber's Inbox: A 120-Word Cold Email
Competition: u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c

A bookkeeping service pitches a busy two-van plumber. The judge, playing the
plumber, reads on a phone between jobs and weighs whether the email knows his
week, keeps the offer small and concrete, and ends with one easy ask. The file
stays under the 800-character gate.
"""
import os

SUBJECT = "Subject: Your bookkeeping, done while you're under a sink"

BODY = """Hi Dan,

Up at 6, van loaded by 6:30, and the invoices still wait till the kids are in bed. That's the job nobody warns you about.

I do the books for four one- and two-van plumbers. I turn your receipts and card payments into clean monthly accounts, chase the slow invoices so you don't have to, and flag which jobs actually made you money. Flat $180 a month, no setup fee, cancel any time.

First step is small: send me last month's receipts. I'll have your numbers back in a week, and you'll see exactly where the cash went.

Worth a quick chat this week? Reply yes and I'll call when you're free.

Mike
Ledgerline Bookkeeping"""


def word_count(text: str) -> int:
    return len(text.split())


def build_entry() -> str:
    """Return the full entry text: subject line first, then the body."""
    return f"{SUBJECT}\n\n{BODY}"


def main() -> None:
    entry = build_entry()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)

    body_words = word_count(BODY)
    total_chars = len(entry)
    valid = total_chars <= 800
    print(f"wrote {out_path}")
    print(f"body words: {body_words}")
    print(f"total chars (gate <=800): {total_chars} -> {'VALID' if valid else 'INVALID'}")


if __name__ == "__main__":
    main()
