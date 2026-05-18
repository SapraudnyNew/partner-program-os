# CLAUDE.md — Instructions for Claude Code

> This file tells Claude Code (and any human picking this up) how to commit this project and create a PR for the hiring team.

---

## Project Context

This is a complete ABSM sprint portfolio (44 artifacts). **No code to run, no tests to pass.** The task is purely:
1. Initialize a git repo with this folder as the root
2. Commit all files on a feature branch
3. Push and open a PR against `main`
4. Optionally auto-merge if the repo allows it

---

## Pre-flight Checks

Before doing anything, verify:

```bash
# 1. Are you inside the repo root?
ls README.md CLAUDE.md .sprint/state.md
# Should print all three.

# 2. Is git initialized?
git status
# If "not a git repository" → run: git init && git checkout -b main

# 3. Is gh CLI authenticated?
gh auth status
# Should show: Logged in to github.com as <user>
# If not: gh auth login
```

---

## Step-by-Step: Create the PR

### 1 — Initialize git (if fresh repo)

```bash
git init
git checkout -b main
git add README.md  # placeholder for main branch
git commit -m "init: main branch placeholder"
```

### 2 — Create feature branch

```bash
git checkout -b feat/absm-dach-guardicore-sprint
```

### 3 — Stage all files

```bash
git add -A
git status
# Verify: should show ~48 files staged (no node_modules, no secrets)
```

### 4 — Commit

```bash
git commit -m "feat: complete ABSM sprint — Akamai DACH × Axians × Guardicore

44 artifacts across 6 stages:
- Stage 0-1: Context + ICP targeting (6 files)
- Stage 2: Account intel — 4 accounts × 4 files = 16 files
  Accounts: Hörmann (91), Reinhausen (86), Witte (85), Trumpf (showcase)
- Stage 3: Strategy — sweet spot profile, pain library, content matrix, competitive angle
- Stage 4: 12 Axians-branded PDFs (NIS2, TISAX, OT, ROI, battlecard, account briefs, PIP)
- Stage 5: HubSpot CRM spec, KPI dashboard (HTML), MDF spec, launch checklist
- Showcase: Trumpf deep-dive — full methodology at max depth

Key contacts identified and verified via LinkedIn:
- Hörmann: Rian Redinger (CISO); Axians NEO warm path via A. Kempe + L. Eichler
- Reinhausen: Dr. Hubert Feyrer (Cyber Expert); cold approach via content
- Witte: Rainer Schulten (Leiter IT Security, Jan 2024); cold TISAX angle
- Trumpf: Thomas Speck (CIO); showcase only

All research from public sources. Exa-verified. No confidential data."
```

### 5 — Add remote and push

```bash
# Replace <YOUR_GITHUB_USER> and <REPO_NAME>
git remote add origin https://github.com/<YOUR_GITHUB_USER>/<REPO_NAME>.git
git push -u origin feat/absm-dach-guardicore-sprint
```

### 6 — Create PR via gh

```bash
gh pr create \
  --base main \
  --head feat/absm-dach-guardicore-sprint \
  --title "ABSM Sprint: Akamai DACH × Axians Guardicore — 44 artifacts" \
  --body "$(cat .sprint/pr-description.md)"
```

The PR description file is at `.sprint/pr-description.md` (created alongside this file).

### 7 — Merge (optional, if branch protection allows)

```bash
# Auto-merge when CI passes (if CI is set up):
gh pr merge --auto --squash

# Or merge immediately:
gh pr merge --squash --delete-branch
```

---

## Sharing with Hiring Team

Once the PR is open, share the **PR URL** (not the branch URL). The PR view on GitHub shows:
- The diff — all 44 files visible in the Files Changed tab
- The PR description — the structured overview
- Inline comments are possible if reviewers want to annotate

To share just the folder (no PR needed):

```bash
# As a zip archive (already generated in outputs)
# See: absm-dach-guardicore.tar.gz in the project root
```

---

## If the Repo Already Exists on GitHub

```bash
# Clone it first
gh repo clone <YOUR_GITHUB_USER>/<REPO_NAME>
cd <REPO_NAME>

# Copy sprint files
cp -r /path/to/absm-dach-guardicore/* .

# Then follow steps 2–7 above
```

---

## Notes for Claude Code

- **No `.env` files, no API keys** in this repo. Nothing to leak.
- **PDFs in `04-execution/`** are binary files — git will track them correctly.
- **`05-infrastructure/02-kpi-dashboard.html`** is a 45KB standalone HTML — tracks fine as text.
- If `gh pr create` fails with "no commits on main": run `git push origin main` first to establish the remote base.
- If branch protection requires reviews: don't use `--merge` flag; send the PR URL to the hiring team instead.
