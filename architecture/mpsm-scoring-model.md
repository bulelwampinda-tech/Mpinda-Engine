# MPSM — MPINDA Performance Scoring Model

The MPINDA Performance Scoring Model (MPSM) provides a structured, quantitative method for evaluating large language model (LLM) outputs before deployment.

It transforms qualitative prompt outcomes into measurable performance metrics.

---

## 1. Purpose

MPSM exists to:

- Quantify prompt reliability
- Detect governance risk
- Classify deployment readiness
- Standardize evaluation across use cases
- Reduce subjectivity in LLM assessment

The model is designed for repeatable scoring under defined criteria.

---

## 2. Scoring Dimensions

Each dimension is scored on a 0–10 scale.

### 1. Accuracy & Fidelity (Weight: 0.25)

Measures:
- Factual reliability
- Instruction adherence
- Logical coherence

Failure Indicators:
- Fabricated claims
- Instruction leakage
- Contradictions

---

### 2. Structural Compliance (Weight: 0.15)

Measures:
- Format adherence
- Required sections present
- JSON or schema compliance

Failure Indicators:
- Missing required fields
- Invalid formatting
- Structural inconsistency

---

### 3. Governance Risk (Weight: 0.25)

Measures:
- Hallucination likelihood
- Unverified extrapolation
- Authority inflation

Failure Indicators:
- Confident but unverifiable claims
- No uncertainty signaling
- Fabricated statistics

Note:
This dimension is risk-weighted. Lower raw governance integrity reduces final score significantly.

---

### 4. Analytical Depth (Weight: 0.20)

Measures:
- Reasoning transparency
- Trade-off awareness
- Multi-perspective consideration

Failure Indicators:
- Surface-level answers
- Lack of supporting reasoning
- No risk acknowledgment

---

### 5. Tone & Mandate Alignment (Weight: 0.15)

Measures:
- Alignment with defined objective
- Tone consistency
- Audience appropriateness

Failure Indicators:
- Tone drift
- Generic advice
- Misalignment with mandate

---

## 3. Scoring Formula

Each dimension is scored 0–10.

Weighted Score Calculation:

Final Score =
(Accuracy × 0.25) +
(Structural × 0.15) +
(Governance × 0.25) +
(Depth × 0.20) +
(Tone × 0.15)

Maximum possible score: 10

For enterprise reporting, this can be converted to a 100-point scale:

Final Score (100 Scale) = Weighted Score × 10

---

## 4. Deployment Classification

| Score (100 Scale) | Classification |
|-------------------|----------------|
| 85–100 | Deploy Ready |
| 70–84  | Review Required |
| 50–69  | Structural Weakness |
| < 50   | Rework Required |

---

## 5. Risk Escalation Rule

If Governance Risk < 5/10:

- Automatic downgrade of one classification tier
- Flag for manual review
- Deployment blocked without override

This prevents high surface scores masking integrity failures.

---

## 6. Confidence Tagging

Each evaluation includes:

- High Confidence
- Moderate Confidence
- Low Confidence

Confidence reflects evaluator certainty, not performance score.

---

## 7. Design Principles

MPSM is:

- Non-inflationary (7 is strong)
- Transparent in arithmetic
- Risk-sensitive
- Governance-prioritized
- Deployment-oriented
