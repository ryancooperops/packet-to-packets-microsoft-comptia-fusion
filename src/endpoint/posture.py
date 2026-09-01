"""Endpoint posture evaluation inspired by zero-trust management patterns."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Device:
    name: str
    encrypted: bool
    patched: bool
    edr_enabled: bool
    compliant_identity: bool

def posture(d: Device) -> str:
    controls = [d.encrypted, d.patched, d.edr_enabled, d.compliant_identity]
    if all(controls):
        return "compliant"
    if sum(controls) >= 3:
        return "remediate"
    return "non_compliant"
