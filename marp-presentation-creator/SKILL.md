---
name: marp-presentation-creator
description: Generates clean, professional Marp (Markdown Presentation) slides. Use this skill whenever the user asks to create a presentation, a PowerPoint, or slides using Marp. Also use it when the user needs to convert content (reports, proposals, papers) into presentation slides. It includes a library of reusable CSS "SmartArt" components (timelines, grids, flow diagrams, stats rows, split cards, SWOT analysis, etc.), compilation guidance for PDF/PPTX, and solutions for common Marp rendering bugs (overflow, HTML parsing, blank slide separators). This skill is self-improving: when it invents a new component or solves a novel Marp issue, it asks the user whether to save the solution for future use.
---

# Marp Presentation Creator

This skill guides you in creating professional, visually engaging presentations using Marp CLI. It includes a library of reusable CSS components and solutions to common Marp rendering pitfalls.

## 1. Presentation Structure & Frontmatter

Always start with Marp frontmatter containing a robust CSS theme:

```yaml
---
marp: true
theme: default
class:
  - lead
size: 16:9
style: |
  :root {
    --primary: #003366;
    --secondary: #00A8CC;
    --bg-color: #F4F7F6;
    --text-color: #2C3E50;
    --white: #FFFFFF;
  }
  section {
    background-color: var(--bg-color);
    background-image: linear-gradient(135deg, rgba(0,168,204,0.03) 0%, rgba(0,51,102,0.06) 100%);
    color: var(--text-color);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding-top: 50px;
    padding-bottom: 30px;
  }
  section::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 10px;
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
  }
  section::after {
    content: '';
    position: absolute;
    bottom: 0; right: 0;
    width: 150px;
    height: 150px;
    background: radial-gradient(circle at bottom right, rgba(0,168,204,0.1), transparent 70%);
    z-index: 0;
  }
  h1 {
    color: var(--primary);
    font-size: 2em;
    margin-top: 0;
    margin-bottom: 0.5em;
    z-index: 10;
    position: relative;
  }
  h1::after {
    content: '';
    display: block;
    width: 60px;
    height: 5px;
    background-color: var(--secondary);
    margin-top: 8px;
    border-radius: 3px;
  }
---
```

Key variables: `--primary` (dark), `--secondary` (accent), `--bg-color`, `--text-color`.

## 2. Title Slide & Special Sections

Use Marp slide classes (`<!-- _class: title-slide -->` or `<!-- _class: demo-slide -->`) to create distinct slide types. Define these in the `<style>` block.

**Title slide pattern:**
```css
section.title-slide {
  background: linear-gradient(135deg, #E6F0FA 0%, #C4DFE6 100%);
  padding: 80px;
}
section.title-slide::before, section.title-slide::after { display: none; }
section.title-slide h1 { font-size: 3.8em; ... }
```

## 3. Layout Variation is Critical

**Do NOT use the same layout for every slide.** Audiences find repetitive layouts (e.g., 2x2 grids on every slide) unappealing. For each content slide, choose a *different* SmartArt style from the component library. Mix and match:
- Some slides use process timelines
- Some use flow diagrams with arrows
- Some use hero + sidebar panels (Focus Panel)
- Some use stats rows with large numbers
- Some use split cards for comparisons
- Some use horizontal stripes for key-value pairs
- Some use smart art rows for tips/warnings with icons
- Some use grids (but limit to 1-2 slides max)

## 4. Preventing Overflow

Content overflowing the slide is a common Marp issue. Fixes:
- Reduce `padding` in cards (use `15px` instead of `20-30px`)
- Reduce icon sizes (`.card-icon { font-size: 1.8em; }`)
- Reduce title `margin-bottom` in cards
- Shorten description text to fit
- For full-width slides, use `max-width: 900px; margin: 0 auto;` on containers

## 5. Slide Separator Discipline

- Every new slide MUST be separated by exactly one `---` on its own line
- **Never** put `---` twice in a row (creates empty slides)
- **Never** forget `---` between slides (content merges)
- Always verify after insertion that slide breaks are clean

