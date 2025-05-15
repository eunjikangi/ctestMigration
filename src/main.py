import os
from pathlib import Path
from dotenv import load_dotenv
from typing import List

from config import SOURCE_DIR, TARGET_DIR
from rag import RAGSystem
from extractor import CppTestExtractor
from converter import TestConverter

def load_environment():
    """Load environment variables"""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set")

def main():
    # Load environment variables
    load_environment()
    
    # Initialize components
    rag_system = RAGSystem()
    extractor = CppTestExtractor(SOURCE_DIR)
    converter = TestConverter(rag_system)
    
    # Extract test cases
    print("Extracting test cases...")
    test_cases = extractor.extract_test_cases()
    
    if not test_cases:
        print("No test cases found in the source directory.")
        return
    
    # Group test cases by file
    test_cases_by_file = {}
    for test_case in test_cases:
        file_path = Path(test_case['file_path'])
        if file_path not in test_cases_by_file:
            test_cases_by_file[file_path] = []
        test_cases_by_file[file_path].append(test_case)
    
    # Create vector store from all test cases
    print("Creating vector store...")
    rag_system.create_vector_store(test_cases)
    
    # Convert test cases
    print("Converting test cases...")
    for file_path, cases in test_cases_by_file.items():
        print(f"Converting {file_path.name}...")
        converter.convert_test_file(cases, file_path)
    
    print(f"Conversion complete. Converted test files can be found in {TARGET_DIR}")

if __name__ == "__main__":
    main() 