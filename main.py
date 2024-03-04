from CodeTemplate import CodeTemplate
from CodeBuilder import CodeBuilder

# Example Usage:
function_body = CodeBuilder()
function_body.add_line("return x * $y")  # Illustrates placeholder usage

new_function_code = generate_function("multiply", "x, y", function_body)
print(new_function_code)
