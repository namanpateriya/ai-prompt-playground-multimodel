import json
import os
from app.service import run_prompt_playground

BASE = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE, "test_cases.json")


def evaluate():
    with open(TEST_FILE) as f:
        cases = json.load(f)

    results = []

    for case in cases:
        output = run_prompt_playground(case["input"])

        variation_count = len(output.keys())
        has_error = any(
            "error" in v.values() if isinstance(v, dict) else False
            for v in output.values()
        )

        results.append({
            "input": case["input"],
            "variation_count": variation_count,
            "has_error": has_error
        })

        print("\nInput:", case["input"])
        print("Output:", json.dumps(output, indent=2))

    return results


def summarize(results):
    total = len(results)
    avg_variations = sum(r["variation_count"] for r in results) / total

    errors = sum(1 for r in results if r["has_error"])

    print("\n=== SUMMARY ===")
    print(f"Total cases: {total}")
    print(f"Average variations: {avg_variations}")
    print(f"Cases with errors: {errors}")


if __name__ == "__main__":
    res = evaluate()
    summarize(res)
