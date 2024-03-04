import unittest
from CodeGenerator import generate_function, generate_class
from CodeBuilder import CodeBuilder

class TestCodeGenerator(unittest.TestCase):
    def test_generate_function(self):
        function_body = CodeBuilder()
        function_body.add_line("return x * $y")  # Placeholder usage
        new_function_code = generate_function("multiply", "x, y", function_body)
        expected_code = "def multiply(x, y):\n    return x * y\n"
        self.assertEqual(new_function_code, expected_code)

    def test_generate_class(self):
        class_attributes = ["attr1", "attr2"]
        method1_builder = CodeBuilder()
        method1_builder.add_line("print('Hello from method1')")
        method2_builder = CodeBuilder()
        method2_builder.add_control_flow("if", "attr1 > 0", "print('Positive value')")
        new_class_code = generate_class("MyClass", class_attributes, [method1_builder, method2_builder])
        expected_code = "class MyClass:\n    attr1\n    attr2\n    def method1(self):\n        print('Hello from method1')\n    def method2(self):\n        if attr1 > 0:\n            print('Positive value')\n"
        self.assertEqual(new_class_code, expected_code)

if __name__ == '__main__':
    unittest.main()
  
