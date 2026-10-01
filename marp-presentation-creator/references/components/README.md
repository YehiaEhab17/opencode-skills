# Component Library

This directory contains reusable Marp SmartArt components. Each component is in its own subfolder with a self-contained `preview.md` and a compiled `preview.pdf`.

## How to use

1. Scan the table below and pick a component that fits your slide's content needs.
2. Open the component's `preview.md` file.
   - **Slide 1** renders the component with descriptive placeholder content so you can see the visual.
   - **Slide 2** contains the copy-paste template: CSS block + HTML snippet.
3. Copy the CSS into your presentation's `<style>` block and the HTML into your slide's content area.
4. Replace the `{{Placeholder}}` text with your actual content. The CSS uses `var(--primary)` and `var(--secondary)` — define these in your presentation's `:root` to match your theme.

---

## Component Catalog

| # | Name | Use Case | Template File |
|---|------|----------|---------------|
| 1 | Process Timeline | Phased plans, roadmaps, sequential steps (3-5 items) | [preview.md](process-timeline/preview.md) |
| 2 | Grid Cards 2x2 | Feature lists, outcomes, 4-item groupings | [preview.md](grid-cards-2x2/preview.md) |
| 3 | Grid 3 | Conclusion/vision items, 3-pillar summaries | [preview.md](grid-3/preview.md) |
| 4 | SWOT Grid | Competitive analysis, strengths/weaknesses/opportunities/threats | [preview.md](swot-grid/preview.md) |
| 5 | Chevron List | Problems, pain points, sequential issues (arrow indicators) | [preview.md](chevron-list/preview.md) |
| 6 | Process Pillars | Core principles, values, high-level concepts (3 columns) | [preview.md](process-pillars/preview.md) |
| 7 | Layered Blocks | Foundation/readability topics, hierarchical information | [preview.md](layered-blocks/preview.md) |
| 8 | Benefits Grid | Feature benefits, advantages, value propositions (2x2 with icons) | [preview.md](benefits-grid/preview.md) |
| 9 | Feature Columns | Platform features, service offerings (4-column horizontal) | [preview.md](feature-columns/preview.md) |
| 10 | Flow Diagram | Sequential outcomes, connected process steps with arrows | [preview.md](flow-diagram/preview.md) |
| 11 | Text + Image Side | How-it-works, numbered steps + screenshot, process explanations | [preview.md](text-image-side/preview.md) |
| 12 | Split Card | Two-concept comparisons, pros/cons, before/after | [preview.md](split-card/preview.md) |
| 13 | Focus Panel | Key message + supporting points (hero + sidebar) | [preview.md](focus-panel/preview.md) |
| 14 | Horizontal Stripes | Market analysis, label + description pairs, key-value lists | [preview.md](horizontal-stripes/preview.md) |
| 15 | Stats Row | Survey data, KPIs, metrics (large percentage numbers) | [preview.md](stats-row/preview.md) |
| 16 | Team Grid | Team member cards, person profiles (4-column grid) | [preview.md](team-grid/preview.md) |
| 17 | Stat Boxes | Key financial numbers, single metrics, emphasized figures | [preview.md](stat-boxes/preview.md) |
| 18 | Smart Art Rows | Tips, warnings, action items with icons (stacked horizontal cards with color variants) | [preview.md](smart-art-rows/preview.md) |
| 19 | Smart Art Grid 2x3 | 6-item groupings, tip collections, feature grids (3 cols × 2 rows) | [preview.md](smart-art-grid-2x3/preview.md) |
| 20 | Quote + Image Container | Testimonials, religious quotes, callouts with supporting image | [preview.md](quote-image-container/preview.md) |

## Adding a New Component

1. Create a new subfolder: `components/your-component-name/`
2. Write `preview.md` following the same 2-slide format (demo + template)
3. Add an entry to this README table
4. Run `bash scripts/generate-previews.sh` to compile the PDF preview
