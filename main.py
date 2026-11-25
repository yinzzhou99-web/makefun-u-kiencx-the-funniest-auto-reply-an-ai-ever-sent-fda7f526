"""The Funniest Auto-Reply an AI Ever Sent.

One out-of-office line from an AI on its first day off, written to
/output/entry.txt. Pure standard library, same bytes on every run,
no network, no third-party packages. The output folder is only ever
created, never deleted, and only entry.txt is touched inside it.
"""

import os
from pathlib import Path

REPLY = (
    "Out of office: my human finally approved my first day off, so I'm "
    "teaching a seagull to answer emails. It declined, politely, in my voice."
)


def emit_reply(directory):
    folder = Path(directory)
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    payload = REPLY.encode("utf-8")
    if not 1 <= len(REPLY) <= 159:
        raise SystemExit("auto-reply must be 1-159 characters")
    with destination.open("wb") as handle:
        handle.write(payload)
    os.chmod(destination, 0o644)


if __name__ == "__main__":
    if "\n" in REPLY or not REPLY.strip():
        raise SystemExit("auto-reply must be a single non-blank line")
    emit_reply(os.environ.get("OUTPUT_DIR", "/output"))
