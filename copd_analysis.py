"""COPD analysis module.

This module provides a function to determine COPD diagnosis and GOLD classification
based on patient spirometry data.
"""

from typing import Dict


def analyze_patient(fev1: float, fvc: float, fev1_percent: float) -> Dict[str, str]:
    """Analyze patient data to diagnose COPD and classify its severity.

    Parameters
    ----------
    fev1: float
        Forced expiratory volume in the first second (liters).
    fvc: float
        Forced vital capacity (liters).
    fev1_percent: float
        FEV1 expressed as percent of the predicted value.

    Returns
    -------
    Dict[str, str]
        A dictionary with keys ``diagnosis`` and ``classification``.
    """
    ratio = fev1 / fvc
    diagnosed = ratio < 0.70

    if diagnosed:
        if fev1_percent >= 80:
            classification = "GOLD 1: Mild"
        elif fev1_percent >= 50:
            classification = "GOLD 2: Moderate"
        elif fev1_percent >= 30:
            classification = "GOLD 3: Severe"
        else:
            classification = "GOLD 4: Very Severe"
        diagnosis = "COPD"
    else:
        classification = "Not Applicable"
        diagnosis = "No COPD"

    return {"diagnosis": diagnosis, "classification": classification}

