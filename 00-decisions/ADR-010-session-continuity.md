# ADR-010: Session Continuity via STATE.md

**Date:** 2026-05-16
**Status:** Accepted

## Decision

The repo maintains a single canonical state document at `STATE.md` (root). Every working session ends with an update to STATE.md before the chat closes. The previous HANDOVER.md and handover-day2-v2.md files are replaced by STATE.md.

The master handover prompt (`prompts/master-handover-prompt.md`) is rewritten to be lean: it tells the new chat to read STATE.md as the authoritative source. The prompt no longer duplicates state information.

## Context

The project ran into a structural problem: HANDOVER.md, master-handover-prompt.md, and handover-day2-v2.md all carried project-state snapshots taken at different times. By Day 2 morning, the three documents disagreed with each other and with the repo:

- HANDOVER.md said Phase 1 was in progress with stages 1, 3, 4, 6, 7 as skeletons. Reality: all seven stages filled.
- master-handover-prompt.md said the same.
- handover-day2-v2.md said Day 1 complete but didn't reflect the new ADR-009 bundle structure.
- README.md ADR table listed 7 ADRs when 9 existed.
- 02-akamai/00-context.md research checklist had all items unchecked when most were completed.

A new chat reading these files received contradictory state and either accepted the most prominent file as truth (typically the master handover prompt) or wasted time reconciling.

Three options were considered:

1. **Discipline only.** Keep three documents, agree to update all three at session end. Risk: high overhead, drift inevitable.
2. **Single state document, multiple snapshot documents.** Keep handover-day2-v2.md, handover-day3.md, etc. as session artifacts plus a STATE.md as current. Risk: multiplies files, snapshot files become noise.
3. **Single state document with append-only session log.** STATE.md is the only state file. Session events append as log entries inside STATE.md. Other handover files are deprecated.

Option 3 wins. One file, one source of truth, session history preserved as log entries within it.

## Resolution

### STATE.md structure

The file has these sections, in order:

1. **Header.** Last updated date, session description, who updated.
2. **Project description.** One-paragraph framing.
3. **Layer status.** Current state of the three architectural layers (per ADR-008).
4. **Day-by-day execution status.** Table with D-block deliverables and status (DONE, NEXT, TODO).
5. **Locked context.** Decisions and inputs that should not be relitigated. Pulled from ADRs where possible.
6. **Research outputs.** Index of research artifacts committed to the repo.
7. **Key inputs for next work.** Specific names, targets, or data points the next session needs immediately.
8. **Active ADRs.** Compact table.
9. **Repo structure.** Current tree, kept in sync with reality.
10. **Next session opener.** Concrete instructions for starting the next chat.
11. **Session log.** Append-only. Newest entry first. Each entry has: date, session title, Done list, Next list, Blockers, Notes.

### Update discipline

At the end of every working session:

1. Forge updates STATE.md before any closing message.
2. Updates touch: header date, day-by-day status (mark new DONE / new NEXT), session log entry appended at top.
3. If new locked context or new ADR emerges, those sections are updated too.
4. The STATE.md update is committed in the same PR as the session's work, or in a follow-up PR if the session's work is already committed.

### Master handover prompt rewrite

The prompt becomes lean. It states:
- The Forge persona (RJSM purist, tone rules).
- Where to find authoritative state (STATE.md).
- The one thing the new chat must do first: read STATE.md.

The prompt does NOT duplicate the day-by-day table, the layer status, or the locked context. Those live only in STATE.md.

### Deprecated files

- `HANDOVER.md`: deleted.
- `handover-day2-v2.md`: deleted.
- `prompts/prompt-template-build.md`: moved to `prompts/_archive/` (Phase 1 complete, prompt no longer relevant for new work).

## Consequences

- New chats reach productive work faster. Read STATE.md, see day-by-day status, pick up where the previous chat stopped.
- No drift between handover artifacts. There is only one.
- Session history is preserved inside STATE.md as a log, useful for future audits or for understanding why a decision was made.
- The discipline holds only if Forge actually updates STATE.md at session end. The system prompt for new chats and the persistent reminders enforce this.
- STATE.md grows over time. When the session log becomes unwieldy, older entries can be archived to `_session-archive/` but this is a pure logistics decision, not a structural one.
