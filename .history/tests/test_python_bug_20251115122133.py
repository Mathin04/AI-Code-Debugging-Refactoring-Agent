from agent import code_debugger_agent

def test_bug():
    code = "def f():\n print('hi')"
    res = code_debugger_agent(code)
    assert res.language == "python"
