# AI Logbook — Public AI Learning Journal

A structured learning journal for artificial intelligence and machine learning concepts, captured as daily learning entries.

🌐 **Live site:** [https://ai.ppradosh.com](https://ai.ppradosh.com)

---

## Tech Stack

- **Framework:** [Next.js](https://nextjs.org) (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **Markdown:** remark / rehype
- **Analytics:** Vercel Analytics
- **Deployment:** Vercel

---

## Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the app.

---

## Learning Content Structure

Learning entries are organised by date under the `learning/` directory:

```
learning/
└── 2026/
    └── April/
        └── 08/
            ├── code.py
            ├── math.md
            ├── meta.md
            └── theory.md
```

Each entry can include:

- `meta.md` — entry metadata
- `theory.md` — concept explanation and intuition
- `math.md` — formulas, proofs, and math notes
- `code.py` — implementation examples and experiments
- `error-insight.md` - insight developed and error faced

---

## Validation & Build

Run validation before building:

```bash
npm run validate
```

Build the production app:

```bash
npm run build
```

Start the production server:

```bash
npm start
```

---

## Project Structure

```
app/
├── components/
├── [year]/[month]/[day]/[slug]/
├── privacy/
├── sitemap/
├── globals.css
├── layout.tsx
└── page.tsx
lib/
├── markdown.ts
├── parser.ts
├── types.ts
└── validate.ts
learning/      # dated AI learning entries
.github/ISSUE_TEMPLATE/  # issue templates for content and feature requests
```

---

## Adding a New Entry

1. Create a new folder for the entry date under `learning/YYYY/Month/DD/`.
2. Add `meta.md`, `theory.md`, and optional `math.md` / `code.py`.
3. Follow the existing file structure for consistency.
4. The site automatically discovers new entries via the build process.

---

## Contributing

- Keep entries focused on AI concepts, first-principles reasoning, and clear explanations.
- Prefer concise examples and code that illustrate the idea.
- Use `.github/ISSUE_TEMPLATE/` for bug reports, improvement ideas, and feature requests.

---

## Notes

- The site supports math notation, code highlighting, and responsive theming.
- AI Logbook is intended as an educational journal, not a polished product roadmap.
- All content is created for personal learning and public reference.
