from pydantic import BaseModel
from typing import List, Optional, Dict
from tools.parser import detect_language, analyze_python
from tools.optimizer import call_llm_refactor
from tools.tester import run_python, compile_java, compile_cpp, run_compiled
import tempfile

class DebugResult(BaseModel):
    language: str
    errors: List[str]
    suggestions: List[str]
    optimized_code: Optional[str]
    test_output: Optional[str]
    metadata: Dict = {}

def code_debugger_agent(code: str, filename_hint: Optional[str] = None, run_tests: bool = True) -> DebugResult:
    language = detect_language(code, filename_hint)
    errors = []
    suggestions = []
    optimized = None
    test_output = None
    metadata = {}

    if language == 'python':
        issues = analyze_python(code)
        errors += issues
    elif language == 'java':
        with tempfile.TemporaryDirectory() as td:
            ok, out = compile_java(code, td)
            if not ok:
                errors.append('Java compile error: ' + out)
    elif language == 'cpp':
        with tempfile.TemporaryDirectory() as td:
            ok, out = compile_cpp(code, td)
            if not ok:
                errors.append('C++ compile error: ' + out)

    optimized = call_llm_refactor(code, language)

    if run_tests and language == 'python':
        test_output = run_python(optimized)

    if not errors:
        suggestions.append('No major issues detected.')
    else:
        suggestions.append('Fix above errors and re-run.')

    return DebugResult(
        language=language,
        errors=errors,
        suggestions=suggestions,
        optimized_code=optimized,
        test_output=test_output,
        metadata=metadata
    )
