# AI Touchpoints

## 1. Search Typeahead

**Problem statement**  
Users struggle to find products quickly in ~10k SKUs; misspellings and natural-language queries cause drop-off that hurts conversion.

**Happy path**
1. User types 2+ characters in the search box.
2. Client sends a fragment to backend endpoint: `POST /api/typeahead?q=...`.
3. Backend checks a query cache (70% hit assumed).
4. If cache miss, backend embeds query and performs a vector search on precomputed SKU embeddings.
5. Backend returns top 5 suggestions to client.
6. Client displays suggestions; user clicks suggestion and opens product page.
7. Events logged for CTR and latency.

**Grounding & guardrails**  
- Source of truth: SKU titles, tags, categories from product DB.  
- Retrieval scope: product metadata only (no user PII).  
- Max context: query fragment ≤ 20 tokens.  
- Refuse: open-ended user Qs (route to support).

**Human-in-the-loop**  
- Offline: weekly review of low-CTR queries; product manager adjusts synonyms.  
- No live escalation.

**Latency budget**
- Cache lookup: 40–60 ms  
- Embedding generation: 100–150 ms (if not cached)  
- Vector search: 60–100 ms  
- Response formatting + network: 30–50 ms  
- **Target p95 ≤ 300 ms** (70% cache hit helps achieve this)

**Error & fallback behavior**  
- If LLM/embedding service down → fallback to exact substring/keyword search.  
- If query empty → show trending products.

**PII handling**  
- No PII sent to model. Queries logged without user id (or hashed).  
- No order/customer data used.

**Success metrics**
- Product: Typeahead CTR = clicks on suggestions / suggestions shown.
- Product: p95 latency ≤ 300 ms.
- Business: Conversion uplift = (orders from sessions with typeahead clicks / total sessions) − baseline.

**Feasibility note**  
Precompute embeddings for 10k SKUs and store in vector DB (pgvector, Pinecone). Next prototype: build a minimal endpoint against 1k sample SKUs and measure 95th percentile latency.

---

## 2. Support Assistant

**Problem statement**  
Customers frequently ask the same FAQ and order-status questions. A grounded assistant reduces load on live agents and improves time-to-answer.

**Happy path**
1. User opens Help chat and types a question (e.g., "Where is my order #1234?").
2. Client sends request to backend with optional order id.
3. Backend tries FAQ cache (30% hit assumed).
4. If cache miss, retrieval pulls relevant chunks from Policies.md (chunked to ≤1000 tokens) and calls `order-status` API if an order id is provided.
5. Compose prompt that includes: system instructions, retrieved policy chunks, order status snippet (if present), and user's question (max context 1500 tokens).
6. Call LLM for answer; get completion ≤200 tokens.
7. Return answer to user with a “confidence” score. If below threshold or user asks to escalate, offer “Talk to agent”.
8. Log outcome (escalated yes/no, resolution).

**Grounding & guardrails**  
- Source of truth: Policies.md (FAQ), order-status API.  
- Retrieval scope: FAQ + order metadata only.  
- Max context: 1500 tokens.  
- Refuse: financial/legal advice, product recommendations outside policies.

**Human-in-the-loop**  
- Escalate when LLM confidence < 0.6 or when user requests agent.  
- UI: “Escalate to agent” button; copies current chat transcript to agent.  
- Reviewer: Support team; SLA for agent response < 1 hour during business hours.

**Latency budget**
- Cache lookup: 80–120 ms  
- Retrieval + order API call: 150–300 ms (order API variability)  
- Prompt build: 30–80 ms  
- LLM inference: 600–800 ms  
- Response render: 50–100 ms  
- **Target p95 ≤ 1200 ms** (30% cache hit)

**Error & fallback behavior**  
- If LLM fails or retrieval empty → show top FAQ results and “contact support” CTA.  
- If order API times out → inform user and offer to escalate.

**PII handling**  
- Do not send user name/email. Only send order id and minimal order fields (status, ETA) to LLM; mask any full payment info.  
- Logs store redacted order id (hash) and question text; do not store full payment card or address.

**Success metrics**
- Product: Self-serve answer rate = answers not escalated / total chats.
- Product: p95 latency ≤ 1200 ms.
- Business: Support contact deflection = (baseline tickets − current tickets) / baseline tickets.

**Feasibility note**  
Policies.md and `order-status` API already exist; models available via hosted API (GPT-4o-mini) or Llama 3.1 via OpenRouter. Next step: run a 100-query probe to measure answer quality and latency.
