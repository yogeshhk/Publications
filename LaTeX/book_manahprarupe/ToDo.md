# ToDo: book_manahprarupe Chapter Edits

**Last updated:** 2026-06-12  
**Book:** मेन्टल मॉडेल्स (formerly मन:प्रारूपे) — Marathi LaTeX book on Mental Models  
**Scope:** Chapters 01–39. Chapter 40 and `whatsnext` are excluded from all edits.

---

## Task List

### Task 1 — Add intro paragraph to each chapter
Insert the chapter's abstract paragraph (from `Mental Models Intro Paragraphs.md`) right after `\chapter{...}`.

| Status | Chapters |
|--------|----------|
| ✅ Done (plain text, no styling) | 01–12 |
| ⬜ Pending | 13–39 |

---

### Task 2 — Add LLMM figure to each chapter
Insert `\begin{figure}...\includegraphics{LLMM_NN_...png}...\end{figure}` before the summary box at end of chapter.

| Status | Chapters |
|--------|----------|
| ✅ Done | 01–12 |
| ⬜ Pending | 13–39 |

---

### Task 3 — Add tcolorbox summary box to each chapter
Append English summary box (Definition + How to Apply + Try This) at end of each chapter, sourced from `Mental Models Summary Boxes.md`.

| Status | Chapters |
|--------|----------|
| ✅ Done | 01–12 |
| ⬜ Pending | 13–39 |

---

### Task 4 — Bold/blue intro paragraph styling (ALL chapters)
Wrap each intro paragraph with `\textcolor{blue!60!black}{\textbf{...}}` so it visually reads as a chapter abstract (distinct from the original newspaper article text).

| Status | Chapters |
|--------|----------|
| ⬜ Pending (no styling applied to any chapter yet) | 01–39 |

---

### Task 5 — Book title change in auxiliary files
Replace `मन:प्रारूपे` → `मेन्टल मॉडेल्स` in auxiliary/cover/initial-page files only.  
**Chapter files are NOT to be touched.**

| Status | File |
|--------|------|
| ⬜ Pending | `Main_Book_ManahPrarupe_covers.tex` |
| ⬜ Pending | `manahprarupe_initialpages.tex` |
| ⬜ Pending | `Main_Book_ManahPrarupe_interior.tex` |

---

### Task 6 — Compile and fix
Run `make_manahprarupe.bat`, resolve LaTeX errors, confirm clean build.

| Status | Notes |
|--------|-------|
| ⬜ Pending | — |

---

## Progress Summary

| Task | Done | Pending | Total |
|------|------|---------|-------|
| 1. Intro paragraph | 12 chapters | 27 chapters (13–39) | 39 |
| 2. LLMM figure | 12 chapters | 27 chapters (13–39) | 39 |
| 3. tcolorbox summary | 12 chapters | 27 chapters (13–39) | 39 |
| 4. Bold/blue styling | 0 chapters | 39 chapters (01–39) | 39 |
| 5. Title change | 0 files | 3 auxiliary files | 3 |
| 6. Compile | — | Pending | — |

---

## Image Filename Reference (LLMM directory)

| Ch | Image filename |
|----|----------------|
| 13 | `LLMM_13_ProbabilisticThinking_diagrams_13_ai.png` |
| 14 | `LLMM_14_TheDunningKrugerEffect_diagrams_14_ai.png` |
| 15 | `LLMM_15_HanlonsRazor_diagrams_15_ai.png` |
| 16 | `LLMM_16_SystemsThinking_diagrams_16_ai.png` |
| 17 | `LLMM_17_TheAvailabilityHeuristic_diagrams_17_ai.png` |
| 18 | `LLMM_18_SkinInTheGame_diagrams_18_ai.png` |
| 19 | `LLMM_19_TheLawOfDiminishingReturns_diagrams_19_ai.png` |
| 20 | `LLMM_20_ConfirmationBias_diagrams_20_ai.png` |
| 21 | `LLMM_21_Falsifiability_diagrams_21_ai.png` |
| 22 | `LLMM_22_SurvivorshipBias_diagrams_22_ai.png` |
| 23 | `LLMM_23_ThePeterPrinciple_diagrams_23_ai.png` |
| 24 | `LLMM_24_TragedyOfTheCommons_diagrams_24_ai.png` |
| 25 | `LLMM_25_Reciprocity_diagrams_25_ai.png` |
| 26 | `LLMM_26_ThoughtExperiment_diagrams_26_ai.png` |
| 27 | `LLMM_27_Relativity_diagrams_27_ai.png` |
| 28 | `LLMM_28_Thermodynamics_diagrams_28_ai.png` |
| 29 | `LLMM_29_Inertia_diagrams_29_ai.png` |
| 30 | `LLMM_30_FrictionAndViscosity_diagrams_30_ai.png` |
| 31 | `LLMM_31_Velocity_diagrams_31_ai.png` |
| 32 | `LLMM_32_Leverage_diagrams_32_ai.png` |
| 33 | `LLMM_33_ActivationEnergy_diagrams_33_ai.png` |
| 34 | `LLMM_34_Alloying_diagrams_34_ai.png` |
| 35 | `LLMM_35_Catalysts_diagrams_35_ai.png` |
| 36 | `LLMM_36_EvolutionaryNaturalSelection_diagrams_36_ai.png` |
| 37 | `LLMM_37_Replication_diagrams_37_ai.png` |
| 38 | `LLMM_38_Ecosystems_diagrams_38_ai.png` |
| 39 | `LLMM_39_Niches_diagrams_39_ai.png` |
