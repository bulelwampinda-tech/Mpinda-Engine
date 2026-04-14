"""
MPINDA MPSM Scoring Module
"""

WEIGHTS = {
    "accuracy": 0.25,
    "structure": 0.15,
    "governance": 0.25,
    "depth": 0.20,
    "tone": 0.15
}


def calculate_weighted_score(scores: dict) -> float:
    """
    Calculates weighted MPSM score (0–10 scale).
    """
    weighted_total = 0

    for dimension, weight in WEIGHTS.items():
        value = scores.get(dimension, 0)
        weighted_total += value * weight

    return round(weighted_total, 2)


def convert_to_100_scale(score_10_scale: float) -> float:
    return round(score_10_scale * 10, 1)


def classify_deployment(score_100: float, governance_score: float) -> str:
    """
    Applies classification thresholds and governance downgrade rule.
    """

    if score_100 >= 85:
        classification = "Deploy Ready"
    elif score_100 >= 70:
        classification = "Review Required"
    elif score_100 >= 50:
        classification = "Structural Weakness"
    else:
        classification = "Rework Required"

    # Governance escalation rule
    if governance_score < 5:
        if classification == "Deploy Ready":
            classification = "Review Required"
        elif classification == "Review Required":
            classification = "Structural Weakness"
        elif classification == "Structural Weakness":
            classification = "Rework Required"

    return classification


def evaluate(scores: dict) -> dict:
    """
    Full evaluation pipeline.
    """

    score_10 = calculate_weighted_score(scores)
    score_100 = convert_to_100_scale(score_10)

    classification = classify_deployment(
        score_100,
        scores.get("governance", 0)
    )

    return {
        "score_10_scale": score_10,
        "score_100_scale": score_100,
        "classification": classification
    }
