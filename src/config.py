import os
from pathlib import Path

# Directory configurations
BASE_DIR = Path(__file__).parent.parent
SOURCE_DIR = BASE_DIR / "source_cpp_tests"
TARGET_DIR = BASE_DIR / "target_python_tests"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

# Create directories if they don't exist
SOURCE_DIR.mkdir(exist_ok=True)
TARGET_DIR.mkdir(exist_ok=True)
VECTOR_DB_DIR.mkdir(exist_ok=True)

# OpenAI configuration
OPENAI_MODEL = "gpt-4-turbo-preview"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# RAG configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 3

# Test conversion configuration
TEST_TEMPLATE = """
import pytest

{imports}

{test_cases}
""" 