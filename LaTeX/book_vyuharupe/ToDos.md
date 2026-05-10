# व्यूहरूपे — Project ToDos

High-level plan. Not exhaustive — adjust as the book evolves.

---

## Phase 0: Setup (Done)

- [x] Project folder and LaTeX template created
- [x] Title and identity fixed: व्यूहरूपे / खेळ मांडला / खेला होबे
- [x] All .tex files updated (covers, interior, initial pages) — ManahPraRupe references removed
- [x] English chapter briefs converted to `book_vyuharupe_content.json`
- [x] `README Strategy Marathi Book.md` adapted for Marathi version
- [x] Prompts ready for manuscript splitting, translation, review, compilation
- [x] Cover design: assigned to Reeya

---

## Phase 1: Marathi Manuscript

- [ ] Decide approach: write Marathi original OR translate from English chapters
- [ ] If writing original: produce chapter briefs in Marathi first (use Prompt 5 in README Strategy Marathi Book.md)
- [ ] If translating: translate each English chapter using Prompt 2, then review with Prompt 3
- [ ] Write ~36 chapters (~1500 words each) following the Marathi structure in README Strategy Marathi Book.md
- [ ] Running theme: Ramesh–Suresh chai tapri duel — write the recurring opening para for each chapter

---

## Phase 2: TeX File Generation

- [ ] Once manuscript is ready, split into chapterwise .tex files (use Prompt 1)
- [ ] Name convention: `ch01_game_theory.tex`, `ch02_zero_sum.tex`, etc.
- [ ] Add all `\input{chNN_*}` lines to `book_vyuharupe_content.tex`
- [ ] Run `make_vyuharupe.bat` — verify compilation
- [ ] Fix any XeLaTeX font or encoding issues

---

## Phase 3: Editorial

- [ ] Anti-AI naturalness pass on each chapter (Prompt 3)
- [ ] Consistency check: Ramesh–Suresh theme consistent across all chapters
- [ ] Marathi proofreading (म्हणी, idioms, terminology consistency)
- [ ] Developmental edit: flow between sections, chapter order
- [ ] Final manuscript freeze

---

## Phase 4: Cover and Design

- [ ] Brief Reeya: theme, colour palette, Devanagari title treatment
- [ ] Cover draft review
- [ ] Back cover text finalised (already drafted in covers.tex)
- [ ] Author photo updated if needed

---

## Phase 5: Publisher

- [ ] Approach Sakal Prakashan first (existing relationship via Sakal column)
- [ ] If declined: try Rajhans Prakashan, then Mehta Publishing House
- [ ] Prepare: 3 sample chapters + overview in Marathi for submission
- [ ] Negotiate: retain Hindi translation rights + Indian language rights
- [ ] Sign contract — review with AI for one-sided clauses before signing

---

## Phase 6: Production and Launch

- [ ] Final LaTeX compile with ISBN barcode (once ISBN assigned)
- [ ] Proof PDF review
- [ ] Print run decision
- [ ] Launch event (Pune; possibly Sakal-linked)

---

## Notes

- English book (Apress) and Marathi book (व्यूहरूपे) are independent — manage timelines separately
- Hindi version (खेला होबे) is a future possibility — not in current scope
- Reeya doing cover design — same as English book
