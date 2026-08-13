"""
Render README.md — which is the CV — to a PDF you can attach to an application.

    pip install weasyprint markdown
    python build_pdf.py

Writes Alex_Castillo_Gonzalez_Applied_AI_Engineer.pdf next to this file.

The Markdown stays the single source of truth. A PDF kept as its own document drifts
from the README within two edits, and the README is what a recruiter sees first when
they open the repo, so it is the one that has to be right.

Design constraints, in priority order:

1. Machine-readable. Most applications go through an applicant tracking system before
   a human sees them. That means real selectable text, one column, and the section
   headings a parser expects (Summary, Skills, Experience, Projects, Education) —
   never a two-column layout or a sidebar, both of which parse as interleaved
   nonsense.
2. Printable. Near-monochrome with one accent, so it survives a greyscale printer.
3. Not broken across pages mid-thought. A job or project entry that splits across a
   page boundary reads as two half-entries.
"""
import os
import re

import markdown
from weasyprint import HTML, CSS

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "README.md")
OUTPUT = os.path.join(HERE, "Alex_Castillo_Gonzalez_Applied_AI_Engineer.pdf")

STYLESHEET = """
@page {
    size: A4;
    margin: 14mm 15mm 16mm;
    @bottom-right {
        content: "Alex Castillo González · page " counter(page) " of " counter(pages);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 7.2pt;
        color: #8A93A0;
    }
}

:root { --ink: #16191F; --muted: #4E5761; --accent: #24406B; --rule: #D2D8DF; }

body {
    font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif;
    font-size: 9.1pt;
    line-height: 1.42;
    color: #16191F;
    margin: 0;
}

/* Name.
   The bottom margin is not decorative. With the blocks tight together, PDF text
   extraction emits them on one line and an applicant tracking system reads the
   surname and the job title as a single token — "GonzálezApplied". Enough vertical
   separation makes the extractor break the line. */
h1 {
    font-size: 20pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    margin: 0 0 3mm;
    color: #16191F;
}

/* The title line and the contact line: the two paragraphs before the first rule. */
h1 + p {
    font-size: 10.5pt;
    font-weight: 700;
    color: #24406B;
    margin: 0 0 1.5mm;
    letter-spacing: 0.01em;
}
h1 + p + p {
    font-size: 8.4pt;
    color: #4E5761;
    margin: 0 0 3mm;
    line-height: 1.5;
}

h2 {
    font-size: 10pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: #24406B;
    margin: 5mm 0 2mm;
    padding-bottom: 1mm;
    border-bottom: 0.6pt solid #24406B;
    break-after: avoid;
}

h3 {
    font-size: 9.8pt;
    font-weight: 700;
    color: #16191F;
    margin: 3.5mm 0 0.6mm;
    break-after: avoid;
}

/* The dated line directly under a role or project heading. */
h3 + p {
    font-size: 8.3pt;
    color: #4E5761;
    margin: 0 0 1.2mm;
}

p { margin: 0 0 1.8mm; }

ul { margin: 0 0 2.5mm; padding-left: 4.2mm; }
li { margin-bottom: 1.1mm; }
li::marker { color: #8A93A0; }

a { color: #24406B; text-decoration: none; }

strong { font-weight: 700; color: #16191F; }
em { color: #4E5761; }

code {
    font-family: "DejaVu Sans Mono", monospace;
    font-size: 8.2pt;
    background: #EFF2F5;
    padding: 0 0.6mm;
    border-radius: 1pt;
}

hr { border: none; border-top: 0.5pt solid #D2D8DF; margin: 3.5mm 0 0; }

/* Keep an entry whole: a role split across a page reads as two half-roles. */
h3 { page-break-after: avoid; }
h3 + p + ul, h3 + ul, h3 + p + p { page-break-before: avoid; }
li { page-break-inside: avoid; }
"""


def build() -> None:
    with open(SOURCE, encoding="utf-8") as handle:
        text = handle.read()

    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    document = f"<!doctype html><html><head><meta charset='utf-8'>" \
               f"<title>Alex Castillo González — Applied AI Engineer</title></head>" \
               f"<body>{body}</body></html>"

    HTML(string=document, base_url=HERE).write_pdf(
        OUTPUT, stylesheets=[CSS(string=STYLESHEET)]
    )

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"Wrote {OUTPUT} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    build()
