# Alex Castillo González

**Applied AI Engineer · Python / LLM**

Remote — UTC−4 · Spanish (native), English (professional)
[alex.castillog33@gmail.com](mailto:alex.castillog33@gmail.com) · [GitHub](https://github.com/pcbeingused333) · [LinkedIn](https://www.linkedin.com/in/alex-castillo-gonzalez-65a13110a/) · [portfolio-alexgonzalez33.vercel.app](https://portfolio-alexgonzalez33.vercel.app)

---

## Summary

Applied AI engineer working in Python on retrieval and agent systems, and on the layer
that decides whether they survive real users: evaluation, failure handling, and knowing
which numbers actually moved. Both of my main projects ship with the harness that
measures them — retrieval and answer quality for the RAG system, tool trajectories and
answer grounding for the MCP agent — and in each case the harness found defects the
tests did not. Fullstack background across Python, TypeScript and Ruby, with production
experience shipping and operating what I build. Two merged upstream contributions to
`pyfenn/fenn`, a Python framework for ML workflows and LLM agents.

---

## Skills

**AI / LLM** — Python · LLM APIs (Groq, OpenAI-compatible) · LangChain · LangGraph ·
ReAct agents and tool use · **Model Context Protocol (MCP)**: building servers and
clients · **agent trajectory evaluation** (tool selection, ordering, argument accuracy,
answer grounding) · RAG: chunking strategy, retrieval tuning, page-level source
citations · **LLM evaluation**: known-answer datasets, retrieval metrics (hit@1,
recall@k, MRR), LLM-as-judge for faithfulness / relevancy / correctness / context
precision · cross-lingual retrieval · resilience to unreliable model output (retry,
graceful degradation)

**Data & retrieval** — embeddings (`sentence-transformers`, BGE, MiniLM) · FAISS ·
PostgreSQL + `pgvector` · PDF ingestion pipelines

**Backend** — Python · pytest · Ruby on Rails · PostgreSQL · REST APIs · JSON/API
integrations (Jira API)

**Web** — TypeScript · Next.js · React · Tailwind · JavaScript · HTML/CSS/SCSS

**Infra & tooling** — **AWS** (Lambda container images, DynamoDB, ECR, IAM
least-privilege, CloudWatch, Budgets) · **Terraform** · **CI/CD with GitHub Actions,
OIDC federation** · Docker · Docker Compose · Vercel · Streamlit Community Cloud ·
Git (GitHub, GitLab) · AI-assisted development (Claude Code, Cursor)

---

## Experience

### Churrería Calderón — Family business · Toronto, Canada
**Oct 2025 – Jul 2026** *(business closed July 2026)*

- **Developer:** built and deployed the business website, plus an embeddable AI chat
  widget that answered customer questions on menu, hours, location and FAQs, grounded
  only in the business's own information so it would not invent details. Built the
  widget to be reusable across clients from a single configuration file. Next.js,
  React, TypeScript, Tailwind, Groq, Vercel.
- Shipped both during the setup period before the December 2025 opening, so the site
  and the assistant were live on day one rather than added later.
- Worked in day-to-day operations of the business throughout, which is where the
  judgement about which problems are worth automating — and which are not — came from.

### Family churrería business — Owner-operator · Catalonia, Spain
**2023 – 2026** *(and in the same business before that)*

- Ran the business single-handed: production, service, customers, purchasing, cash
  and compliance. No staff to delegate to and no manager to escalate to — if it did
  not work, it was mine to fix that morning.
- Took it from a mobile trailer to fixed premises, which meant rebuilding the
  operation around a different site, different hours and a different customer base.
- Also worked my father's stand on the fairground circuit.
- Years of reading what customers actually ask for, in person, hundreds of times a
  day. That is the same instinct a support-facing product feature needs, and it is
  why the AI widget I later built was scoped to the four questions people really ask.

### Le Wagon — Part-time Programming Teacher · Remote (France)
**Oct 2022**

- Taught on the new part-time flex cohort of the fullstack bootcamp: Ruby,
  object-oriented programming, SQL and PostgreSQL, HTML/CSS/JavaScript, and building
  on Ruby on Rails.
- Supported students through exercises and debugging during live sessions.

### TECNOBIT (Grupo Oesía) — Fullstack Developer · Valdepeñas, Spain
**Aug 2022 – Nov 2022** · On-site

- Shipped features into a long-running internal application maintained by a team of four
  engineers and a systems engineer.
- **Backend:** wrote Ruby routines that pulled data from JSON files and the **Jira API**,
  transformed it and persisted it to PostgreSQL; implemented multi-stage validation
  processes that gated document generation and downloads.
- **Frontend:** built form-driven pages and PostgreSQL-backed views with role-dependent
  data (users and managers saw different data), and surfaced the state of backend
  subprocesses so users could follow a document download to completion.
- Worked across a codebase distributed over both GitHub and GitLab.

---

## Selected projects

### Business Ops Agent — MCP server + agent, with trajectory evaluation
[Live demo](https://mcp-business-agent-8wawhyaqt2flfixqj8dpnk.streamlit.app) · [Code](https://github.com/pcbeingused333/mcp-business-agent)

A **Model Context Protocol server** exposing a business's operations (catalog, booking
capacity, stock, quoting, orders) as tools any MCP client can call — Claude Desktop,
Cursor, or the LangGraph agent bundled with it. The agent carries no business rules;
tools are discovered at runtime, so adding one requires no agent change.

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

### RAG Chatbot — retrieval assistant with verifiable citations
[Live demo](https://rag-chatbot-demo-0.streamlit.app) · [Code](https://github.com/pcbeingused333/rag-chatbot-portfolio)

LangGraph agent over PDF documents; every answer carries its source file and page number.
Ships in two modes behind one flag: an in-memory FAISS demo that runs on a free 1 GB
container with no database, and a pgvector-backed production path.

- Built the project's **evaluation harness**: 17 known-answer questions across three
  languages, scoring retrieval (hit@1, recall@k, MRR), cross-lingual retrieval, peak
  memory per embedding model, end-to-end answer quality (LLM-as-judge: faithfulness by
  claim decomposition, relevancy, correctness, context precision) and raw tool-call
  failure rate. Every figure in the README is regenerated by a command, not measured
  by hand.
- Measurement caught three defects that unit tests could not. Production-sized chunks
  split the corpus into fewer pieces than the retrieval `k`, so recall@k read a perfect
  100% while retrieval returned the whole document and filtered nothing — only hit@1
  exposed it. Spanish queries reached the correct passage 0/4 against an English index.
  The agent refused an ordinary customer question as off-topic without ever calling its
  retrieval tool; fixing that moved grounded retrieval 16/17 → 17/17 and faithfulness
  0.87 → 0.96.
- Fixed cross-lingual retrieval by translating the retrieval query rather than paying
  ~600 MB for a multilingual embedding model that did not fit the deployment's 1 GB
  budget — a measured trade-off, not a preference.
- CI on every push runs the suite headlessly, including a boot test of the app itself
  — the host redeploys straight from `main`, so the suite is the only gate before the
  public demo. One test forces the embedding loader to raise and asserts the first
  render still succeeds, proving nothing heavy sits on the render path.
- Python, LangChain, LangGraph, Groq, FAISS, pgvector, Streamlit, Docker, GitHub
  Actions, pytest (66 tests).

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

---

## Open source

**Merged**

- [`pyfenn/fenn` #277](https://github.com/pyfenn/fenn/pull/277) — added `.docx` support to
  the RAG document loader, so the framework ingests Word documents alongside PDFs and text.
- [`pyfenn/fenn` #286](https://github.com/pyfenn/fenn/pull/286) — corrected the RAG
  optional-dependency install instructions, which referenced a package name that does
  not exist.

**Open**

- [`rubocop/rubocop-rspec` #2209](https://github.com/rubocop/rubocop-rspec/pull/2209) —
  fixed a crash in `RSpec/LeadingSubject` on Ruby 3.4's implicit `it` block parameter: the
  cop only walked `:block` AST ancestors and hit `nil` on the new `itblock`/`numblock`
  nodes. Widened the lookup to `:any_block`, with a regression spec.
- [`rubocop/rubocop-rspec` #2214](https://github.com/rubocop/rubocop-rspec/pull/2214) —
  fixed `RSpec/LeadingSubject` autocorrecting a subject to a position above another
  subject.
- [`rubocop/rubocop-performance` #529](https://github.com/rubocop/rubocop-performance/pull/529) —
  fixed `Performance/ConstantRegexp` emitting invalid code when autocorrecting a regexp
  used as a pattern in `case`/`in` pattern matching.
- [`Rails-Designer/courrier`](https://github.com/Rails-Designer/courrier/pulls?q=is%3Apr+author%3Apcbeingused333) —
  four PRs: MailerSend, Mailtrap and SMTP.com provider integrations, and a `NameError`
  fix affecting Mailgun and Mailjet on Ruby 3.4.

---

## Education

**Le Wagon** — Fullstack Web Development bootcamp · 2022
Ruby, Ruby on Rails, JavaScript, SQL/PostgreSQL, HTML/CSS.

**Self-directed, 2022 – 2025** — LaunchSchool coursework, coding challenges and
independent study alongside running the business, before moving back into
engineering full time.
