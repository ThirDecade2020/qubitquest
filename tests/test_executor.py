from utils.executor import execute_code

def test_execute_code_prints():
    code_str = "print('hello')"
    output = execute_code(code_str)
    assert "hello" in output

def test_execute_code_error():
    code_str = "raise ValueError('oops')"
    output = execute_code(code_str)
    assert "Error executing code" in output