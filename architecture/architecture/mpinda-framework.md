# MPINDA 6-Layer Architecture

The MPINDA Framework structures prompt systems into enforceable layers, each with defined responsibilities and output contracts.

---

## 1. Mandate Layer

Defines the core objective and success criteria of the prompt.

Input:
- Business objective
- Intended outcome
- Deployment context

Output:
- Clear task definition
- Success condition

Failure Mode:
- Ambiguous objectives
- Misaligned output intent

---

## 2. Parameters Layer

Defines constraints and boundaries.

Input:
- Tone requirements
- Length limits
- Structural rules
- Compliance requirements

Failure Mode:
- Over-general responses
- Tone drift
- Instruction leakage

---

## 3. Intelligence Structure

Defines reasoning depth and analytical format.

Examples:
- Step-by-step reasoning
- Comparative analysis
- Risk-based evaluation
- Scenario modeling

Failure Mode:
- Surface-level reasoning
- Missing trade-offs

---

## 4. Non-Negotiables

Explicit prohibitions and hard constraints.

Examples:
- No fabricated statistics
- No unverifiable claims
- Flag assumptions

Failure Mode:
- Hallucination risk
- Fabricated authority

---

## 5. Deliverable Schema

Defines output structure format.

Examples:
- JSON schema
- Sectioned report
- Scoring table

Failure Mode:
- Structural inconsistency
- Missing required sections

---

## 6. Assurance Layer

Validates output integrity before deployment.

Includes:
- Risk detection
- Confidence classification
- Deployment readiness scoring
