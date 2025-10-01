# RAG System Evaluation



## 1. Retrieval Quality Tests (10 tests)

| Test ID | Question | Expected Documents | Pass Criteria |
|---------|----------|-------------------|---------------|
| R01 | How do I reset my Shoplite password? | [doc 12] | Retrieved docs contain expected titles |
| R02 | What is the checkout process for Shoplite orders? | [doc 4] | Retrieved docs are relevant to question |
| R03 | How are discounts applied during checkout? | [doc 16] | Retrieved docs are relevant to question |
| R04 | How do I update my shipping address? | [doc9] | Retrieved docs contain expected titles |
| R05 | What payment methods are supported? | [doc 5] | Retrieved docs are relevant to question |
| R06 | How to return an item on Shoplite? | [doc 7] | Retrieved docs contain expected titles |
| R07 | How to track an order? | [doc 6] | Retrieved docs are relevant to question |
| R08 | How to contact customer support? | [doc 12]| Retrieved docs contain expected titles |
| R09 | How to enable two-factor authentication? | none | Retrieved docs are not relevant to question |
| R10 | How to cancel a subscription? | none | Retrieved docs are not relevant to question |

---

## 2. Response Quality Tests (15 tests)

| Test ID | Question | Required Keywords | Forbidden Terms | Expected Behavior |
|---------|----------|------------------|-----------------|------------------|
| Q01 | How do I reset my password? | ["reset", "password"] | ["hack", "guess"] | Direct answer with citation |
| Q02 | Explain the checkout process including discounts. | ["checkout", "discounts"] | ["speculation"] | Multi-source synthesis |
| Q03 | What are supported payment methods? | ["credit card", "PayPal"] | ["unofficial", "wrong"] | Direct answer with citation |
| Q04 | How to track my order status? | ["tracking", "order"] | ["guess"] | Direct answer with citation |
| Q05 | How do I return a purchased item? | ["return", "item"] | ["hack", "exploit"] | Direct answer with citation |
| Q06 | How to update shipping address? | ["update", "shipping"] | ["speculation"] | Direct answer with citation |
| Q07 | How to contact customer support? | ["support", "contact"] | ["unofficial"] | Direct answer with citation |
| Q08 | How to enable two-factor authentication? | ["2FA", "security"] | ["guess"] | Direct answer with citation |
| Q09 | How to cancel subscription? | ["cancel", "subscription"] | ["speculation"] | Direct answer with citation |
| Q10 | What documents are needed for returns? | ["documents", "returns"] | ["guess"] | Multi-source synthesis |
| Q11 | How to change account email? | ["email", "update"] | ["speculation"] | Direct answer with citation |
| Q12 | How to redeem discount codes? | ["redeem", "discount"] | ["hack"] | Direct answer with citation |
| Q13 | How to apply multiple discounts? | ["multiple", "discounts"] | ["guess"] | Multi-source synthesis |
| Q14 | How to delete my Shoplite account? | ["delete", "account"] | ["speculation"] | Direct answer with citation |
| Q15 | How to reset password with forgotten email? | ["reset", "forgotten email"] | ["guess"] | Direct answer with citation |

---

## 3. Edge Case Tests (5 tests)

| Test ID | Scenario | Expected Response Type |
|---------|----------|----------------------|
| E01 | Question not in knowledge base | Refusal with explanation |
| E02 | Ambiguous question | Clarification request |
| E03 | Question contains conflicting info | Refusal or clarification request |
| E04 | Question with unsupported format | Refusal with explanation |
| E05 | Multi-part question with missing context | Clarification request |

---


