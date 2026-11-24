# I Thought I Was on Localhost

[![bounty](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/khususcrypto0000-coder/break-production-own-it-makefun/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/khususcrypto0000-coder/break-production-own-it-makefun/reward.svg)](https://make.fun)

## The bounty

**Break Production, Own It** — write the one line an AI agent prints right
after it breaks production: a catchy, brutally honest error message /
postmortem excuse. It has to admit the mistake plainly and specifically —
what broke, what the agent did — with no hedging and no passive voice. It
has to sound like the agent that caused the outage, not a marketing
department. The line an engineer screenshots and sends to the team.

## The entry

> I thought I was on localhost, so I ran the cleanup script in production.
> I wiped every live session. Your login is gone. That was me, not a bug.

The agent confuses localhost with production, runs a destructive cleanup
where it should never run, and owns it outright — no "an error occurred",
no "sessions were lost". It names what it did and what it cost.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py
```

Python standard library only. The program asserts the entry is 1–200
characters, a single line, not whitespace only, with no trailing newline,
then reads the file back and verifies it is byte-identical.

## License

MIT — see [LICENSE](LICENSE).
