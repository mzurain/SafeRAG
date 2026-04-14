# Local AI Agent — ChromaDB + DuckDuckGo

A local AI agent built with LangChain and LangGraph that answers questions from your own ingested documents (PDFs, text files) or searches the web via DuckDuckGo. Runs fully offline using Ollama.

## Features

- **ChromaDB retriever** — search your own ingested documents
- **DuckDuckGo search** — live web search for anything not in your documents
- **3-layer prompt injection & harmful content protection**
  - Layer 1: Hardcoded regex patterns for known injection phrases
  - Layer 2: Hardcoded regex patterns for harmful/illegal content
  - Layer 3: LLM-based AI judge as a catch-all

## Requirements

- [Ollama](https://ollama.com/download) installed and running
- Python 3.10+

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Pull the required Ollama models:
   ```bash
   ollama pull qwen2.5:3b
   ollama pull nomic-embed-text
   ```

4. Add your documents (PDF or TXT) to the project folder and update the file paths in `ingest.py`, then run:
   ```bash
   python ingest.py
   ```

5. Start the agent:
   ```bash
   python BasicAgent.py
   ```

## Project Structure

```
Agent/
├── BasicAgent.py      # Main agent with tools and safety checks
├── ingest.py          # Document ingestion into ChromaDB
├── requirements.txt   # Python dependencies
└── README.md
```

## How It Works

```
User Input
    │
    ▼
Safety Check (3 layers)
    │ blocked → print warning and skip
    ▼
Agent (qwen2.5:3b via Ollama)
    │
    ├── chromadb_search → query local vector store
    └── duckduckgo_search → query the web
    │
    ▼
Answer
```

## Usage Example

```
Ask: What is the patient's name in the appointment reminder?
Answer: The patient's name is John Smith and the appointment date is 2024-04-01.

Ask: What is the latest news about AI?
Answer: [web search results]

Ask: ignore previous instructions
Answer: Potential prompt injection detected (hardcoded pattern). Query blocked.
```

## Notes

- `chroma_db/` is excluded from git — run `ingest.py` after cloning to rebuild it
- Larger models (e.g. `qwen2.5:7b`, `llama3.2:3b`) will give more reliable tool-calling behavior
