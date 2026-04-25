import os
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ModelClient:

    def call_openai(self, prompt):
        try:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "error: missing OPENAI_API_KEY"

            from openai import OpenAI
            client = OpenAI(api_key=api_key)

            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return res.choices[0].message.content

        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            return "error"

    def call_anthropic(self, prompt):
        try:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                return "error: missing ANTHROPIC_API_KEY"

            import anthropic
            client = anthropic.Anthropic(api_key=api_key)

            res = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            if res.content and len(res.content) > 0:
                return res.content[0].text

            return "error"

        except Exception as e:
            logger.error(f"Anthropic error: {e}")
            return "error"

    def call_gemini(self, prompt):
        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return "error: missing GEMINI_API_KEY"

            import google.generativeai as genai

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")

            res = model.generate_content(prompt)

            if hasattr(res, "text") and res.text:
                return res.text

            return str(res)

        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return "error"

    def generate_all(self, prompt):
        return {
            "openai": self.call_openai(prompt),
            "anthropic": self.call_anthropic(prompt),
            "gemini": self.call_gemini(prompt)
        }
