import sys
import io

def execute_code(code_str):
    """
    Executes the given code string and captures stdout output.
    Returns the printed output or any exception message.
    """
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        exec(code_str, {})
        output = redirected_output.getvalue()
    except Exception as e:
        output = f"Error executing code: {e}"
    finally:
        sys.stdout = old_stdout
    return output