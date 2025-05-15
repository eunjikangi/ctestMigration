# C++ to Python Test Migration Tool

This tool helps migrate C++ test cases to Python PyTest format using LLM and RAG techniques.

## Features

- Extracts test cases from C++ test files
- Uses RAG to provide context to LLM
- Converts C++ test cases to Python PyTest format
- Maintains test logic and assertions

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
```

3. Configure source and target directories in `config.py`

## Usage

1. Place your C++ test files in the source directory
2. Run the migration tool:
```bash
python src/main.py
```

3. Find converted PyTest files in the target directory

## Project Structure

- `src/` - Main source code
  - `main.py` - Entry point
  - `extractor.py` - C++ test case extractor
  - `converter.py` - Test case converter
  - `rag.py` - RAG implementation
  - `config.py` - Configuration
- `tests/` - Test files
- `requirements.txt` - Python dependencies 