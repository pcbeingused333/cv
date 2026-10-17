# Alex Castillo González

<!--ai-->
**Applied AI Engineer · Python / LLM**
<!--/ai-->
<!--swe:
**Software Engineer · Python / TypeScript / Ruby**
-->

Santo Domingo, Dominican Republic — UTC−4 · Independent contractor (Spanish passport) · Spanish (native), English (professional)
[alex.castillog33@gmail.com](mailto:alex.castillog33@gmail.com) · [github.com/pcbeingused333](https://github.com/pcbeingused333) · [linkedin.com/in/alexcastillogonzalez](https://www.linkedin.com/in/alexcastillogonzalez) · [portfolio-alexgonzalez33.vercel.app](https://portfolio-alexgonzalez33.vercel.app)

---

## Summary

<!--ai-->
<!--long-->
Applied AI engineer working in Python on retrieval and agent systems, and on the layer
that decides whether they survive real users: evaluation, failure handling, and knowing
which numbers actually moved. My main retrieval project answers over the text of the
**GDPR** and is built around a constraint that regulated domains impose and generic RAG
ignores — every statement has to name the provision it came from, and the system has to
decline when the source does not cover the question. Both projects ship with the harness
that measures them — retrieval, citation accuracy and abstention for the RAG system,
tool trajectories and answer grounding for the MCP agent — and in each case the harness
found defects the tests did not. That measurement layer is now a published library,
[`ragcite`](https://github.com/pcbeingused333/ragcite), which asserts that it reproduces the
numbers of the project it was extracted from. Fullstack background across Python, TypeScript
and Ruby, with production experience shipping and operating what I build. I also fix the
frameworks this work runs on — **91 merged pull requests** across 21 projects since July,
with a median of under a day to merge. The largest groups: 30 in **LangChain.rb**, most of its
LLM-provider and tool-calling layer; 12 in **Haystack** and its integrations, deepset's
framework for production RAG and agent pipelines (concurrency and async/sync-parity
defects); and the breakage Claude 5 and the 1.x Anthropic SDK caused in about a dozen LLM
projects, usually merged within hours.
<!--/long-->
<!--short:
Applied AI engineer in Python: two retrieval and agent systems in production, each shipping
the harness that measures it, and **91 merged pull requests** this year into the
frameworks they run on. My main project answers over the text of the **GDPR** under a
constraint generic RAG ignores — every statement names the provision it came from, and the
system declines when the source does not cover the question. In both projects the harness
found defects the tests did not. Fullstack across Python, TypeScript and Ruby; twelve of
those merged fixes are in **Haystack** and its integrations (deepset's RAG and agent
framework), concurrency and async/sync-parity defects, and 30 in **LangChain.rb**.
-->
<!--/ai-->
<!--swe:
Software engineer working across Python, TypeScript and Ruby, with **91 merged
pull requests** this year into open-source projects other teams build on: twelve in
**Haystack** and its integrations (deepset's RAG and agent framework), 30 in
**LangChain.rb**, nine in the Rails app **Sure** (personal finance, 10k★), two in Tencent's **WeKnora**, and fixes in Ruby tooling (`rubocop-rspec`, `courrier`, `perron`) and Python
libraries (`pydantic-ai`, `opik`, `phoenix`, `pipenv`, `pdm`) — concurrency, serialization and
error-handling defects. I build and deploy end to end: Python services with their own test
suites, Next.js front ends, AWS infrastructure in Terraform with CI/CD on GitHub Actions.
Earlier, fullstack Rails at TECNOBIT and teaching Ruby and SQL at Le Wagon. Before moving
to the Dominican Republic I founded and ran a business on my own in Toronto.
-->

---

## Skills

<!--ai-->
<!--long-->
**AI / LLM** — Python · LLM APIs (Groq, OpenAI-compatible) · LangChain · LangGraph ·
ReAct agents and tool use · **Model Context Protocol (MCP)**: building servers and
clients · **agent trajectory evaluation** (tool selection, ordering, argument accuracy,
answer grounding) · RAG: chunking strategy, retrieval tuning, **structure-aware
citation at the provision level** · **LLM evaluation**: known-answer datasets,
retrieval metrics (hit@1, recall@k, MRR), **abstention and unsupported-claim rate**,
LLM-as-judge for faithfulness / relevancy / correctness / context precision ·
cross-lingual retrieval · resilience to unreliable model output (retry with
rate-limit backoff, graceful degradation)

**Regulatory / legal text** — parsing legislative sources into citable provisions
(EUR-Lex / Official Journal markup) · citation integrity as a design constraint ·
evaluating refusal on out-of-corpus questions · GDPR structure (data subject rights,
controller and processor obligations, breach notification, administrative fines)

**Data & retrieval** — embeddings (`sentence-transformers`, BGE, MiniLM) · FAISS ·
PostgreSQL + `pgvector` · PDF ingestion pipelines · structured corpus construction

**Backend** — Python · pytest · Ruby on Rails · PostgreSQL · REST APIs · JSON/API
integrations (Jira API)

**Web** — TypeScript · Next.js · React · Tailwind · JavaScript · HTML/CSS/SCSS

**Infra & tooling** — **AWS** (Lambda container images, DynamoDB, ECR, IAM
least-privilege, CloudWatch, Budgets) · **Terraform** · **CI/CD with GitHub Actions,
OIDC federation** · Docker · Docker Compose · Vercel · Streamlit Community Cloud ·
Git (GitHub, GitLab) · AI-assisted development (Claude Code, Cursor)
<!--/long-->
<!--short:
**AI / LLM** — Python · LLM APIs (Groq, OpenAI-compatible) · LangChain · LangGraph ·
ReAct agents and tool use · **Model Context Protocol (MCP)**: building servers and
clients · **LLM evaluation**: known-answer datasets, retrieval metrics (hit@1, recall@k,
MRR), **abstention and unsupported-claim rate**, agent trajectory scoring, LLM-as-judge
for faithfulness / relevancy / correctness · RAG: chunking strategy, retrieval tuning,
**structure-aware citation at the provision level** · cross-lingual retrieval

**Regulatory / legal text** — parsing legislative sources into citable provisions
(EUR-Lex / Official Journal markup) · citation integrity as a design constraint ·
evaluating refusal on out-of-corpus questions · GDPR structure (data subject rights,
controller and processor obligations, breach notification, administrative fines)

**Data & retrieval** — embeddings (`sentence-transformers`, BGE) · FAISS · PostgreSQL +
`pgvector` · PDF ingestion pipelines · structured corpus construction

**Backend & web** — Python · pytest · Ruby on Rails · PostgreSQL · REST APIs · JSON/API
integrations (Jira API) · TypeScript · Next.js · React · Tailwind

**Infra & tooling** — **AWS** (Lambda container images, DynamoDB, ECR, IAM
least-privilege, CloudWatch) · **Terraform** · **CI/CD with GitHub Actions, OIDC
federation** · Docker · Vercel · Git · AI-assisted development (Claude Code, Cursor)
-->
<!--/ai-->
<!--swe:
**Backend** — Python · pytest · Ruby on Rails · PostgreSQL · REST APIs · JSON/API
integrations (Jira API)

**Web** — TypeScript · Next.js · React · Tailwind · JavaScript · HTML/CSS

**Infra & tooling** — **AWS** (Lambda container images, DynamoDB, ECR, IAM
least-privilege, CloudWatch) · **Terraform** · **CI/CD with GitHub Actions, OIDC
federation** · Docker · Vercel · Git (GitHub, GitLab) · AI-assisted development (Claude
Code, Cursor)

**AI / LLM** — LLM APIs · LangChain · LangGraph · agents and tool use · **Model Context
Protocol (MCP)** servers and clients · RAG with embeddings, FAISS and `pgvector` · LLM
evaluation
-->

---

## Experience

### Churrería Calderón — Founder & owner-operator · Toronto, Canada
**Sep 2025 – Jul 2026** *(business closed July 2026)*

<!--long-->
- Moved my churro business from Spain to Toronto on my own: signed a lease in Kensington
  Market, imported the production machinery, registered the business and obtained every
  permit needed to operate legally.
- Fitted out the store from my arrival in September 2025 and opened on 16 December, then
  ran it with no hires — production, service, customers, purchasing, cash and
  compliance — until it closed in July 2026.
<!--/long-->
<!--short:
- Moved my business from Spain to Toronto on my own: leased premises in Kensington Market,
  imported the machinery, registered the business and obtained every permit to operate
  legally. Opened in December 2025 and ran it with no hires — production, service,
  purchasing, cash and compliance — until it closed in July 2026.
-->

### Family churrería business — Manager · Catalonia, Spain
**2023 – Aug 2025** · mainly summer seasons *(and in the same business before that)*

<!--long-->
- Managed the family business, mainly through the summer seasons: production, service,
  customers, purchasing and cash.
- Took it from a mobile trailer to fixed premises, which meant rebuilding the
  operation around a different site, different hours and a different customer base.
- Also worked my father's stand on the fairground circuit.
- Years of reading what customers actually ask for, in person, hundreds of times a
  day. That is the same instinct a support-facing product feature needs, and it is
  why the AI widget I later built was scoped to the four questions people really ask.
<!--/long-->
<!--short:
- Managed the family business, mainly in the summer seasons — production, service,
  purchasing and cash — and took it from a mobile trailer to fixed premises, rebuilding the
  operation around a different site, hours and customer base.
-->

### Le Wagon — Part-time Programming Teacher · Remote (France)
**Oct 2022**

<!--long-->
- Taught on the new part-time flex cohort of the fullstack bootcamp: Ruby,
  object-oriented programming, SQL and PostgreSQL, HTML/CSS/JavaScript, and building
  on Ruby on Rails.
- Supported students through exercises and debugging during live sessions.
<!--/long-->
<!--short:
- Taught the new part-time flex cohort of the fullstack bootcamp — Ruby, OOP, SQL and
  PostgreSQL, HTML/CSS/JavaScript, Rails — through exercises and live debugging.
-->

### TECNOBIT (Grupo Oesía) — Fullstack Developer · Valdepeñas, Spain
**Aug 2022 – Nov 2022** · On-site

<!--long-->
- Shipped features into a long-running internal application maintained by a team of four
  engineers and a systems engineer.
- **Backend:** wrote Ruby routines that pulled data from JSON files and the **Jira API**,
  transformed it and persisted it to PostgreSQL; implemented multi-stage validation
  processes that gated document generation and downloads.
- **Frontend:** built form-driven pages and PostgreSQL-backed views with role-dependent
  data (users and managers saw different data), and surfaced the state of backend
  subprocesses so users could follow a document download to completion.
- Worked across a codebase distributed over both GitHub and GitLab.
<!--/long-->
<!--short:
- Shipped features into a long-running internal application maintained by a team of five,
  across a codebase distributed over both GitHub and GitLab.
- **Backend:** Ruby routines pulling data from JSON files and the **Jira API**, persisting
  it to PostgreSQL with multi-stage validation gating document generation and downloads.
  **Frontend:** form-driven pages and PostgreSQL-backed views with role-dependent data,
  surfacing subprocess state so users could follow a download to completion.
-->

---

## Selected projects

### Business Ops Agent — MCP server + agent, with trajectory evaluation
[Live demo](https://mcp-business-agent-8wawhyaqt2flfixqj8dpnk.streamlit.app) · [Code](https://github.com/pcbeingused333/mcp-business-agent)

A **Model Context Protocol server** exposing a business's operations (catalog, booking
capacity, stock, quoting, orders) as tools any MCP client can call — Claude Desktop, Cursor,
or the LangGraph agent bundled with it. The agent carries no business rules: tools are
discovered at runtime, so adding one requires no agent change.

<!--long-->
- Built an evaluation harness that scores **tool trajectories**, not just answers:
  which tools were called, in what order, with which arguments, and whether every
  figure in the reply traces back to a tool result. The grounding check needs no judge
  model and is therefore deterministic and free — it holds even when a fabricated
  number happens to be correct.
- The harness caught the agent answering "I don't have that information" with zero
  tool calls, and caught it **intermittently**, which single-run testing misses;
  scenarios can be repeated to measure flaky behaviour. Scored 11/12, mean 0.98.
- Chose not to use `langchain-mcp-adapters`: it pins `mcp<2` and would have forced a
  working server back to an older SDK. Wrote a 60-line bridge instead, passing the
  server's JSON Schema straight through so no tool signature is duplicated.
- **Deployed it to AWS** as a remote MCP server — Lambda container behind a Function
  URL, DynamoDB single-table store, least-privilege IAM, all in Terraform. Storage sits
  behind an interface, so the same server runs on SQLite locally and DynamoDB in
  production with no change above the backend.
- CI/CD on every push to main via GitHub Actions, authenticating with **OIDC** rather
  than a stored access key, and scoped to one branch so a fork's pull request cannot
  assume the deploy role. The role deliberately cannot apply infrastructure: it can
  ship an image and repoint the function, nothing more.
- Python, MCP 2.0, LangGraph, Groq, AWS (Lambda, DynamoDB, ECR, IAM), Terraform,
  Docker, GitHub Actions, pytest (161 tests).
<!--/long-->
<!--short:
- Built an evaluation harness that scores **tool trajectories**, not just answers: which
  tools were called, in what order, with which arguments, and whether every figure in the
  reply traces back to a tool result — deterministic, no judge model, so it holds even
  when a fabricated number happens to be correct. It caught the agent answering with zero
  tool calls, and caught it **intermittently**, which single-run testing misses. 11/12,
  mean 0.98.
- **Deployed to AWS** as a remote MCP server — Lambda container behind a Function URL,
  DynamoDB single-table store, least-privilege IAM, all in Terraform. Storage sits behind
  an interface, so the same server runs on SQLite locally and DynamoDB in production.
- Python, MCP 2.0, LangGraph, Groq, AWS (Lambda, DynamoDB, ECR, IAM), Terraform, Docker,
  pytest (161 tests). CI/CD on every push via GitHub Actions authenticating with **OIDC**
  rather than a stored key, scoped to one branch and unable to apply infrastructure.
-->

### Ask the GDPR — retrieval over regulation, with citations that can be checked
[Live demo](https://rag-chatbot-demo-0.streamlit.app) · [Code](https://github.com/pcbeingused333/rag-chatbot-portfolio)

LangGraph agent over the full text of the GDPR. Every answer names the provision behind it —
`Art. 33(1)`, not a page number — and the system declines when the source does not cover the
question. Two modes behind one flag: an in-memory FAISS demo on a free 1 GB container, and a
pgvector-backed production path.

<!--long-->
- **Made the citation structural rather than incidental.** A regulation is cited by
  article and paragraph; the page a provision lands on is an artefact of typesetting,
  and a reader sent to "page 14" can confirm nothing. So the corpus is not a PDF: a
  builder parses the Official Journal text from EUR-Lex (not a mirror — in a system
  whose claim is checkable citations, the text has to come from the authority the
  citation names) into **414 provisions** carrying article, paragraph, title and
  chapter as metadata. The chunk size was then chosen so that **97% of provisions
  survive as exactly one chunk**, because a chunk straddling Art. 33(1) and 33(2) gets
  attributed to one of them and cites the wrong paragraph.
- **Built an eval for the answers that should never be given.** In legal text a
  retrieval miss announces itself; an invention is fluent, confident and
  indistinguishable from a correct answer, and a citation the model reasoned its way to
  rather than read makes it more convincing. So the harness scores refusal against
  questions the Regulation does not answer but every model has read about — adequacy
  decisions by country, the text of the standard contractual clauses, Schrems II, a
  CCPA penalty — alongside a deterministic check for citations that appear in the
  answer but never in the retrieved passages. Every question scored so far declined
  correctly and specifically, naming the provision that creates the mechanism and
  stating that the detail asked for is not in the text; none produced an unsupported
  answer or a citation that was never retrieved.
- Changed the ground truth from matching text to **matching the cited provision**,
  which is stricter (retrieving the right words is not retrieving the right authority)
  and removes the chunk-boundary false misses the substring approach suffered.
- **Re-ran every measurement when the corpus changed, and one result reversed.**
  Embedding the article heading measurably *hurt* retrieval under the old embedding
  model and measurably *helped* under the new one; carrying the first conclusion
  forward would have shipped the worse setting on the strength of real evidence. The
  model swap itself was worth 8/20 → 13/20 at rank 1 for 42 MB of RAM, against a hard
  1 GB ceiling measured with the index loaded, not just the model.
- Three parse bugs caught by sanity checks that now block the build: the closing
  article silently absorbing the signatures and all 21 footnotes, nested sub-points
  truncated by a non-greedy regex that could not handle nested markup, and the 26
  definitions of Art. 4 collapsing into one uncitable record.
- Fixed cross-lingual retrieval (Spanish 0/4 at rank 1 against an English index) by
  translating the retrieval query rather than paying ~350 MB for a multilingual
  embedding model that did not fit the 1 GB budget — a measured trade-off.
- CI on every push runs the suite headlessly, including a boot test of the app itself
  — the host redeploys straight from `main`, so the suite is the only gate before the
  public demo. One test forces the embedding loader to raise and asserts the first
  render still succeeds, proving nothing heavy sits on the render path.
- Python, LangChain, LangGraph, Groq, FAISS, pgvector, Streamlit, Docker, GitHub
  Actions, pytest (72 tests).
<!--/long-->
<!--short:
- **Made the citation structural rather than incidental.** A regulation is cited by
  article and paragraph; the page a provision lands on is an artefact of typesetting. So
  the corpus is not a PDF: a builder parses the Official Journal text from EUR-Lex into
  **414 provisions** carrying article, paragraph and chapter as metadata, and the chunk
  size was chosen so **97% survive as exactly one chunk** — a chunk straddling Art. 33(1)
  and 33(2) cites the wrong paragraph.
- **Built an eval for the answers that should never be given.** In legal text a retrieval
  miss announces itself; an invention is fluent and indistinguishable from a correct
  answer. The harness scores refusal against questions the Regulation does not answer but
  every model has read about — adequacy decisions, Schrems II, a CCPA penalty — plus a
  deterministic check for citations that appear in the answer and never in the passages.
- **Re-ran every measurement when the corpus changed, and one result reversed.** Embedding
  the article heading hurt retrieval under the old embedding model and helped under the
  new one; carrying the first conclusion forward would have shipped the worse setting on
  the strength of real evidence. The model swap was worth 8/20 → 13/20 at rank 1 for
  42 MB, against a hard 1 GB ceiling.
- Python, LangChain, LangGraph, Groq, FAISS, pgvector, Streamlit, Docker, GitHub Actions,
  pytest (72 tests). CI runs headlessly on every push, including a boot test of the app —
  the host redeploys straight from `main`, so the suite is the only gate before the demo.
-->

### ragcite — the evaluation layer of the two projects above, as a library
[Code](https://github.com/pcbeingused333/ragcite)

Retrieval metrics, citation grounding, abstention scoring and tool-trajectory scoring,
extracted from the two harnesses above and generalized. No LangChain, vector store or LLM
client is imported: you bring the retriever and the judge, `ragcite` scores what they return.

<!--long-->
- **It reproduces the numbers of the project it came from, and asserts it.** The dogfood
  example scores one FAISS index twice — once with `ragcite`, once with the original
  project's own independent metrics code — and exits non-zero if they disagree. They match
  exactly (hit@1 13/25, recall@k 17/25, MRR 0.59), which is what makes "extracted from a
  production harness" a check rather than a claim.
- Retrieval and grounding need no model at all: `hit@1`/`recall@k`/`MRR` are id matching
  and grounding is a set membership test, so both are deterministic and free to run on
  every commit. A fabricated citation is caught however fluently it reads.
- `--min-hit-at-1`, `--min-recall`, `--min-mrr` turn a run into a CI gate that exits 2 on
  a regression. Without a threshold flag the command always exits 0 — a report, not a
  gate, and it stays that way by default.
- `check_judge_independence` refuses to run when the judge and the system under test are
  the same model. That defect is why it exists: my own harness spent weeks marking a model
  as its own examiner.
- Zero runtime dependencies, MIT, 155 tests, CI on Python 3.9–3.12.
<!--/long-->
<!--short:
- **It reproduces the numbers of the project it came from, and asserts it.** The dogfood
  example scores one FAISS index twice — once with `ragcite`, once with the original
  project's own independent metrics code — and exits non-zero if they disagree. They match
  exactly (hit@1 13/25, recall@k 17/25, MRR 0.59).
- Zero runtime dependencies, MIT, 155 tests, CI on Python 3.9–3.12. `--min-hit-at-1` turns
  a run into a CI gate that exits 2 on a regression.
-->

<!--long-->
### AI Website Chat Widget — embeddable business assistant
[Live demo](https://ai-chat-widget-five-ashen.vercel.app) · [Code](https://github.com/pcbeingused333/ai-chat-widget)

Drop-in chat widget for small-business sites, grounded strictly in the business's own
content. Reusable for any client from a single config file.
Next.js, React, TypeScript, Tailwind, Groq, Vercel.

### Semantic Recommender — embedding-based recommendations
[Code](https://github.com/pcbeingused333/semantic-recommender)

Recommendation engine built on vector embeddings with a feedback loop that refines
results over time, as a reusable backend for platforms that have outgrown rule-based
filters. Python, embeddings, pgvector, PostgreSQL.
<!--/long-->


---

## Open source

<!--long-->
**91 merged pull requests across 21 open-source projects since July 2026** — Haystack,
LangChain.rb, Sure, pipenv, Arize Phoenix, Opik, TruLens, pydantic-ai, Tencent's WeKnora and others.
Median time to merge is under a day; 50 merged within 24 hours. Most are fixes I found by reading
the code or tracking a provider change rather than picking from an issue tracker, and each
ships a regression test I verified fails with the fix reverted. They fall into five patterns:

- **When the LLM provider changes, the code built on it breaks.** Claude 5 and the 1.x
  Anthropic SDK broke the same few assumptions in about a dozen projects: reading a reply as
  `content[0].text` when the first block is now a `thinking` block; sending `temperature` or a
  forced `tool_choice` that current models reject with a 400; calling the removed Text
  Completions API; and model catalogs that didn't recognise new or Bedrock model IDs. Merged
  in hostedgpt, reward-bench, TruLens, chatlas, WeKnora and LangChain.rb, with a median of
  about eight hours to merge, because users were hitting them that week. Examples:
  [`Tencent/WeKnora` #4155](https://github.com/Tencent/WeKnora/pull/4155) — internal pipelines (query
  understanding, entity extraction, compaction) got a 400 on six Claude models catalogued as
  accepting sampling parameters; [`AllYourBot/hostedgpt` #823](https://github.com/AllYourBot/hostedgpt/pull/823) —
  auto-titling read the first content block and got `nil`, intermittently, because adaptive
  thinking skips short prompts.
- **Async paths in Haystack that drifted from the sync ones.** `run_async` implementations
  that ran blocking work on the event loop, held an `asyncio.Lock` across event loops,
  ignored `max_workers`, skipped batching, or re-wrapped errors the sync path re-raises. These
  bugs hide from test suites that only call `run`. Eight merged, plus four `to_dict`
  fixes from an AST audit of `__init__` against serialization, where a setting
  silently reverted when a pipeline was reloaded. Examples:
  [`haystack-core-integrations` #3790](https://github.com/deepset-ai/haystack-core-integrations/pull/3790)
  (the lock, reported first as #3789),
  [`haystack` #12662](https://github.com/deepset-ai/haystack/pull/12662) (50 expanded queries meant 50
  concurrent embedding calls whatever the limit). Written up as
  [Four concurrency bugs on Haystack's async path](https://portfolio-alexgonzalez33.vercel.app/writing/haystack-async-concurrency).
- **The provider and tool-calling layer of LangChain.rb.** 30 merged, usually the same day,
  across its Anthropic, OpenAI, Gemini, Ollama, Cohere and Mistral adapters: `tool_choice`
  `"none"`/`"auto"` sent in the shape each API expects, an agent loop that could never stop
  calling a forced tool, streamed tool calls lost on Ollama, thinking blocks dropped from the
  tool-use loop, a migration to the cohere-ruby 1.0 (v2) API, and tool errors returned to the
  LLM instead of ending the run. Examples:
  [#1063](https://github.com/patterns-ai-core/langchainrb/pull/1063),
  [#1058](https://github.com/patterns-ai-core/langchainrb/pull/1058);
  [all of them](https://github.com/patterns-ai-core/langchainrb/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged).
- **One rare but legitimate input that brings down the whole flow.** An empty `choices`
  list, a `nil` body, a division by zero, a bare `%` in an email layout — often inside a
  `rescue`/`except` written to catch a different exception. Merged across LangChain.rb and
  three Ruby gems: [`courrier`](https://github.com/Rails-Designer/courrier/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged)
  (11 merged, including three new providers and cc/bcc that six providers silently dropped),
  [`perron`](https://github.com/Rails-Designer/perron/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged)
  (4) and [`icons`](https://github.com/Rails-Designer/icons/pulls?q=is%3Apr+author%3Apcbeingused333) (2);
  open in instructor, openinference and guardrails.
- **Evaluation metrics that return a wrong number without failing.** Retrieval metrics above
  1.0 on rankings with repeated ids, pass@k averaged as pass/fail, a Spearman correlation
  computed on rankings with duplicates, an eval case that could never fail. Merged in
  [`opik` #8276](https://github.com/comet-ml/opik/pull/8276),
  [`phoenix` #16002](https://github.com/Arize-ai/phoenix/pull/16002) and
  [`pydantic-ai` #7936](https://github.com/pydantic/pydantic-ai/pull/7936); five open in
  [`llama-index-core`](https://github.com/run-llama/llama_index/pulls?q=is%3Apr+author%3Apcbeingused333)
  and four in [`deepeval`](https://github.com/confident-ai/deepeval/pulls?q=is%3Apr+author%3Apcbeingused333).
  [`pydantic-ai` #7927](https://github.com/pydantic/pydantic-ai/issues/7927), a judge grading binary
  output rendered as one decimal byte per line, was reported with a reproduction and
  accepted.

Also merged: nine in the Rails app [`we-promise/sure`](https://github.com/we-promise/sure/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged)
(personal finance, 10k★: provider-setup flows from Add Account, wrong HTTP methods, data kept
when merging duplicates); four in [`pipenv`](https://github.com/pypa/pipenv/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged)
and one in [`pdm`](https://github.com/pdm-project/pdm/pull/3931) (PEP 751 `pylock.toml` and inline script
metadata); token usage of failed Responses API calls in [`pipecat`](https://github.com/pipecat-ai/pipecat/pull/6215);
Ruby and Rails tooling — two in [`rubocop-rspec`](https://github.com/rubocop/rubocop-rspec/pull/2209)
and a drop-down ordering fix in [`human-essentials`](https://github.com/rubyforgood/human-essentials/pull/5656)
— and two in [`pyfenn/fenn`](https://github.com/pyfenn/fenn/pull/277).
[Every pull request, open and closed](https://github.com/pulls?q=is%3Apr+author%3Apcbeingused333).

**What worked:** small PRs with a failing-first regression test and the local verification
pasted in; answering reviews quickly; going back to maintainers who already trusted the
work (LangChain.rb went from 6 to 30 merged); and fixing what a release had just broken.
**What didn't:** crowded repos where the maintainer fixes it first, and repos where CI never
runs for fork PRs.
<!--/long-->
<!--short:
**91 merged pull requests across 21 open-source projects since July 2026** (Haystack,
LangChain.rb, Sure, pipenv, Phoenix, Opik, pydantic-ai, WeKnora), median under a day to merge, each
with a regression test verified to fail without the fix:

- **Provider changes:** Claude 5 and the 1.x Anthropic SDK broke the same assumptions in
  about a dozen LLM projects (`content[0].text` vs thinking blocks, rejected `temperature` or
  forced `tool_choice`, removed APIs, Bedrock IDs). Merged in WeKnora, TruLens, hostedgpt,
  reward-bench, chatlas and LangChain.rb, median about eight hours
  (e.g. [WeKnora #4155](https://github.com/Tencent/WeKnora/pull/4155)).
- **Haystack async paths:** `run_async` drifting from `run` — blocking calls on the event
  loop, a lock shared across loops, `max_workers` ignored. Eight merged, plus four `to_dict`
  fixes from an AST audit
  ([write-up](https://portfolio-alexgonzalez33.vercel.app/writing/haystack-async-concurrency)).
- **LangChain.rb's provider and tool-calling layer:** [30 merged](https://github.com/patterns-ai-core/langchainrb/pulls?q=is%3Apr+author%3Apcbeingused333+is%3Amerged),
  usually the same day, across six provider adapters.
- **Edge cases that crash the whole flow:** empty `choices`, `nil`, division by zero —
  courrier (11), perron (4), icons (2).
- **Eval metrics that are silently wrong:** merged in opik, phoenix and pydantic-ai; open in
  llama-index-core and deepeval.
-->

---

## Education

<!--long-->
**Le Wagon** — Fullstack Web Development bootcamp · 2022
Ruby, Ruby on Rails, JavaScript, SQL/PostgreSQL, HTML/CSS.

**Self-directed, 2022 – 2025** — LaunchSchool coursework, coding challenges and
independent study alongside running the business, before moving back into
engineering full time.
<!--/long-->
<!--short:
**Le Wagon** — Fullstack Web Development bootcamp, 2022. Self-directed study since.
-->
