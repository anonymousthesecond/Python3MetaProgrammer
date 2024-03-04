import unittest
from CodeBuilder import CodeBuilder

class TestCodeBuilder(unittest.TestCase):
    def test_add_line(self):
        builder = CodeBuilder()
        builder.add_line("def example_function():")
        builder.indent()
        builder.add_line("return True")
        builder.dedent()
        builder.add_line("")
        expected_code = "def example_function():\n    return True\n"
        self.assertEqual(builder.get_code(), expected_code)

    def test_add_control_flow(self):
        builder = CodeBuilder()
        builder.add_control_flow("if", "condition")
        builder.indent()
        builder.add_line("print('Condition is True')")
        builder.dedent()
        builder.add_line("else:")
        builder.indent()
        builder.add_line("print('Condition is False')")
        builder.dedent()
        expected_code = "if condition:\n    print('Condition is True')\nelse:\n    print('Condition is False')\n"
        self.assertEqual(builder.get_code(), expected_code)

if __name__ == '__main__':
    unittest.main()
  
