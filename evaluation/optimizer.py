from evaluation.evaluator import evaluate


def optimize():
    results = evaluate()

    failures = [r for r in results if r["has_error"]]

    print("\nFailures:", len(failures))

    if not failures:
        print("System stable")
    else:
        print("Investigate provider/API failures")


if __name__ == "__main__":
    optimize()
