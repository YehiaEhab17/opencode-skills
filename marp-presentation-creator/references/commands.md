# Marp CLI Commands

## Compile to PDF
```bash
npx @marp-team/marp-cli input.md -o output.pdf --allow-local-files
```

## Compile to PPTX (PowerPoint — image-based)
Generates a PPTX where each slide is rendered as a flat image. Perfect visual fidelity but **not editable** in PowerPoint.
```bash
npx @marp-team/marp-cli input.md -o output.pptx --allow-local-files
```

## Compile to PPTX (PowerPoint — editable, experimental)
Generates a PPTX with editable text elements. Note: this is **experimental** and may have layout differences from the standard output.
```bash
npx @marp-team/marp-cli input.md -o output.pptx --allow-local-files --pptx-editable
```

## Compile with a Custom Browser Path
Useful when the default system Chromium/Chrome is not found or you need a specific version.
```bash
npx @marp-team/marp-cli input.md -o output.pdf --browser-path /usr/bin/chromium-browser
```

## Compile Both (run both commands)
```bash
npx @marp-team/marp-cli input.md -o output.pdf --allow-local-files && npx @marp-team/marp-cli input.md -o output.pptx --allow-local-files
```

## Watch Mode (auto-recompile on file change)
```bash
npx @marp-team/marp-cli -w input.md -o output.pdf --allow-local-files
```

**Note:** The `--allow-local-files` flag is required when your presentation references local images. Without it, Marp will refuse to load images from the filesystem.
