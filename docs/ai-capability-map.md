# AI Capability Map

| Capability | Intent (user) | Inputs (this sprint) | Risk 1–5 (tag) | p95 ms | Est. cost/action | Fallback | Selected |
|---|---|---|---|---:|---:|---|:---:|
| Search typeahead | Quickly find products while typing | SKU titles, tags, precomputed embeddings | 2 | 300 | $0.03 | Keyword match | yes |
| Support assistant | Answer FAQ & order-status queries | Policies.md, order-status API | 3 | 1200 | $0.21 | FAQ search + human escalation | yes |
| Personalized recommendations | Recommend products based on session | Recent session events, last-30d views | 4 | 800 | $0.04 | Generic bestsellers |  |
| Review summarizer | Summarise product reviews | Top reviews per SKU | 3 | 900 | $0.01 | Show raw reviews |  |

## Why these two
We selected **Search typeahead** and **Support assistant** because they map directly to immediate KPIs: faster discovery increases conversion, and automated answers reduce support tickets. Both use existing data (catalog metadata + FAQ markdown + order-status API), so integration risk is low and a small prototype will validate feasibility fast.
