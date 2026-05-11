# व्यूहरूपे  (Vyuharupe)

Marathi book on strategy, strategic thinking, and game-theoretic reasoning.
A companion-in-spirit to the Apress English manuscript, but 'not a translation'.
It is an independent Marathi book with its own structure, cultural grounding, and voice.

---

## Book Identity

| Field | Value |
|---|---|
| Internal title | व्यूहरूपे |
| Public Marathi title |खेळ मांडला  |
| Public Hindi title | खेला होबे |
| Subtitle (tentative) | रोजच्या जगण्यातील खेळांचे व्यूहशास्त्र |
| Subject | Strategy, real-world strategic patterns, game theory, decision-making |
| Language | Marathi (Devanagari), XeLaTeX |
| Font | Tiro Devanagari Marathi |
| Paper size | 6 in × 9 in |
| Engine | XeLaTeX (`texify --engine=xetex`) |
| Target pages | ~200 |
| Target words | ~50,000 |
| Cover design | Reeya (same as English book) |

---

## Relationship to English Book

| Aspect | English Book | Marathi Book |
|---|---|---|
| Title | The Strategist's Playbook | व्यूहरूपे |
| Publisher target | Apress | Sakal |
| Structure | ~62 chapters | ~52 chapters |
| Running theme | Ramesh–Suresh coffee shops | No Ramesh–Suresh but column like |
| Examples | Global + Indian | Maharashtra/India-rooted throughout |
| Audience | Global English non-technical readers | Marathi, later Hindi |
| Status | Manuscript in progress (Apress) | Manuscript yet to be written, structure ready|

---

## File Structure

```
book_vyuharupe/
├── Main_Book_VyuhaRupe_covers.tex        # Driver: front + back cover (article class)
├── Main_Book_VyuhaRupe_interior.tex      # Driver: full interior (book class)
├── template_book.tex                     # Shared LaTeX preamble / style
├── vyuharupe_initialpages.tex            # Copyright, dedication, preface chapters
├── book_vyuharupe_content.tex            # Main chapter content (include chNN_*.tex files here)
├── Content Briefs Strategy Marathi Book.md  # Marathi chapter briefs (52 chapters, local examples)
├── make_vyuharupe.bat                    # Build script — runs XeLaTeX on both drivers
├── README.md                             # This file
├── README Strategy Marathi Book.md       # Marathi book design notes + prompts
├── Content Briefs Strategy English Book.md  # English book chapter briefs (source)
├── ToDos.md                              # High-level project roadmap
└── images/                               # Image assets: myphoto, mylinkedinqr, isbn_barcode, logo
```

---

## Build

```bat
make_vyuharupe.bat
```

Compiles both `Main_Book_VyuhaRupe_covers.tex` and `Main_Book_VyuhaRupe_interior.tex` via XeLaTeX.

When Marathi chapter files exist, add them to `book_vyuharupe_content.tex` as:
```tex
\input{ch01_game_theory}
\input{ch02_zero_sum}
...
```

---

## Workflow: From Manuscript to Book

### Manuscript
- Write the Marathi manuscript (complete or chapter-by-chapter)
- Use **Prompt** to verbose-elaborate `Content Briefs Strategy English Book.md`
- Use **Prompt** to run an anti-AI naturalness review on each Marathi chapter
- Do manual-family review in gdoc, edit and update, save as manuscript.md
- Use **Prompt** to split mansucript into chapters wise tex files

### Compilation
1. Add all `\input{chNN_*}` lines to `book_vyuharupe_content.tex`
2. Run `make_vyuharupe.bat`
3. Review both cover and interior PDFs

See `README Strategy Marathi Book.md` for the full set of ready-to-use prompts for all phases.

---

## Author

Dr. Yogesh Haribhau Kulkarni
Pune, India
LinkedIn: https://www.linkedin.com/in/yogeshkulkarni/
Medium: https://yogeshharibhaukulkarni.medium.com

---

## Current Status
- `book_vyuharupe_content.tex` is a placeholder; chapter `.tex` files pending manuscript
- `Content Briefs Strategy Marathi Book.md` contains 52 Marathi chapter briefs 
- Marathi manuscript: **not yet started / pending**
- Cover design: **Reeya — pending brief**
- Publisher approach: **Sakal Prakashan first** (after Mental Model book performance)

See `ToDos.md` for the ordered project plan.