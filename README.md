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

## Phase 2: Building a 10-Expert Research Base on LinkedIn Strategy for B2B SaaS

**Topic:** LinkedIn organic content strategy for B2B SaaS
**Date:** June 11–13, 2026

---

### Starting With a Hypothesis — and Testing It

The brief was blunt: "10 high-signal sources beat 50 generic ones." So before touching a single transcript, I started by asking Claude to identify genuinely strong voices in LinkedIn organic content for B2B SaaS — not agency listicle names, not the first page of Google.

That first pass surfaced a list, and I started executing on it — adding Dave Gerhardt as expert #1, setting up sources.md, and prepping to pull his LinkedIn posts.

Then I stopped myself. I checked whether Dave Gerhardt had actually said anything specific about LinkedIn organic content strategy for B2B SaaS — and he hadn't. He's a respected B2B marketing voice, but that's not the same as being relevant to this research question. Rather than push forward with a list that looked credible on paper, I went back and re-verified every name against the actual topic, and re-ran the research with sharper criteria: genuinely strong, currently active, and demonstrably about LinkedIn-as-a-channel.

That early catch shaped everything that followed.

---

### Executing: 10 Experts, 10 Transcripts, Real APIs

With the corrected list, I worked through each expert in order — no skipping ahead — using Claude Code to:

- Search for a recent, relevant video on the expert's own channel
- Verify the video was real, on-channel, and on-topic (not just "this person is famous, so anything counts")
- Install and run youtube-transcript-api via pip to pull the full transcript
- Save it as formatted markdown in research/youtube-transcripts/
- Commit and push — one expert at a time, not in one giant batch

Adam Robinson's "30 Million Dollar ARR Growth Machine" video became the template: verified channel, verified video ID, transcript fetched via a real Python script using a real API, saved and pushed within minutes. That same loop repeated for Chris Walker, Simon Høiberg, April Dunford, and others.

---

### When the Source Itself Was the Problem

Not every expert had a clean YouTube trail. For a few — most notably the experts originally in the #5, #6, and #9 slots — the available content was either inaccessible (private videos, channels with no listable videos) or, on closer inspection, not actually about LinkedIn content strategy at all. It was strong SaaS content from credible operators, but it was answering a different question than the one I was researching.

Rather than force those picks to fit, I treated it the same way as the Dave Gerhardt moment: re-verify against the brief, and swap if the fit isn't real. Those three slots became Michelle J. Raymond (LinkedIn Company Pages, two published LinkedIn books), Richard van der Blom (runs the annual LinkedIn Algorithm Insights Report, built on 2.5M+ posts of data), and Sam McKenna (#samsales — LinkedIn personal branding for B2B sales, creator of the "Show Me You Know Me" framework). Each swap, and the reasoning behind it, is documented directly in research/sources.md — including an explicit note on how "SaaS credibility" and "LinkedIn relevance" aren't automatically the same thing.

---

### Collecting LinkedIn Posts — Manually, By Design

LinkedIn has no public API, and scraping it violates their ToS — most automated attempts just hit a login wall. Rather than fight that, I made it a deliberate manual process: for each expert, visit their profile, select 3 recent posts genuinely relevant to the topic, and copy the full text plus the post URL.

The workflow ran one expert at a time: paste the posts → format into clean markdown → Claude Code writes the file → commit → push. By the end, all 10 experts had 3 fully-documented posts each in research/linkedin-posts/, organized in a flat structure (linkedin-posts/[expert-name].md) that mirrors youtube-transcripts/ for consistency.

---

### Final Lineup

| # | Expert | Why They're Here |
|---|--------|-------------------|
| 1 | Adam Robinson | Bootstrapped RB2B to ~10 Million Dollar ARR using LinkedIn as the primary acquisition channel |
| 2 | Chris Walker | High-engagement B2B commentary on demand gen and platform dynamics |
| 3 | Dave Gerhardt | Founder of Exit Five, B2B marketing community and brand strategy |
| 4 | Justin Welsh | Built a 15 Million Dollar solo business on LinkedIn content systems |
| 5 | Michelle J. Raymond | LinkedIn Company Pages strategist, author of two LinkedIn books |
| 6 | Richard van der Blom | Publishes the annual LinkedIn Algorithm Insights Report |
| 7 | Simon Høiberg | Bootstrapped SaaS portfolio, builds AI-driven content workflows |
| 8 | April Dunford | Author of Obviously Awesome, positioning as the foundation of good content |
| 9 | Sam McKenna | #samsales — LinkedIn personal branding for B2B sales leaders |
| 10 | Lenny Rachitsky | Runs the largest product/growth podcast and newsletter in tech |

Full rationale, links, and source annotations for every expert — including the mid-project swaps — live in research/sources.md. All source material is organized in research/youtube-transcripts/, research/other/, and research/linkedin-posts/.

---

### The Real Lesson (Phase 2)

A credible name isn't the same as a relevant source. The first list I built was full of people who'd impress anyone reading it — but two separate checks caught the same problem: content that sounds authoritative isn't automatically content that answers the question being asked. Catching that early, and again mid-project, and fixing it both times with documented reasoning rather than quietly hoping nobody would notice, is what turned a "looks good" research base into one that actually holds up.
