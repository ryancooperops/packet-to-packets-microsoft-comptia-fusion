from security.risk_engine import Finding, prioritize
from endpoint.posture import Device, posture
from network.segmentation import Flow, allowed
from data_ai.pipeline import Record, validate
from dynamics.workflow import transition

def test_risk_priority():
    result = prioritize([Finding("a", .9, .9, .8), Finding("b", .2, .2, .2)])
    assert result[0][0] == "a"

def test_endpoint_posture():
    assert posture(Device("d1", True, True, True, True)) == "compliant"
    assert posture(Device("d2", True, True, False, True)) == "remediate"

def test_network_policy():
    assert allowed(Flow("user", "app", 443))
    assert not allowed(Flow("user", "data", 5432))

def test_data_quality():
    result = validate([Record("c1", "hello", .9), Record("", "", 2)])
    assert result["valid"] is False
    assert result["accepted"] == 0

def test_workflow():
    assert transition("new", "triaged") == "triaged"
