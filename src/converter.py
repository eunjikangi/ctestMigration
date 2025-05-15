from pathlib import Path
from typing import List, Dict
from config import TEST_TEMPLATE, TARGET_DIR

class TestConverter:
    def __init__(self, rag_system):
        self.rag_system = rag_system
        self.conversion_chain = rag_system.create_conversion_chain()
        
    def convert_test_case(self, test_case: Dict) -> str:
        """Convert a single test case using RAG"""
        # Prepare the test case for conversion
        test_case_text = f"""
        Test Suite: {test_case['test_suite']}
        Test Name: {test_case['test_name']}
        Test Body:
        {test_case['test_body']}
        """
        
        # Convert using RAG chain
        converted_test = self.conversion_chain.invoke(test_case_text)
        return converted_test
    
    def convert_test_file(self, test_cases: List[Dict], file_path: Path) -> None:
        """Convert all test cases from a file and save as Python test file"""
        # Convert all test cases
        converted_tests = []
        for test_case in test_cases:
            converted_test = self.convert_test_case(test_case)
            converted_tests.append(converted_test)
        
        # Prepare imports (this should be customized based on your needs)
        imports = [
            "import pytest",
            "import sys",
            "import os"
        ]
        
        # Create the test file content
        test_file_content = TEST_TEMPLATE.format(
            imports="\n".join(imports),
            test_cases="\n\n".join(converted_tests)
        )
        
        # Save the converted test file
        target_path = TARGET_DIR / f"{file_path.stem}_test.py"
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(test_file_content) 