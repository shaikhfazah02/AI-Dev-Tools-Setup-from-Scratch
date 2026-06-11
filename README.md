# No Tutorial Matched What I Saw; So I Figured It Out Myself
Setup documentation for Cursor IDE, Claude Code, and Codex as part of the application assignment.
# Setting Up AI Dev Tools With Zero Prior Experience- Every Step, Every Roadblock, Documented!

**Name:** Fazah Shaikh
**Date:** May 5, 2026

---

## Tools Installed

| Tool | Where I Got It |
|------|---------------|
| Cursor IDE | cursor.com |
| Claude Code | Cursor Extensions Marketplace |
| Codex | Cursor Extensions Marketplace |
| Git | git-scm.com |

---

## Steps Completed

1. Downloaded and installed Cursor IDE from cursor.com
2. Installed Git from git-scm.com after realizing it was required for GitHub
3. Installed Claude Code extension inside Cursor
4. Installed Codex extension inside Cursor
5. Created a public GitHub repository
6. Cloned the repository locally using Git
7. Opened the cloned folder in Cursor
8. Created and documented this README.md
9. Committed and pushed to GitHub

---

## Issues & How I Solved Them

### Issue 1 — Could not find Extensions in Cursor's new interface
Cursor recently released version 3 which completely replaced the classic IDE layout with an agent-first interface. Every YouTube tutorial I watched showed a different screen than what I had. The standard shortcut `Ctrl + Shift + X` wasn't working because the extensions panel doesn't exist in the Agents Window.

**How I solved it:** After going through every single icon in the Agents tab and watching multiple YouTube videos that were all outdated, I discovered on my own that I had to switch to the **Editor Window** inside Cursor first. Once I clicked that, `Ctrl + Shift + X` worked and the Extensions tab opened.

---

### Issue 2 — Could not log into Claude Code or Codex
After installing both extensions, logging in required a **Pro or Max subscription** for Claude Code and a paid OpenAI plan for Codex. I do not have either.

**How I handled it:** I successfully installed both extensions and went through the setup process up to the login step. Since the assignment required installing the tools and documenting the process — not actively using them — I completed what was possible without a paid plan and documented this roadblock honestly.

---

### Issue 3 — Git was not installed, GitHub clone failed
When I tried to clone my GitHub repository inside Cursor's terminal, I got a `CommandNotFoundException` error. The terminal did not recognize the `git` command at all.

**How I solved it:** After researching, I found that Git needs to be installed separately — it doesn't come with Cursor or Windows by default. I downloaded and installed it from git-scm.com, restarted Cursor, and the clone command worked.

---

### Issue 4 — Cloned folder ended up in the wrong location
After cloning, I couldn't find my repository folder in the expected location. The terminal kept throwing a `PathNotFound` error when I tried to navigate to it.

**How I solved it:** I searched for the folder in Windows File Explorer and found it had been cloned in an unexpected location. I navigated there using the correct path and opened the folder successfully in Cursor.

---

### Issue 5 — Two commands typed on one line caused an error
While navigating into my folder and opening Cursor, I typed `cd 100hires-Test-Project cursor.` as a single line. This caused a `PositionalParameterNotFound` error in PowerShell.

**How I solved it:** Each terminal command needs to be run separately with Enter pressed after each one. Split into two commands — `cd 100hires-Test-Project` then `cursor .` — and it worked immediately.

---

## The Real Lesson

None of these tools worked out of the box without running into real problems. Every issue required independent research — YouTube, documentation, and a lot of trial and error. That process of figuring things out is exactly what this assignment was testing.
