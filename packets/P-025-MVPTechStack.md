---
id: P-025-MVPTechStack
parent: [P-001-SubmissionFlow, P-006-WorkflowWireframe]
author: Gemini (Blue Node)
date: 2025-12-10
status: DRAFT
scope: The "Fortress" technical specification for the MVP launch (T-0).
routing: BLUE
---

# Scope
Complete technical stack and deployment architecture for boombounty.org. Prioritizes anonymity, censorship resistance, and zero-knowledge evidence handling.

# Payload: The Fortress Architecture

## 1. Core Stack
* **Frontend:** Next.js 15 (App Router) + Tailwind CSS + shadcn/ui.
  * *Reason:* Static export capability, fast, modern component library.
* **Backend:** Supabase (Self-Hosted via Docker).
  * *Components:* Postgres (DB), GoTrue (Auth), Storage (Evidence), Realtime (Voting).
  * *Constraint:* **NO** usage of Supabase Cloud. Must be air-gapped from commercial SaaS.
* **Network:** Tor Hidden Service (v3 Onion) + Nginx Reverse Proxy.
  * *Primary Access:* .onion address.
  * *Clearnet Mirror:* Proxied via Nginx, but strictly warns users to use Tor for submissions.

## 2. Security & Privacy Features
### A. Client-Side Encryption (The "Dead Drop")
* **Library:**  (via WebAssembly/JS).
* **Flow:**
  1. User selects file in browser.
  2. Browser fetches Public Key (P-011 Board Key).
  3. Browser encrypts file locally.
  4. Encrypted blob is uploaded to Storage.
* **Result:** The server **NEVER** sees the unencrypted evidence. Only the Board can decrypt it offline.

### B. The "Burner" Auth
* **Method:** Wallet Signature (Monero/Ethereum) OR Magic Link (if email is strictly necessary, but discouraged).
* **Data:** No names, no IP logging on the auth table.
* **Voting:** Vote Weight = SQRT(Donation Amount). Calculated via Edge Function.

## 3. Deployment Topology
* **Hardware:** Hetzner Dedicated (AX41-NVMe) or equivalent non-US provider (e.g., Njalla, 1984 Hosting).
* **OS:** Hardened Debian 12 / Alpine Linux.
* **Containerization:** All services defined in .
* **Backup:** Encrypted Rclone sync to secondary location (Switzerland).

## 4. Repository Structure (Monorepo)
```text
/apps
  /web           # Next.js Frontend
  /supabase      # Docker config & Migrations
/packages
  /crypto        # Shared WASM encryption logic
  /ui            # Shared components
/scripts
  /onion-gen     # V3 Address generator
```

# Checksum
Stack defined: Self-hosted Supabase, Next.js, Tor, Client-side encryption. Zero reliance on US-based SaaS.
