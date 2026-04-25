# AI Prompt Playground (Multi-Model)

Experiment with prompt variations across multiple AI models and compare outputs.

Supports:

* CLI-based prompt experimentation
* API-based prompt experimentation

---

## Features

* Run prompts across multiple providers (OpenAI, Anthropic, Gemini)
* Compare outputs across models
* Prompt variations (concise, detailed, bullet points, beginner)
* Lightweight and easy to use
* CLI and API support
* Evaluation support

---

## Setup

```bash
git clone <repo_url>
cd ai-prompt-playground-multimodel
pip install -r requirements.txt
```

Create `.env` file:

```
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GEMINI_API_KEY=your_key
```

For API based execution

```
uvicorn app.main:app --reload
Open Swagger UI - http://127.0.0.1:8000/docs
```

For CLI based execution
Run using the client cli.py with appropriate options

---

# Execution Modes

## Direct Mode (CLI)

```bash
python -m app.cli --input "Explain artificial intelligence"
```

---

## Direct Mode (API)

Endpoint:

POST /run

Sample request:

```
{
  "input": "Explain artificial intelligence"
}
```

---

# CLI Options

| Option  | Description  |
| ------- | ------------ |
| --input | Input prompt |

---

# Use Cases

* Compare outputs across AI models
* Test prompt variations quickly
* Understand differences in model behavior
* Experiment with prompt engineering strategies
* Evaluate responses across providers

---

# Roadmap

* Add support for more providers
* Add response scoring and ranking
* Add UI for interactive experimentation
* Add prompt templates library
* Add export functionality

---

Built for fast experimentation and ecosystem exploration
