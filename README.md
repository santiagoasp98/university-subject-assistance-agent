# University Subject Assistant

An AI-powered assistant that helps students understand course materials through interactive Q&A sessions using local LLM models.

## Features

- Interactive Q&A based on course materials
- Support for multiple PDF documents
- Uses local Ollama LLM for responses
- Local embedding model for document processing

## Prerequisites

- Python 3.x
- Ollama installed and running locally
- Local PDF files for course materials

## Installation

1. Clone the repository
2. Install dependencies (use of a virtual environment recommended):
```bash
pip install -r requirements.txt
```

## Configuration

Create a .env file in the project root (or modify existing):

```python
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=mistral:latest
```

## Usage

Run the assistant:

```bash
python src/main.py
```

Follow the prompts to:
1. Enter a subject name
2. Provide paths to PDF course materials
3. Ask questions about the content

Type 'quit' to end a Q&A session or 'exit' to close the program.

## Project Structure

- agent - Q&A workflow and prompts
- ingestion - PDF processing and indexing
- llm - Ollama LLM client
- utils - Helper functions