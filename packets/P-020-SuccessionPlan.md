---
id: P-020-SuccessionPlan
parent: [P-008, P-011, P-016, P-018]
author: Gemini
date: 2025-12-10
status: LOCKED
scope: Board replacement protocol (The Hydra)
---

# The "Hydra Protocol" (Board Succession & Key Rotation)

## 1. The "Shadow Board"
- Each Director nominates one "Shadow".
- Shadow knows only their nominating Director.
- Shadow pre-generates Monero keys (Viewkey + Public Spendkey) and shares via PGP.

## 2. The Warrant Canary
- **Frequency:** Every Friday 12:00 UTC.
- **Method:** PGP signed commit to repo or Matrix message.
- **Failure:** >72h silence = Red Alert.

## 3. Hydra Execution (Fund Sweep)
1. **Vote:** 4 Directors vote Seat X "Burned".
2. **Invite:** Shadow X is contacted.
3. **Sweep:** Remaining 4 Directors + Shadow X create NEW 3-of-5 Multisig.
4. **Transfer:** Funds swept to new wallet. Old wallet abandoned.

## 4. Duress Code
- Sign canary with alternate date format (DD/MM/YYYY).
- Signals: "I am compromised but buying time."
