from app.utils.model import ModelClient
from app.variations import VARIATIONS

model = ModelClient()

def run_prompt_playground(input_text):

    outputs = {}

    for key, template in VARIATIONS.items():
        prompt = template.format(input=input_text)

        results = model.generate_all(prompt)

        outputs[key] = results

    return outputs
