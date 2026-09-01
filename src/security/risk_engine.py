"""Vendor-neutral security risk scoring example."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Finding:
    asset: str
    likelihood: float  # 0..1
    impact: float      # 0..1
    exposure: float    # 0..1

    def score(self) -> float:
        values = (self.likelihood, self.impact, self.exposure)
        if any(not 0 <= x <= 1 for x in values):
            raise ValueError("likelihood, impact and exposure must be in [0, 1]")
        return round(self.likelihood * self.impact * (0.5 + 0.5 * self.exposure), 4)

def prioritize(findings: list[Finding]) -> list[tuple[str, float]]:
    return sorted(((f.asset, f.score()) for f in findings), key=lambda x: x[1], reverse=True)
