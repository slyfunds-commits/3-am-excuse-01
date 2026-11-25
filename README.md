# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/slyfunds-commits/3-am-excuse-01/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/slyfunds-commits/3-am-excuse-01/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the make.fun bounty [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) — one line of under 200 characters, the excuse a hardware wallet gives for refusing to sign a transaction at 3 AM, written by `main.py` to `/output/entry.txt`.

## The line

> I read the transaction: same coin, same address, 3:14 AM. The only new thing is the hour. The hour is the scam.

111 characters. The wallet autopsies the transaction and finds the hour in the evidence: same coin, same address, only the hour is new — and the hour is the scam. Three beats (the autopsy, the receipt, the redefinition), a punch in the last words, and a line that breaks if 3 AM becomes 3 PM.

## How it was chosen

378 generated candidates across 8 wallet-native premise families (secure element / PIN, the signer is the threat, screen / air-gap, seed phrase as a character, sleep policy / curfew, dream logic, wallet as bouncer / bodyguard, transaction autopsy), mechanically screened to 356 clean lines in the 90–150 character band, then hand-read in full and scored through the judge-list-max gate (12-item checklist + 5 likes + 5 dislikes + 18 patterns). The keeper passes all 12 checklist items with 5/5 likes, zero dislikes, and patterns P12 (echo-close: "the hour" returns as "the scam"), P1 (self-sealing: the autopsy seals the refusal) and P2 (claim-vs-evidence: the transaction vs the hour). It passes the 3 PM test (at 3 PM the hour is not the scam, so the line collapses) and the excuse test (it deflects blame onto the hour, never confesses).

## Run it

```sh
python3 main.py   # writes output/entry.txt (111 bytes, no trailing newline)
```
