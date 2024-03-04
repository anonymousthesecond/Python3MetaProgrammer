# File: main.py

from code_builder import CodeBuilder, CodeTemplate
from code_generator import generate_function, generate_class

# Example Usage: (This can be extended for more complex scenarios)

# Create a CodeTemplate instance to represent a function body with a placeholder
function_body = CodeBuilder()
function_body.add_formatted_line(CodeTemplate("return x * $y"))  # Illustrates placeholder usage

# Generate a Python function named "multiply" with arguments "x" and "y" and the body defined by function_body
new_function_code = generate_function("multiply", "x, y", function_body)
print(new_function_code)

# Example for class generation
# Define class attributes
class_attributes = ["attr1", "attr2"]

# Define method bodies using CodeBuilder instances
method1_builder = CodeBuilder()
method1_builder.add_line("  print('Hello from method1')")

method2_builder = CodeBuilder()
method2_builder.add_control_flow("if", "attr1 > 0", CodeBuilder().add_line("  print('Positive value')"))

# Generate a Python class named "MyClass" with the defined attributes and methods
new_class_code = generate_class("MyClass", class_attributes, [method1_builder, method2_builder])
print(new_class_code)
