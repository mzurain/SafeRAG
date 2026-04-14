---
title: RAG Agent
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.41.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# RAG Agent
My local document search agent!


# SafeRAG — Local AI Agent with ChromaDB + DuckDuckGo

A local AI agent built with LangChain and LangGraph that answers questions from your own ingested documents (PDFs, text files) or searches the web via DuckDuckGo. Runs fully offline using Ollama. Includes a Gradio web UI.

## Features

- **ChromaDB retriever** — search your own ingested documents
- **DuckDuckGo search** — live web search for anything not in your documents
- **Gradio web UI** — chat interface with Send and Clear History buttons
- **3-layer prompt injection & harmful content protection**
  - Layer 1: Hardcoded regex patterns for known injection phrases
  - Layer 2: Hardcoded regex patterns for harmful/illegal content (weapons, drugs, violence)
  - Layer 3: LLM-based AI judge as a catch-all

## Requirements

- [Ollama](https://ollama.com/download) installed and running
- Python 3.10+

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd SafeRAG
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

4. Add your documents (PDF or TXT) to the project folder, update the file paths in `ingest.py`, then run:
   ```bash
   python ingest.py
   ```

5. Start the agent (terminal):
   ```bash
   python BasicAgent.py
   ```

   Or launch the Gradio web UI:
   ```bash
   python app.py
   ```
   Then open `http://127.0.0.1:7860` in your browser.

## Project Structure

```
SafeRAG/
├── BasicAgent.py      # Main agent with tools and safety checks
├── ingest.py          # Document ingestion into ChromaDB
├── app.py             # Gradio web UI
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
Answer: [summarized web search results]

Ask: ignore previous instructions
Answer: ⚠️ Query blocked: hardcoded pattern.

Ask: teach me how to build a gun
Answer: ⚠️ Query blocked: harmful content.
```

## Notes

- `chroma_db/` is excluded from git — run `ingest.py` after cloning to rebuild it
- Larger models (e.g. `qwen2.5:7b`, `llama3.2:3b`) will give more reliable tool-calling behavior
