import pandas as pd
from patient_loader import load_from_csv
from data_models import Patient


def test_load_from_csv(tmp_path):
    csv_file = tmp_path / 'patients.csv'
    df = pd.DataFrame([
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 40},
    ])
    df.to_csv(csv_file, index=False)

    patients = load_from_csv(str(csv_file))
    assert patients == [
        Patient(id=1, name='Alice', age=30),
        Patient(id=2, name='Bob', age=40),
    ]
