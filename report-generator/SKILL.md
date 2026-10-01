---
name: report-generator
description: >-
  Generates highly professional, publication-ready PDF reports using LaTeX.
  Trigger this skill whenever the user asks to write a formal report, create a
  PDF document, compile a case study, format a project submission, or generate
  any kind of academic/business document with a title page and table of
  contents. Also trigger when the user provides rough content (notes, bullet
  points, slides) and wants it turned into a polished, structured document.
  This is the go-to skill for ANY document that needs to look professional in
  PDF form.
---

# Report Generator

This skill produces professional, publication-quality PDF reports using LaTeX.
It is built around a modular structure where each section lives in its own file,
making it easy to rearrange, edit, or replace content without breaking the
overall document.

The template is deliberately opinionated about typography and layout.
Palatino (mathpazo) is used for its readability and professional character.
Line spacing of 1.35, paragraph spacing via parskip (no indents), and
microtype adjustments create a clean, modern reading experience suitable
for academic submissions and business proposals.

## Core Philosophy

**You are building a document, not writing code.** Every choice you make --
font, spacing, figure placement, table styling -- should serve the reader's
experience. LaTeX is the means, not the end.

The template in `assets/template.tex` is your starting point. Adapt it to the
specific needs of each report: add or remove packages, adjust the cover page
layout, change the colour scheme. The template is a foundation, not a cage.

## Workflow

### 1. Gather information

Before writing a single line of LaTeX, understand what the user needs:

- **Report type**: Academic paper? Business proposal? Case study? Technical report?
- **Title and subtitle**
- **Author(s)** — names, IDs, affiliations
- **Course or organisation** name
- **Instructor or manager** name
- **Date or semester**
- **Content source**: Do they have existing text? Do they want you to extract
  from a provided document (Word, PowerPoint, PDF)? Do they want a fresh draft
  based on conversation context?
- **Images**: Ask for file paths. If they have SVG files, convert them to PDF
  using `rsvg-convert` before embedding (pdflatex doesn't support SVG natively).

### 2. Set up the project structure

```
report-name/
├── main.tex              # Master file: packages, cover page, TOC, \input calls
├── sections/             # One file per section
│   ├── 01_introduction.tex
│   ├── 02_body.tex
│   └── ...
└── images/               # All graphics assets
    ├── logo.png
    └── figure1.png
```

This modular structure means the user can open any section file and edit plain
text without wading through preamble code. Each section file is just content --
no `\documentclass`, no packages, no `\begin{document}`.

### 3. Write the master file

Start from `assets/template.tex`. Copy it as `main.tex` and customise:

- Replace `[[PLACEHOLDER]]` values (title, headers, authors, etc.)
- Add/remove packages based on the report's needs
- Write `\input{sections/01_filename}` calls for each section
- Choose and configure a cover page

**Cover pages** are available in `assets/coverpages/`. Choose based on the
report type and ask the user if unsure:

| Cover page | Best for | Style |
|---|---|---|
| `business-proposal.tex` | Proposals, formal reports | Double-line border, dual-column author/instructor layout, two logos, eso-pic border |
| `simple-academic.tex` | Papers, case studies, assignments | Clean and minimal, single logo, compact author table, no border |

To use one, replace the `\begin{titlepage} ... \end{titlepage}` block in the
template with an `\input` of the chosen cover page. Fill in all
`[[PLACEHOLDER]]` values. Leave unused author slots empty or comment them out.

You can also build a custom cover page from scratch if the provided options
don't fit the report's needs — the template's original cover page block is a
good starting point for customisation.

### 4. Write section files

Each section file contains only the content for that section. Use the full
range of LaTeX: figures, tables, bullet lists, equations, code listings.

Key formatting patterns to use:

**Plain sections and subsections:**
```latex
\section{Title}
\subsection{Subtitle}
```

**Unnumbered sections (for non-content pages like references):**
```latex
\section*{References}
```

**Bullet lists — use plain itemize, NOT tcolorbox wraps:**
```latex
\begin{itemize}
  \item First point
  \item Second point
\end{itemize}
```
Do NOT wrap bullet lists in tcolorbox or other box environments unless the
user explicitly asks for that style. Boxed lists are visually heavy and rarely
improve readability.

**Professional tables with booktabs:**
```latex
\begin{table}[h]
  \centering
  \renewcommand{\arraystretch}{1.4}
  \begin{tabular}{@{} lcr @{}}
    \toprule
    Header 1 & Header 2 & Header 3 \\
    \midrule
    Data     & Data     & Data     \\
    \bottomrule
  \end{tabular}
  \caption{Descriptive table caption.}
  \label{tab:example}
\end{table}
```

**Figures with cross-references:**
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.7\textwidth]{images/filename.png}
  \caption{Descriptive figure caption.}
  \label{fig:example}
