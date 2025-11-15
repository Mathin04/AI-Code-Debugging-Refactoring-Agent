from tools.parser import detect_language

def test_detect():
    assert detect_language("def a(): pass") == "python"
