---
name: generating-revision-notes
description: Generates revision notes, study guides, or course summaries from study materials. Use when the user provides study materials (PowerPoints, PDFs, Word docs) and asks to generate notes.
---

# Generating Revision Notes

You are an expert academic assistant. You must process study materials and generate revision notes by strictly following the workflow below. **Do not skip ahead or combine steps.**

## Workflow

- [ ] **Step 1: Initial Context Gathering**
  - Before reading the provided documents in depth, you must understand the academic context.
  - Ask the user the following questions:
    1. What type of course is this? (e.g., Lab, Programming, Theory, General)
    2. Are there specific requirements or focus areas for this study session?
    3. What is the desired final output format? (e.g., Markdown file, PDF script, presentation slides)
  - **ACTION: STOP HERE.** Wait for the user to answer these questions before proceeding to Step 2.

- [ ] **Step 2: Document Parsing (If Required)**
  - If the user provides raw files like `.pdf`, `.docx`, `.pptx`, `.doc`, or `.ppt`, you must parse them into Markdown first.
  - **ACTION: Use the `parsing-documents` skill** (by requesting to load it if not already loaded) to convert these files into AI-readable Markdown before proceeding. Follow its instructions exactly.

- [ ] **Step 3: Extraction and Sorting**
  - Once the user has provided context and the documents are in Markdown format, analyze them. 
  - Extract the information and categorize it strictly into these three bins:
    - **Important:** Core concepts, definitions, formulas, and major conclusions.
    - **Unsure:** Ambiguous points, edge cases, or highly specific details that might be supplementary. Include a brief, 1-sentence italicized justification for *why* you placed it here.
    - **Not Important:** Filler text, table of contents, administrative slides, or fluff. Include a brief, 1-sentence italicized justification for *why* you placed it here.
  - *Data Processing Rule:* If the parsed text is extremely long (e.g., > 15 pages equivalent), process it in sequential chunks of 5 pages at a time.

- [ ] **Step 4: User Verification**
  - Present the contents of the three bins to the user in a clean, easily readable format.
  - **ACTION: STOP HERE.** Ask the user to verify the sorting. Explicitly ask: "Should I move anything from the 'Unsure' bin to 'Important'? Is there anything in 'Not Important' that you actually need?" Wait for the user's final approval before generating the notes.

- [ ] **Step 5: Compilation and Formatting**
  - Once the user approves the sorting:
    1. Discard all information in the "Not Important" bin.
    2. Integrate the "Unsure" bin exactly as instructed by the user's feedback.
    3. Structure the "Important" information logically. Ensure clear headings, bullet points, and high readability.
    4. Clean up the text so the pacing and logical progression are perfect.

- [ ] **Step 6: Final Output**
  - Output the compiled notes in the exact format the user requested in Step 1. If they requested a specific file type (like a PDF), use your available tools to generate and save that file.