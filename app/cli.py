import argparse
import json
from app.service import run_prompt_playground

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)

args = parser.parse_args()

result = run_prompt_playground(args.input)

print(json.dumps(result, indent=2))
