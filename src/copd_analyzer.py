"""COPD Analyzer module based on the GOLD 2025 report.

This module provides utilities to diagnose Chronic Obstructive Pulmonary
Disease (COPD) and classify confirmed cases according to GOLD 2025
recommendations.

Patient data should be provided as a dictionary with the following keys:
    - fev1_fvc: ratio of FEV1/FVC post-bronchodilation (float)
    - fev1_percent_predicted: FEV1 percent predicted (float)
    - symptom_score: symptom burden score (mMRC or CAT equivalent)
    - exacerbations_last_year: number of exacerbations in the last year (int)
    - hospitalizations_last_year: number of COPD hospitalizations in the last year (int)

Example:
    >>> from src.copd_analyzer import diagnose
    >>> patient = {
    ...     'fev1_fvc': 0.62,
    ...     'fev1_percent_predicted': 78,
    ...     'symptom_score': 1,
    ...     'exacerbations_last_year': 0,
    ...     'hospitalizations_last_year': 0,
    ... }
    >>> diagnose(patient)
    {'diagnosis': True, 'gold_stage': 1, 'risk_group': 'A'}
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class PatientData:
    fev1_fvc: float
    fev1_percent_predicted: float
    symptom_score: int
    exacerbations_last_year: int
    hospitalizations_last_year: int


def diagnose(data: Dict[str, Any]) -> Dict[str, Optional[Any]]:
    """Return COPD diagnosis and classification results.

    Parameters
    ----------
    data : dict
        Patient data as described in the module docstring.
    """
    patient = PatientData(**data)

    diagnosis = patient.fev1_fvc < 0.7
    stage = gold_stage(patient.fev1_percent_predicted) if diagnosis else None
    group = (
        risk_group(
            patient.symptom_score,
            patient.exacerbations_last_year,
            patient.hospitalizations_last_year,
        )
        if diagnosis
        else None
    )
    return {"diagnosis": diagnosis, "gold_stage": stage, "risk_group": group}


def gold_stage(fev1_percent: float) -> int:
    """Classify COPD GOLD stage based on FEV1 percent predicted."""
    if fev1_percent >= 80:
        return 1
    if fev1_percent >= 50:
        return 2
    if fev1_percent >= 30:
        return 3
    return 4


def risk_group(symptom_score: int, exacerbations: int, hospitalizations: int) -> str:
    """Return GOLD risk group (A, B, C, D) based on symptoms and exacerbations."""

    high_symptoms = symptom_score >= 2
    high_risk = exacerbations >= 2 or hospitalizations >= 1

    if not high_symptoms and not high_risk:
        return "A"
    if high_symptoms and not high_risk:
        return "B"
    if not high_symptoms and high_risk:
        return "C"
    return "D"