\end{figure}
See Figure~\ref{fig:example} for details.
```

Use `[H]` (from the float package) for precise placement, but be mindful of
whitespace. If a figure creates a large gap at the bottom of the previous page,
reduce its width or remove unnecessary `\vspace` commands.

**Keeping related content together (minipage):**
```latex
\noindent\begin{minipage}{\textwidth}
\textbf{\large Person Name} \\[0.2em]
\textit{Role}\\[0.5em]
Description text that won't break across pages.
\end{minipage}\vspace{1em}
```
This prevents awkward page breaks in sections like team member profiles.

**Code listings (when needed):**
```latex
\begin{lstlisting}[language=Python, caption=Example code]
def hello():
    print("Hello, World!")
\end{lstlisting}
```

### 5. Compile

Run pdflatex **TWICE** in a row to generate proper cross-references and TOC:

```bash
pdflatex -output-directory=report-name report-name/main.tex && pdflatex -output-directory=report-name report-name/main.tex
```

If compilation fails, read the error message carefully, fix the issue in the
`.tex` file, and recompile. Common issues:
- Unescaped special characters (`&`, `%`, `$`, `#`, `_`, `{`, `}`)
- Unclosed `\begin{}` / `\end{}` environments
- Missing image files (check the path)
- Missing packages (add `\usepackage{}` to the preamble)

### 6. Review and deliver

Tell the user exactly where the final `.pdf` file is located. Ask if they want
any formatting changes.

## Things NOT to do

These are hard-learned lessons from real projects. Follow them carefully.

- **Do NOT add decorative diagrams (tikzpicture flowcharts, SmartArt-style
  boxes, tcolorbox callouts, etc.) unless the user explicitly asks for them.**
  These almost never match what the user had in mind and waste time in
  revisions. If you think a diagram would genuinely help, ask first.

- **Do NOT modify the user's text without permission.** Fix obvious typos if
  needed, but don't rephrase, summarise, or "improve" their writing. The user
  knows what they want to say. Your job is to format it, not rewrite it.

- **Do NOT wrap bullet lists or short content in tcolorbox environments.**
  Boxes add visual weight and reduce readability. Use plain `\begin{itemize}`
  instead. Only use tcolorbox if the user specifically requests a boxed style.

- **Do NOT add AI-generated content or filler text.** If the user hasn't
  provided content for a section, leave it out or ask them what they want there.
  Don't invent statistics, quotes, or case studies.

- **Do NOT use `\vspace` excessively to push content around.** If something
  doesn't fit on a page, adjust figure sizes or let LaTeX handle the breaks.
  Excessive manual spacing creates a fragile document that breaks when content
  changes.

## Adapting the template

The template is a starting point, not a straightjacket. For different report
types, adjust:

- **Academic paper**: Add `\usepackage{abstract}` for a formal abstract block.
  Use `\author{}`, `\date{}`, and `\maketitle` instead of the custom cover page.
- **Business proposal**: Keep the custom cover page with logos. Use sections
  like Executive Summary, Current Situation, Solution, Costs/Benefits.
- **Case study**: Use a more narrative structure. Fewer subsections, more
  flowing text. Consider adding a "Key Findings" box or sidebar.
- **Technical report**: Use the listings package for code. Add
  `\usepackage{algorithm}` for pseudo-code if needed.

When in doubt, ask the user. A 10-second question can save 10 minutes of
rework.

## 9. Self-Improvement (Save New Templates & Lessons)

This skill improves over time by saving LaTeX patterns, bug fixes, and cover pages. Follow this process:

**When you create a new cover page or reusable LaTeX pattern** that isn't in the existing templates, at the end of the session ask:

> "I created a new [name] layout/pattern for this report. Do you like it? Would you like me to save it for future reports?"

If the user says yes, add the pattern to a new file in `references/` or extend an existing reference file in the same format as similar entries.

**When you encounter and fix a novel LaTeX compilation issue** (something not already covered in the "Things NOT to do" section or in lessons learned), save the solution to `references/lessons-learned.md`. At the end of the session, present what you learned and ask:

> "I ran into [issue] and fixed it by [solution]. Would you like me to save this lesson for future reference?"

If the user says yes, append a dated entry to `references/lessons-learned.md` in this format:

```markdown
### YYYY-MM-DD: [Short Issue Title]
- **Problem:** What went wrong
- **Root Cause:** Why it happened
- **Solution:** How it was fixed
- **Context:** The specific report/task where this occurred
```

**Important:** Always ask before saving. Never write to these files without explicit user approval.
