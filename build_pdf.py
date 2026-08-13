"""
Render README.md — which is the CV — to a PDF you can attach to an application.

    pip install weasyprint markdown
    python build_pdf.py            # full version, ~4 pages
    python build_pdf.py --short    # 2-page version for applications

Two lengths, one source
-----------------------
Keeping a second Markdown file for the short version would have it drift from this one
inside two edits, so both come out of README.md via markers:

    <!--long-->  ...visible on GitHub and in the full PDF, cut from the short one...
    <!--/long-->

    <!--short:  ...a shorter rewrite of the same passage...  -->

GitHub renders HTML comments as nothing, so the short variants stay invisible in the
README and the reading experience there is unchanged. The short build strips the `long`
blocks and un-comments the `short` ones.

The full version is for when someone asks for detail. The short one is what gets
attached to an application: two pages is the convention, and four pages of prose from
someone whose formal employment is measured in months reads as an editing problem before
anyone has judged the engineering.

Writes Alex_Castillo_Gonzalez_Applied_AI_Engineer.pdf (or ..._2-page.pdf) next to
this file.

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
OUTPUT_LONG = os.path.join(HERE, "Alex_Castillo_Gonzalez_Applied_AI_Engineer.pdf")
OUTPUT_SHORT = os.path.join(HERE, "Alex_Castillo_Gonzalez_Applied_AI_Engineer_2-page.pdf")

LONG_BLOCK = re.compile(r"[ \t]*<!--long-->[ \t]*\n(.*?)\n?[ \t]*<!--/long-->[ \t]*\n?", re.S)
SHORT_BLOCK = re.compile(r"[ \t]*<!--short:[ \t]*\n(.*?)\n?[ \t]*-->[ \t]*\n?", re.S)


def select_variant(text: str, short: bool) -> str:
    """Resolve the long/short markers down to one version of the document."""
    if short:
        text = LONG_BLOCK.sub("", text)
        text = SHORT_BLOCK.sub(lambda m: m.group(1) + "\n", text)
    else:
        text = LONG_BLOCK.sub(lambda m: m.group(1) + "\n", text)
        text = SHORT_BLOCK.sub("", text)

    if "<!--" in text:
        raise SystemExit(
            "Unresolved marker left in the document — check for an unclosed "
            "<!--long--> or <!--short: block in README.md."
        )
    # Collapse the blank-line runs the stripped blocks leave behind, or Markdown
    # renders spurious gaps between sections.
    return re.sub(r"\n{3,}", "\n\n", text)

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
    /* Kerning is what a parser trips over. The renderer tightens pairs like "Ty" and
       "Ta" with a positioning offset, and text extraction reads the offset as a space:
       "TypeScript" comes back as "T ypeScript", "Terraform" as "T erraform", "Tailwind"
       as "T ailwind". An applicant tracking system searching for those exact strings
       finds nothing. The typographic loss at 9pt is invisible; the parsing loss is not. */
    font-kerning: none;
    font-variant-ligatures: none;
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


# Applied on top of STYLESHEET for the two-page build. Modest: the point of the short
# version is that there is less to say, not that the same text is squeezed smaller. Type
# below about 8.5pt stops being comfortable on paper, so the savings come from spacing.
SHORT_TIGHTENING = """
body { font-size: 8.6pt; line-height: 1.31; }
@page { margin: 11mm 13mm 13mm; }
h1 { font-size: 18pt; margin-bottom: 2.4mm; }
h2 { font-size: 9.4pt; margin: 3.2mm 0 1.2mm; }
h3 { font-size: 9.2pt; margin: 2.2mm 0 0.4mm; }
p { margin: 0 0 1.2mm; }
li { margin-bottom: 0.6mm; }
ul { margin: 0 0 1.5mm; }
hr { margin: 2.2mm 0 0; }
"""


def build(short: bool = False) -> None:
    with open(SOURCE, encoding="utf-8") as handle:
        text = select_variant(handle.read(), short)

    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    document = f"<!doctype html><html><head><meta charset='utf-8'>" \
               f"<title>Alex Castillo González — Applied AI Engineer</title></head>" \
               f"<body>{body}</body></html>"

    output = OUTPUT_SHORT if short else OUTPUT_LONG
    sheets = [CSS(string=STYLESHEET)]
    if short:
        sheets.append(CSS(string=SHORT_TIGHTENING))

    rendered = HTML(string=document, base_url=HERE).render(stylesheets=sheets)
    rendered.write_pdf(output)

    pages = len(rendered.pages)
    size_kb = os.path.getsize(output) / 1024
    print(f"Wrote {output} ({size_kb:.0f} KB, {pages} pages)")
    if short and pages > 2:
        print(f"  !! {pages} pages — the short version is meant to be 2. Trim further.")


if __name__ == "__main__":
    import sys

    build(short="--short" in sys.argv)
