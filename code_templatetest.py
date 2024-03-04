import unittest
from CodeTemplate import CodeTemplate

class TestCodeTemplate(unittest.TestCase):
    def test_render(self):
        template = CodeTemplate("def $function_name($arg1, $arg2):")
        template.set_value("function_name", "example_function")
        template.set_value("arg1", "param1")
        template.set_value("arg2", "param2")
        rendered_template = template.render()
        self.assertEqual(rendered_template, "def example_function(param1, param2):")

if __name__ == '__main__':
    unittest.main()
  
