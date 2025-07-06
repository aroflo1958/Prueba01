"""COPD analysis utilities."""

from .copd_analyzer import diagnose, gold_stage, risk_group, PatientData

__all__ = [
    "diagnose",
    "gold_stage",
    "risk_group",
    "PatientData",
]
