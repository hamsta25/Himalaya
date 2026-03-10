# HI
# TDP: 2026-03-10T11:00:00Z | Turin, Italy | Himalaya
"""
Himalaya status.py — Expedition & Travel Planning
Run from repo root: python status.py
"""

import os
import subprocess
import sys
import io
from pathlib import Path
from datetime import datetime

# Force UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── ANSI colours ──────────────────────────────────────────────────────────────
R = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GRN = "\033[92m"
YLW = "\033[93m"
BLU = "\033[94m"
MAG = "\033[95m"
CYN = "\033[96m"
DIM = "\033[2m"

def c(color, text): return f"{color}{text}{R}"

def run(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, shell=True)
        return r.stdout.strip()
    except Exception:
        return ""

def section(title):
    print(f"\n{BOLD}{CYN}{'─' * 60}{R}")
    print(f"{BOLD}{CYN}  {title}{R}")
    print(f"{BOLD}{CYN}{'─' * 60}{R}")

ROOT = Path(__file__).parent.resolve()

# ═══════════════════════════════════════════════════════════════════════════════
# 1. BANNER
# ═══════════════════════════════════════════════════════════════════════════════
def banner():
    print(f"""
{BOLD}{MAG}
  ██╗  ██╗██╗███╗   ███╗ █████╗ ██╗      █████╗ ██╗   ██╗ █████╗
  ██║  ██║██║████╗ ████║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔══██╗
  ███████║██║██╔████╔██║███████║██║     ███████║ ╚████╔╝ ███████║
  ██╔══██║██║██║╚██╔╝██║██╔══██║██║     ██╔══██║  ╚██╔╝  ██╔══██║
  ██║  ██║██║██║ ╚═╝ ██║██║  ██║███████╗██║  ██║   ██║   ██║  ██║
  ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
{R}{BOLD}  Expedition & Travel Planning  🏔️{R}
{DIM}  Owner: Hamza Ilyas (hamsta25) | Turin, Italy → Pakistan → Himalaya → Uzbekistan
  Location: {ROOT}
  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{R}
""")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. GIT STATUS
# ═══════════════════════════════════════════════════════════════════════════════
def git_status():
    section("GIT STATUS")
    branch  = run("git rev-parse --abbrev-ref HEAD", ROOT) or "unknown"
    remote  = run("git remote get-url origin", ROOT) or "no remote"
    dirty   = run("git status --porcelain", ROOT)
    ahead   = run("git rev-list @{u}..HEAD --count 2>nul", ROOT) or "0"
    behind  = run("git rev-list HEAD..@{u} --count 2>nul", ROOT) or "0"

    print(f"  {BOLD}Branch:{R}  {c(GRN, branch)}")
    print(f"  {BOLD}Remote:{R}  {c(BLU, remote)}")
    print(f"  {BOLD}Dirty: {R}  {c(RED, 'YES — uncommitted changes') if dirty else c(GRN, 'Clean')}")
    print(f"  {BOLD}Ahead/Behind origin:{R}  +{ahead} / -{behind}")

    print(f"\n  {BOLD}Last 3 commits:{R}")
    log = run("git log --oneline -3", ROOT)
    for line in log.splitlines():
        sha, _, msg = line.partition(" ")
        print(f"    {c(YLW, sha)}  {msg}")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. README CONTENT DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════
def readme_summary():
    section("README — TRIP OVERVIEW")
    readme = ROOT / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8", errors="ignore").strip()
        print(f"  {BOLD}{c(MAG, 'README.md')}:{R}")
        for line in content.splitlines():
            if line.startswith("#"):
                print(f"  {c(CYN, BOLD + line + R)}")
            elif line.strip():
                # word-wrap at ~70 chars for terminal display
                words = line.split()
                cur_line = "    "
                for w in words:
                    if len(cur_line) + len(w) + 1 > 75:
                        print(cur_line)
                        cur_line = "    " + w + " "
                    else:
                        cur_line += w + " "
                if cur_line.strip():
                    print(cur_line)
    else:
        print(f"  {c(RED, 'README.md not found')}")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. DOCUMENT INVENTORY
