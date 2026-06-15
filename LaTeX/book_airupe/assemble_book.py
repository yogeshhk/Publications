#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_book.py
Assembles AIRupe_book_interior.md from individual section files in md_files/.
Streams each file line-by-line; never holds the whole book in memory.

Heading hierarchy for Google Docs import:
  #   (H1)  -- book title (frontmatter) + chapter headings
  ##  (H2)  -- article titles + front/back matter sections
  ### (H3)  -- article subsections (article_23 only)

heading_shift=1 in PLAN shifts every heading down one level on the fly:
  # Title  ->  ## Title
  ## Sub   ->  ### Sub

Usage:
    python assemble_book.py
"""

import os
import sys
import time

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
MD_DIR      = os.path.join(SCRIPT_DIR, "md_files")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "AIRupe_book_interior.md")

# Separator written between every section in the assembled book
SECTION_SEP = "\n\n---\n\n"

# ── Assembly plan ──────────────────────────────────────────────────────────────
# Each entry is one of:
#   ("file",    filename, heading_shift)  -- 0=no change, 1=shift all headings down one level
#   ("chapter", heading_text)            -- inject a single H1 heading line
#
# Front/back matter: shift=0  (their ## sections stay ## in Google Docs)
# Article files:     shift=1  (# title -> ##,  ## subsection -> ###)
# Chapter headings:  injected as '#' (H1) so chapters sit above article '##' (H2)
PLAN = [
    # ── Front matter ──────────────────────────────────────────────
    ("file",    "AIRupe_frontmatter.md",                           0),

    # ── Chapter 1 ─────────────────────────────────────────────────
    ("chapter", "# प्रकरण १: 'एआय' म्हणजे काय?"),
    ("file",    "article_01_whatisai.md",                          1),
    ("file",    "article_02_whatisml.md",                          1),

    # ── Chapter 2 ─────────────────────────────────────────────────
    ("chapter", "# प्रकरण २: 'एआय'ची विविध रूपे"),
    ("file",    "article_03_aimythsandreality.md",                 1),
    ("file",    "article_04_digitalworkforce.md",                  1),
    ("file",    "article_05_aiinpocket.md",                        1),
    ("file",    "article_06_aiinagriculture.md",                   1),
    ("file",    "article_07_aiindefense.md",                       1),
    ("file",    "article_08_aiintranslation.md",                   1),
    ("file",    "article_09_aiinentertainment.md",                 1),
    ("file",    "article_10_aiineducation.md",                     1),
    ("file",    "article_11_aiinhealthcare.md",                    1),
    ("file",    "article_12_aiinhomes.md",                         1),
    ("file",    "article_13_aiintransportation.md",                1),
    ("file",    "article_14_aiinfinance.md",                       1),

    # ── Chapter 3 ─────────────────────────────────────────────────
    ("chapter", "# प्रकरण ३: 'एआय', तंत्रज्ञान आणि आपण"),
    ("file",    "article_15_powerofprompts.md",                    1),
    ("file",    "article_16_myselfandmydata.md",                   1),
    ("file",    "article_17_responsetodigitalcolonization.md",     1),
    ("file",    "article_18_regulatingai.md",                      1),
    ("file",    "article_19_preparingforbigtransition.md",         1),
    ("file",    "article_20_howtocounterdeepfakes.md",             1),
    ("file",    "article_21_attentioneconomy.md",                  1),
    ("file",    "article_22_waratthedoorsteps.md",                 1),

    # ── Chapter 4 ─────────────────────────────────────────────────
    ("chapter", "# प्रकरण ४: ॥ अथ 'एआय'नुशासनाम् ॥"),
    ("file",    "article_23_whatsnext.md",                         1),

    # ── Back matter ───────────────────────────────────────────────
    ("file",    "AIRupe_backmatter.md",                            0),
]


# ── Helpers ────────────────────────────────────────────────────────────────────

def progress_bar(done: int, total: int, width: int = 36) -> str:
    filled = int(width * done / total)
    pct    = 100 * done // total
    return f"[{'#' * filled}{'.' * (width - filled)}] {pct:3d}%"


def verify_files() -> bool:
    """Check all referenced files exist before writing anything."""
    missing = [
        entry[1] for entry in PLAN
        if entry[0] == "file"
        and not os.path.isfile(os.path.join(MD_DIR, entry[1]))
    ]
    if missing:
        print(f"\nERROR - {len(missing)} file(s) not found in {MD_DIR}:")
        for m in missing:
            print(f"  X  {m}")
        return False
    return True


def shift_heading(line: str, shift: int) -> str:
    """Prepend `shift` extra '#' to a Markdown heading line."""
    n = 0
    while n < len(line) and line[n] == "#":
        n += 1
    if n > 0 and n < len(line) and line[n] == " ":
        return "#" * shift + line
    return line


def stream_file(src_path: str, dst, heading_shift: int = 0):
    """
    Stream src_path into dst line-by-line, optionally shifting heading levels.
    Returns (bytes_written, lines_written).
    """
    byte_count = line_count = 0
    with open(src_path, "r", encoding="utf-8") as src:
        for line in src:
            if heading_shift and line.startswith("#"):
                line = shift_heading(line, heading_shift)
            dst.write(line)
            byte_count += len(line.encode("utf-8"))
            line_count += 1
    return byte_count, line_count


# ── Main assembler ─────────────────────────────────────────────────────────────

def assemble() -> None:
    print("=" * 70)
    print("  AIRupe book assembler  (heading-shift edition)")
    print(f"  Source dir : {MD_DIR}")
    print(f"  Output     : {OUTPUT_PATH}")
    print("=" * 70)

    if not verify_files():
        sys.exit(1)

    n_files    = sum(1 for e in PLAN if e[0] == "file")
    n_chapters = sum(1 for e in PLAN if e[0] == "chapter")
    n_total    = len(PLAN)
    print(f"\n  Plan: {n_files} files + {n_chapters} chapter headings = {n_total} steps\n")

    t0           = time.perf_counter()
    total_bytes  = 0
    total_lines  = 0
    files_done   = 0
    first_item   = True

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        for step, entry in enumerate(PLAN, start=1):

            if not first_item:
                out.write(SECTION_SEP)
            first_item = False

            kind = entry[0]

            if kind == "file":
                _, value, shift = entry
                src = os.path.join(MD_DIR, value)
                b, ln = stream_file(src, out, shift)
                total_bytes += b
                total_lines += ln
                files_done  += 1
                shift_tag = f"+{shift}" if shift else "  "
                label = (
                    f"  {progress_bar(step, n_total)}  "
                    f"[{step:02d}/{n_total}]  FILE {shift_tag}  {value:<52s}  "
                    f"{b / 1024:6.1f} KB"
                )
            else:
                _, value = entry
                out.write(value + "\n")
                label = (
                    f"  {progress_bar(step, n_total)}  "
                    f"[{step:02d}/{n_total}]  CHAPTER  {value}"
                )

            print(label)

    elapsed  = time.perf_counter() - t0
    out_size = os.path.getsize(OUTPUT_PATH)

    print()
    print("-" * 70)
    print(f"  Done in {elapsed:.3f} s")
    print(f"  Files streamed : {files_done}")
    print(f"  Lines written  : {total_lines:,}")
    print(f"  Output size    : {out_size / 1024:.1f} KB  ({out_size:,} bytes)")
    print(f"  Output file    : {OUTPUT_PATH}")
    print("-" * 70)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    assemble()
