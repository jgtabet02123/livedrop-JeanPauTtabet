# Cost Model

## Assumptions
- Model: GPT-4o-mini at $0.15/1K prompt tokens, $0.60/1K completion tokens
- Typeahead: Avg tokens in 20, Avg tokens out 40
- Support: Avg tokens in 600, Avg tokens out 200
- Requests/day: Typeahead 50,000; Support 1,000
- Cache hit rate: Typeahead 70%; Support 30%

## Calculation
Cost/action = (tokens_in/1000 * prompt_price) + (tokens_out/1000 * completion_price)

### Typeahead
- Cost/action = (20/1000 × 0.15) + (40/1000 × 0.60) = $0.003 + $0.024 = **$0.027**
- Daily cost = 50,000 × 0.027 × (1 - 0.70) = **$405/day**

### Support Assistant
- Cost/action = (600/1000 × 0.15) + (200/1000 × 0.60) = $0.09 + $0.12 = **$0.21**
- Daily cost = 1,000 × 0.21 × (1 - 0.30) = **$147/day**

## Results
- Typeahead daily ≈ **$405**
- Support daily ≈ **$147**

## Cost lever if over budget
- Switch model to Llama 3.1 8B (example: $0.05/1K prompt, $0.20/1K completion) for ~3× savings.
- Reduce prompt size (shorter retrieval chunks).
- Increase cache hit rate via TTL tuning and query normalization.
