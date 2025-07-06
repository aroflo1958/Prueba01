import pandas as pd
from data_models import Patient


def load_from_csv(path: str) -> list[Patient]:
    """Load patient records from a CSV file."""
    df = pd.read_csv(path)
    return [Patient(**row.to_dict()) for _, row in df.iterrows()]
