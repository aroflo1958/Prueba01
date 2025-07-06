import os, sys; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from src.copd_analyzer import diagnose, gold_stage, risk_group


def test_diagnosis_positive_stage1_group_a():
    patient = {
        "fev1_fvc": 0.65,
        "fev1_percent_predicted": 85,
        "symptom_score": 1,
        "exacerbations_last_year": 0,
        "hospitalizations_last_year": 0,
    }
    result = diagnose(patient)
    assert result["diagnosis"] is True
    assert result["gold_stage"] == 1
    assert result["risk_group"] == "A"


def test_diagnosis_positive_stage3_group_d():
    patient = {
        "fev1_fvc": 0.55,
        "fev1_percent_predicted": 45,
        "symptom_score": 3,
        "exacerbations_last_year": 2,
        "hospitalizations_last_year": 1,
    }
    result = diagnose(patient)
    assert result["diagnosis"] is True
    assert result["gold_stage"] == 3
    assert result["risk_group"] == "D"


def test_no_copd_diagnosis():
    patient = {
        "fev1_fvc": 0.8,
        "fev1_percent_predicted": 90,
        "symptom_score": 0,
        "exacerbations_last_year": 0,
        "hospitalizations_last_year": 0,
    }
    result = diagnose(patient)
    assert result["diagnosis"] is False
    assert result["gold_stage"] is None
    assert result["risk_group"] is None

