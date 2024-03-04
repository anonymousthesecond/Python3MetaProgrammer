# File: code_builder.py

from typing import List, Union

class CodeBuilder:
    """
    A class to build Python code dynamically with functionalities for control flow, indentation, and error handling
    """
    def __init__(self, indent=0):
        """
        Initialize a CodeBuilder object with optional indentation.

        Args:
            indent (int): The initial indentation level.
        """
        self.code_lines: List[str] = []
        self.indent = indent

    def add_line(self, line: str) -> None:
        """
        Add a line of code to the code builder with proper indentation.

        Args:
            line (str): The line of code to add.
        """
        self.code_lines.append(" " * self.indent + line)

    def add_formatted_line(self, template: 'CodeTemplate') -> None:
        """
        Add a formatted line of code to the code builder using a CodeTemplate object.

        Args:
            template (CodeTemplate): The CodeTemplate object containing placeholders.
        """
        self.add_line(template.render())

    def indent(self) -> None:
        """Increase the indentation level."""
        self.indent += 2

    def dedent(self) -> None:
        """
        Decrease the indentation level.

        Raises:
            IndentationError: If the indentation level becomes negative.
        """
        if self.indent > 0:
            self.indent -= 2
        else:
            raise IndentationError("Indent cannot be negative")

    def add_control_flow(self, statement: str, condition: str = None, body: Union[str, 'CodeBuilder'] = None) -> None:
        """
        Add a control flow statement with optional condition and body.

        Args:
            statement (str): The control flow statement (e.g., "if", "for", "while").
            condition (str): The condition for the control flow statement.
            body (Union[str, 'CodeBuilder']): The body of the control flow statement.
                It can be either a string or a CodeBuilder object.

        Raises:
            TypeError: If the body is neither a string nor a CodeBuilder object.
        """
        if condition:
            self.add_line(f"{statement} ({condition}):")
        else:
            self.add_line(f"{statement}:")
        if isinstance(body, str):
            self.add_line(body)
        elif isinstance(body, CodeBuilder):
            body.indent()
            self.code_lines.extend(body.code_lines)
            body.dedent()
        else:
            raise TypeError("Body for control flow should be string or CodeBuilder")

    def get_code(self) -> str:
        """
        Get the generated Python code as a single string.

        Returns:
            str: The generated Python code.
        """
        return "\n".join(self.code_lines)
      
