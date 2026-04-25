import json
import os
from app.service import run_prompt_playground

BASE = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE, "test_cases.json")


def has_error_block(block):
    if not isinstance(block, dict):
        return True

    return any(str(val).lower().startswith("error") for val in block.values())


def evaluate():
    with open(TEST_FILE) as f:
        cases = json.load(f)

    results = []

    for case in cases:
        output = run_prompt_playground(case["input"])

        variation_count = len(output.keys())

        has_error = any(
            has_error_block(v) for v in output.values()
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
    avg_variations = sum(r["variation_count"] for r in results) / total if total else 0
    errors = sum(1 for r in results if r["has_error"])

    print("\n=== SUMMARY ===")
    print(f"Total cases: {total}")
    print(f"Average variations: {round(avg_variations,2)}")
    print(f"Cases with errors: {errors}")


if __name__ == "__main__":
    res = evaluate()
    summarize(res)
