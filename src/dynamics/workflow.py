"""Generic business-process state machine for Dynamics-style workflows."""
TRANSITIONS = {
    "new": {"triaged"},
    "triaged": {"in_progress", "blocked"},
    "in_progress": {"resolved", "blocked"},
    "blocked": {"in_progress"},
    "resolved": set(),
}

def transition(state: str, target: str) -> str:
    if target not in TRANSITIONS.get(state, set()):
        raise ValueError(f"Invalid transition: {state} -> {target}")
    return target
