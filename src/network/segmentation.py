"""Simple network segmentation policy model."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Flow:
    source_zone: str
    destination_zone: str
    port: int

ALLOWED = {
    ("user", "app", 443),
    ("app", "data", 5432),
    ("admin", "management", 443),
}

def allowed(flow: Flow) -> bool:
    return (flow.source_zone, flow.destination_zone, flow.port) in ALLOWED
