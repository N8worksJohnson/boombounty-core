---
id: P-021-DeadManSwitch
parent: [P-018-EscalationMatrix, P-020-SuccessionPlan]
author: Gemini
date: 2025-12-10
status: DRAFT
scope: Technical automation if the entire board is neutralized.
---

# Scope
Technical implementation of the 72-hour timer that triggers the "Scorched Earth" protocol if no board member checks in.

# Payload: The "Lazarus" Daemon

## 1. The Trigger Mechanism
A simple, dumb script running on 3 independent, anonymous VPS instances (Iceland, Switzerland, Panama).
- **Input:** Polling the 'canary' branch of this repo.
- **Logic:** `if (last_commit_timestamp > 72h) { initiate_broadcast(); }`

## 2. The Payload (Encrypted Blob)
We pre-encrypt a file named `DOOMSDAY.7z.gpg` containing:
- The full "Phase 2" and "Phase 3" Target Lists (unredacted).
- The "Zero-Day" cache (any exploits we are holding back).
- The raw source code of the platform.

This file is hosted on **IPFS** and **Arweave** (permanent storage) right now. It is useless without the key.

## 3. The Key Release (Shamir's Secret Sharing)
The decryption key is split into 5 parts using Shamir's Secret Sharing (3-of-5 required).
- **Part 1:** Hardcoded in the Lazarus Daemon source code.
- **Part 2:** Posted automatically to the Ethereum blockchain (via smart contract) if a heartbeat transaction misses.
- **Part 3:** Emailed to 30 journalists (P-014 Press List) via delayed send service.
- **Part 4 & 5:** Held by trusted allies (EFF/WikiLeaks contacts).

## 4. Execution Flow
1. **T+72h:** Board silent.
2. **T+72h 1m:** Lazarus Daemons detect silence.
3. **T+72h 5m:** Daemons publish **Part 1** of the key to X, Reddit, and Nostr.
4. **T+72h 10m:** Ethereum contract misses heartbeat, auto-publishes **Part 2**.
5. **Result:** The public now has 2 parts. They need 1 more from the Press or Allies to unlock the full database.

## 5. Checksum
Dead Man Switch defined. If we die, the information becomes free.

