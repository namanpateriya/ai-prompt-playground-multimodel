import os

class ModelClient:

    def call_openai(self, prompt):
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return res.choices[0].message.content

    def call_anthropic(self, prompt):
        import anthropic
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        res = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.content[0].text

    def call_gemini(self, prompt):
        import google.generativeai as genai

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")

        res = model.generate_content(prompt)
        return res.text

    def generate_all(self, prompt):
        results = {}

        try:
            results["openai"] = self.call_openai(prompt)
        except:
            results["openai"] = "error"

        try:
            results["anthropic"] = self.call_anthropic(prompt)
        except:
            results["anthropic"] = "error"

        try:
            results["gemini"] = self.call_gemini(prompt)
        except:
            results["gemini"] = "error"

        return results
