import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from copd_analysis import analyze_patient


def test_diagnosis_positive():
    result = analyze_patient(1.0, 2.0, 45)
    assert result["diagnosis"] == "COPD"
    assert result["classification"] == "GOLD 3: Severe"


def test_diagnosis_negative():
    result = analyze_patient(3.0, 3.0, 90)
    assert result["diagnosis"] == "No COPD"
    assert result["classification"] == "Not Applicable"
