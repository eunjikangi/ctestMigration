import re
from pathlib import Path
from typing import List, Dict

class CppTestExtractor:
    def __init__(self, source_dir: Path):
        self.source_dir = source_dir
        
    def extract_test_cases(self) -> List[Dict]:
        """Extract test cases from C++ test files"""
        test_cases = []
        
        for file_path in self.source_dir.glob("**/*.cpp"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract test cases using regex patterns
            # This pattern should be adjusted based on your C++ test framework
            test_pattern = r'TEST\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)\s*{([^}]+)}'
            matches = re.finditer(test_pattern, content, re.DOTALL)
            
            for match in matches:
                test_suite = match.group(1)
                test_name = match.group(2)
                test_body = match.group(3).strip()
                
                test_cases.append({
                    'file_path': str(file_path),
                    'test_suite': test_suite,
                    'test_name': test_name,
                    'test_body': test_body
                })
                
        return test_cases
    
    def extract_imports(self, content: str) -> List[str]:
        """Extract import statements from C++ test file"""
        import_pattern = r'#include\s*<([^>]+)>'
        return re.findall(import_pattern, content)
    
    def extract_test_dependencies(self, test_body: str) -> List[str]:
        """Extract test dependencies from test body"""
        # This pattern should be adjusted based on your test framework
        dependency_pattern = r'ASSERT_|EXPECT_|REQUIRE_'
        return re.findall(dependency_pattern, test_body) 