# ═══════════════════════════════════════════════════════════════════════════════
def dir_inventory():
    section("DOCUMENT INVENTORY")
    all_files = [f for f in ROOT.rglob("*") if f.is_file() and ".git" not in str(f)]

    ext_counts = {}
    for f in all_files:
        ext = f.suffix.lower() or "(no ext)"
        ext_counts[ext] = ext_counts.get(ext, 0) + 1

    print(f"  {BOLD}Total files:{R} {len(all_files)}")
    print(f"\n  {BOLD}File types:{R}")
    for ext, n in sorted(ext_counts.items(), key=lambda x: -x[1]):
        bar = "█" * min(n * 3, 30)
        print(f"    {ext:12s}  {c(CYN, bar)}  {n}")

    # Directory listing
    print(f"\n  {BOLD}All files (non-hidden):{R}")
    for f in sorted(all_files):
        try:
            rel = f.relative_to(ROOT)
            size = f.stat().st_size
            size_str = f"{size}B" if size < 1024 else f"{size//1024}KB"
            print(f"    {c(BLU, str(rel)):50s}  {c(DIM, size_str)}")
        except Exception:
            pass

    # FKUnited license
    fku_lic = ROOT / "FKUnited_license"
    if fku_lic.is_dir():
        lic_files = list(fku_lic.rglob("*"))
        print(f"\n  {BOLD}FKUnited_license/:{R} {len(lic_files)} items  {c(GRN, '(FKUnited Inc. connection)')}")
    else:
        print(f"\n  {c(DIM, 'FKUnited_license/ directory not found')}")

# ═══════════════════════════════════════════════════════════════════════════════
# 5. TODO / NOTES EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════════
def todo_scan():
    section("TODOS & PLANNING NOTES")
    found_todos = []
    found_notes = []

    md_files = list(ROOT.rglob("*.md"))
    for mdf in md_files:
        try:
            lines = mdf.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("- [ ]"):
                try:
                    rel = mdf.relative_to(ROOT)
                except Exception:
                    rel = mdf.name
                found_todos.append((str(rel), i, stripped[6:].strip()))
            elif any(kw in stripped.upper() for kw in ["TODO", "FIXME", "NOTE:", "PLAN:"]):
                try:
                    rel = mdf.relative_to(ROOT)
                except Exception:
                    rel = mdf.name
                found_notes.append((str(rel), i, stripped))

    if found_todos:
        print(f"  {BOLD}Open items ({len(found_todos)}):{R}")
        for fname, lineno, text in found_todos:
            print(f"    {c(YLW, '[ ]')} {text}  {c(DIM, f'({fname}:{lineno})')}")
    else:
        print(f"  {c(GRN, 'No open checklist items found.')}")

    if found_notes:
        print(f"\n  {BOLD}Planning notes ({len(found_notes)}):{R}")
        for fname, lineno, text in found_notes[:10]:
            print(f"    {c(CYN, '📝')} {text[:70]}  {c(DIM, f'({fname}:{lineno})')}")

    # Suggest next planning items if repo is minimal
    if not found_todos and len(list(ROOT.rglob("*.md"))) < 3:
        print(f"\n  {c(YLW, '💡 Suggested next steps:')}")
        suggestions = [
            "Create itinerary/master_itinerary.md with day-by-day schedule",
            "Add logistics/flights.md with booking references",
            "Add gear/packing_list.md for Himalaya equipment",
            "Add research/himalaya_routes.md for route and permit planning",
            "Add logistics/visa_docs.md for EU→PK and PK→UZ visa requirements",
        ]
        for s in suggestions:
            print(f"    {c(YLW, '→')} {s}")

