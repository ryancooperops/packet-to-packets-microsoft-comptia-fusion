"""Small data-quality gate suitable for an AI/data pipeline prototype."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Record:
    customer_id: str
    text: str
    confidence: float

def validate(records: list[Record]) -> dict:
    errors = []
    for i, r in enumerate(records):
        if not r.customer_id.strip(): errors.append((i, "missing_customer_id"))
        if not r.text.strip(): errors.append((i, "empty_text"))
        if not 0 <= r.confidence <= 1: errors.append((i, "invalid_confidence"))
    return {"valid": not errors, "errors": errors, "accepted": len(records) - len(errors)}
