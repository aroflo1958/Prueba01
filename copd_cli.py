"""Command-line interface for COPD analysis."""

import argparse
from copd_analysis import analyze_patient


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze patient data for COPD")
    parser.add_argument("--fev1", type=float, required=True, help="FEV1 in liters")
    parser.add_argument("--fvc", type=float, required=True, help="FVC in liters")
    parser.add_argument(
        "--fev1_percent",
        type=float,
        required=True,
        help="FEV1 expressed as percent of predicted value",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    result = analyze_patient(args.fev1, args.fvc, args.fev1_percent)
    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Classification: {result['classification']}")


if __name__ == "__main__":
    main()