# ═══════════════════════════════════════════════════════════════════════════════
# 6. TECH STACK (document/planning repo)
# ═══════════════════════════════════════════════════════════════════════════════
def tech_stack():
    section("PROJECT TYPE & STACK")
    print(f"  {BOLD}Type:{R}     Personal expedition and travel planning repository")
    print(f"  {BOLD}Format:{R}   Markdown-first, documentation-driven")
    print(f"  {BOLD}License:{R}  FKUnited license (FKUnited_license/ directory)")
    print(f"  {BOLD}Tools:{R}    Git, Markdown editors, mapping tools")
    print()

    md_count = len(list(ROOT.rglob("*.md")))
    print(f"  {BOLD}Markdown files:{R} {md_count}")

    if md_count < 3:
        print(f"  {c(YLW, '  Repo is minimal — primary content is README.md')}")
    else:
        print(f"  {c(GRN, '  Multiple documents present')}")

# ═══════════════════════════════════════════════════════════════════════════════
# 7. QUICK COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════
def quick_commands():
    section("QUICK COMMANDS")
    cmds = [
        ("Open README",             "cat README.md  (or: code README.md)"),
        ("Add expedition notes",    "code itinerary/himalaya_expedition.md"),
        ("See full file tree",      "find . -not -path './.git/*' | sort"),
        ("Git log",                 "git log --oneline"),
        ("Push changes",            "git push origin main"),
        ("Check repo size",         "git count-objects -v"),
        ("Add new location doc",    "cp itinerary/_template.md itinerary/<location>.md"),
    ]
    for label, cmd in cmds:
        print(f"  {BOLD}{c(GRN, label+':'):28s}{R}  {c(DIM, cmd)}")

# ═══════════════════════════════════════════════════════════════════════════════
# 8. HEALTH CHECK
# ═══════════════════════════════════════════════════════════════════════════════
def health_check():
    section("HEALTH CHECK")
    issues = []
    oks = []

    # Dirty check
    dirty = run("git status --porcelain", ROOT)
    if dirty:
        issues.append("Uncommitted changes")
    else:
        oks.append("Working tree clean")

    # README present
    if (ROOT / "README.md").exists():
        oks.append("README.md present")
    else:
        issues.append("README.md MISSING")

    # FKUnited license
    if (ROOT / "FKUnited_license").is_dir():
        oks.append("FKUnited_license/ directory present")
    else:
        issues.append("FKUnited_license/ directory missing")

    # Security: no sensitive data in committed files
    sensitive_patterns = ["password", "passport", "booking ref", "pnr", "secret"]
    all_md = list(ROOT.rglob("*.md"))
    for f in all_md:
        try:
            content = f.read_text(encoding="utf-8", errors="ignore").lower()
            for pat in sensitive_patterns:
                if pat in content:
                    rel = f.relative_to(ROOT)
                    issues.append(f"Possible sensitive data '{pat}' in {rel} — verify it's not a real value")
                    break
        except Exception:
            pass

    # Large files (photos etc.)
    large = []
    for f in ROOT.rglob("*"):
        if f.is_file() and ".git" not in str(f):
            try:
                if f.stat().st_size > 5_000_000:
                    large.append(f"{f.relative_to(ROOT)} ({f.stat().st_size//1_000_000}MB)")
            except Exception:
                pass
    if large:
        issues.append(f"Large files committed (use Git LFS): {', '.join(large)}")
    else:
        oks.append("No oversized files (>5MB)")

    for ok in oks:
        print(f"  {c(GRN, '✓')} {ok}")
    for issue in issues:
        print(f"  {c(RED, '✗')} {issue}")

    print(f"\n  {BOLD}Score:{R} {c(GRN, str(len(oks)))} OK  |  {c(RED, str(len(issues)))} issues")
    if not issues:
        print(f"  {c(GRN, BOLD + '  All checks passed.' + R)}")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        banner()
        git_status()
        readme_summary()
        dir_inventory()
        todo_scan()
        tech_stack()
        quick_commands()
        health_check()
        print(f"\n{DIM}  Himalaya status complete — {datetime.now().strftime('%H:%M:%S')}{R}\n")
    except KeyboardInterrupt:
        print(f"\n{YLW}Interrupted.{R}")
        sys.exit(0)
