import ast
import os
from typing import Optional, List

LANG_EXT = {
    'python': ['.py'],
    'java': ['.java'],
    'cpp': ['.cpp']
}

def detect_language(code: str, filename: Optional[str] = None) -> str:
    if filename and filename.endswith('.py'):
        return 'python'
    if filename and filename.endswith('.java'):
        return 'java'
    if filename and filename.endswith('.cpp'):
        return 'cpp'

    if 'def ' in code:
        return 'python'
    if '#include' in code:
        return 'cpp'
    if 'class ' in code and 'public static void main' in code:
        return 'java'

    return 'text'

def analyze_python(code: str) -> List[str]:
    issues = []
    try:
        ast.parse(code)
    except SyntaxError as e:
        issues.append(f"SyntaxError: {e.msg} at line {e.lineno}")
    return issues
