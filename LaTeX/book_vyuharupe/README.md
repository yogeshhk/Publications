# व्यूहरूपे — *Vyuharupe*

**Internal working title:** khel mandala (खेळ मंडळ)

Marathi book on strategy, strategic thinking, and game-theoretic reasoning.  
Companion to the Apress English manuscript (see below).

---

## Book Identity

| Field | Value |
|---|---|
| Internal title | khel mandala / खेळ मंडळ |
| Public Marathi title | व्यूहरूपे |
| Subject | Strategy — real-world strategic patterns, game theory, decision-making |
| Language | Marathi (Devanagari), XeLaTeX |
| Font | Tiro Devanagari Marathi |
| Paper size | 6 in × 9 in |
| Engine | XeLaTeX (`texify --engine=xetex`) |

---

## File Structure

```
book_vyuharupe/
├── Main_Book_VyuhaRupe_covers.tex    # Driver: front + back cover (article class)
├── Main_Book_VyuhaRupe_interior.tex  # Driver: full interior (book class)
├── template_book.tex                 # Shared LaTeX preamble / style
├── vyuharupe_initialpages.tex        # Copyright, dedication, preface chapters
├── book_vyuharupe_content.tex        # Main chapter content (currently empty)
├── make_vyuharupe.bat                # Build script — runs XeLaTeX on both drivers
├── book_vyuharupe_structure.json     # Machine-readable logical-unit map of all tex files
├── TODO.md                           # Comprehensive project roadmap
└── images/                           # Image assets (myphoto, mylinkedinqr, isbn_barcode, logo)
```

---

## Build

```bat
make_vyuharupe.bat
```

Compiles both `Main_Book_VyuhaRupe_covers.tex` and `Main_Book_VyuhaRupe_interior.tex` via XeLaTeX.

---

## Apress English Manuscript

> **Placeholder — to be filled once Apress manuscript is available / translation is approved.**

When the English manuscript is received:

1. Place chapter markdown/Word source as `manuscript_en/` or reference `manuscript.md` here.
2. Follow prompts in `TODO.md → Phase 3` to split into chapter-wise `.tex` files.
3. Compile English book independently, then trigger Marathi translation workflow.

See `TODO.md` for the full pipeline, including ready-to-use prompts for:
- Splitting a monolithic manuscript into `ch01_*.tex`, `ch02_*.tex`, … files
- Translating each English chapter `.tex` → Marathi `.tex`
- Compiling the Marathi book from translated chapters

---

## Current Status

All `.tex` files were copied from the earlier *मन:प्रारूपे* (ManahPraRupe — mental models) book
and **have not yet been updated** for *व्यूहरूपे*. All titles, descriptions, dedication, and
front/back cover text still reference the mental-models subject.

See `TODO.md` for the ordered revamp plan.

---

## Author

Dr. Yogesh Hari Kulkarni  
Pune, India