## 6. HTML & Markdown Interactions

**Inside HTML divs**, Marp does NOT render Markdown unless there is a blank line after the opening tag. However, when building HTML-only structures (divs with no markdown inside), blank lines are safe.

**Best practice for SmartArt components:** Use pure HTML (no markdown inside the divs). Put all text inside `<p>`, `<h3>`, `<h4>` tags instead of mixing markdown syntax.

When using images with absolute positioning (e.g., a logo on the title slide), constrain dimensions explicitly:
```css
.ts-logo {
  position: absolute;
  top: 50px; right: 50px;
  width: 160px; height: 160px;
  border-radius: 50%;
  object-fit: cover;
}
```

## 7. Compilation

Use Marp CLI to compile. See `references/commands.md` for the full list of options.

Basic compilation:
```bash
npx @marp-team/marp-cli input.md -o output.pdf --allow-local-files
npx @marp-team/marp-cli input.md -o output.pptx --allow-local-files
```

For editable PowerPoint text (experimental — may have layout differences):
```bash
npx @marp-team/marp-cli input.md -o output.pptx --allow-local-files --pptx-editable
```

If the default Chromium is not found, specify a browser path:
```bash
npx @marp-team/marp-cli input.md -o output.pdf --browser-path /usr/bin/chromium-browser
```

## 8. Reusable Component Library

This skill bundles a comprehensive CSS component library in `references/components/`. **Read `references/components/README.md` first** and choose from its layouts before writing custom CSS.

The component library is organized as individual folders, each containing:
- **`preview.md`** — A self-contained Marp file with the component's CSS and a demo slide.
- **`preview.pdf`** — A compiled preview showing the component rendered.

Each component's `preview.md` has two slides:
- **Slide 1:** Renders the component with descriptive `{{placeholder}}` content so you can see the visual layout.
- **Slide 2:** Contains the reusable template — CSS block with `var(--primary)` / `var(--secondary)` + HTML snippet with `{{Placeholders}}`.

To use a component:
1. Scan the component table in `README.md` to find the right layout for your content.
2. Open the component's `preview.md` file in the corresponding folder.
3. Copy the CSS from Slide 2 into your presentation's `<style>` block.
4. Copy the HTML template from Slide 2 into your slide content.
5. Replace all `{{Placeholders}}` with your actual content. The `--primary` and `--secondary` CSS variables will auto-theme the component to match your presentation.

## 9. Self-Improvement (Save New Components & Lessons)

This skill improves over time by saving new components and bug fixes. Follow this process:

**When you invent a new CSS layout/component** that isn't in the component library, at the end of the session (after the user has seen the output) ask:
> "I created a new [name] layout for this slide. Do you like it? Would you like me to save it to the component library so it's available for future presentations?"

If the user says yes, create a new component entry:
1. Create a new folder: `references/components/your-component-name/`
2. Create `preview.md` following the same 2-slide format (demo slide + template slide). The CSS should use `var(--primary)` / `var(--secondary)` for theme compatibility.
3. Add an entry to `references/components/README.md` in the component catalog table.
4. Run `bash references/components/scripts/generate-previews.sh` to compile the PDF preview.

**When you encounter and fix a novel Marp rendering issue** (something not already covered in this skill or in lessons learned), save the solution to `references/lessons-learned.md`. At the end of the session, present what you learned and ask:
> "I ran into [issue] and fixed it by [solution]. Would you like me to save this lesson for future reference?"

If the user says yes, append an entry to `references/lessons-learned.md` in the playbook format:
```markdown
### Symptom: [What went wrong in one line]
Fix: [Actionable fix in 1-2 sentences, with code if helpful]
```

New entries should be added under the relevant existing category (e.g. "Layout & Overflow", "Images", "PPTX Output") or a new category if none fits.

**Important:** Always ask before saving. Never write to these files without explicit user approval.
