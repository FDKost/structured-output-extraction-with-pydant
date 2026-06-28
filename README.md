# Structured Output Extraction CLI

This project demonstrates how to extract structured data from free‑text using **LangChain** and **Pydantic**.  
It supports two schemas:

- **PersonInfo** – basic personal details  
- **MeetingNotes** – meeting agenda, participants, decisions, etc.

The CLI automatically selects the appropriate schema based on the input text and returns a fully validated Pydantic model.

## Installation

```bash
# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Using a built‑in example
python -m src.cli --example person
python -m src.cli --example meeting

# Provide your own text
python -m src.cli --text "John Doe is a 35‑year‑old software engineer..."
```

### Optional arguments

- `--model` – OpenAI model name (default: `gpt-3.5-turbo`)
- `--temperature` – LLM temperature (default: `0.0`)

## Environment Variables

Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=sk-...
```

## Running Tests

```bash
pytest
```

## License

MIT
