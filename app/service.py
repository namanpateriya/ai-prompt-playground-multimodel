from app.utils.model import ModelClient
from app.variations import VARIATIONS
from app.utils.logger import get_logger

logger = get_logger(__name__)
model = ModelClient()


def run_prompt_playground(input_text: str):
    if not input_text or not input_text.strip():
        return {"error": "Empty input"}

    # basic input length control
    input_text = input_text[:2000]

    outputs = {}

    for variation, template in VARIATIONS.items():
        prompt = template.format(input=input_text)

        logger.info(f"Running variation: {variation}")

        results = model.generate_all(prompt)

        outputs[variation] = results

    return outputs
